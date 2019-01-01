from collections import deque
from itertools import count


def parse_input():
    rules = dict()
    with open('input.txt', 'r') as f:
        state = f.readline()[14:].strip()
        for line in f:
            split_str = line.split()
            if split_str:
                rules[split_str[0]] = split_str[2]

    return state, rules


class State:
    def __init__(self, i, d):
        # i is index corresponding to first element in d
        # d is a deque with '.' or '#' for dead and live plants
        self.i = i
        self.d = d

    def __iter__(self):
        # yield plant states with ends as required for use in evolve
        yield from self.d
        for _ in range(4):
            yield '.'

    def __str__(self):
        return "{:3d} {}".format(self.i, "".join(iter(self.d)))

    def mutate(self, rules):
        new_i = self.i - 2
        new_d = deque()

        temp = deque('.....', maxlen=5)
        for x in iter(self):
            temp.append(x)
            new_d.append(rules.get("".join(temp), '.'))

        while new_d[0] == '.':
            new_d.popleft()
            new_i += 1

        while new_d[-1] == '.':
            new_d.pop()

        return State(new_i, new_d)

    def sum(self):
        return sum(i for i, x in zip(count(start=self.i), self.d) if x == '#')


def sum_generator(gene, rules):
    index = 0
    while True:
        gene = gene.mutate(rules)
        gene_sum = gene.sum()
        index += 1

        yield index, gene_sum


if __name__ == '__main__':
    state_str, rules = parse_input()

    state = State(0, deque(state_str))
    gene = sum_generator(state, rules)

    for _ in range(20):
        result = next(gene)
    print(result[1])

    sums = deque(maxlen=4)
    # continue until the sums are consistently changing linearly
    while len(sums) < 4 or not all(sums[i] == sums[0] + i * (sums[1] - sums[0]) for i in range(2, len(sums))):
        i, x = next(gene)
        sums.append(x)

    print(sums[-1] + (sums[1] - sums[0]) * (int(5e10) - i))
