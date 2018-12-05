from copy import deepcopy
from string import ascii_lowercase


def polymer(char_list):
    # define pointers
    p1 = 0
    p2 = 1

    while p2 < len(char_list):
        if char_list[p1].swapcase() == char_list[p2]:
            if p1 != 0:
                char_list.pop(p2)
                char_list.pop(p1)
                p1 -= 1
                p2 -= 1
            else:
                char_list.pop(1)
                char_list.pop(0)
        else:
            p1 = p2
            p2 += 1

    return char_list


def find_lowest_possible_length(reduced_list):
    lowest_length = len(reduced_list)

    for c in ascii_lowercase:
        new_list = deepcopy(reduced_list)
        new_list = list(filter(lambda a: a != c and a != c.swapcase(), new_list))

        possible_list = polymer(new_list)

        if len(possible_list) < lowest_length:
            lowest_length = len(possible_list)

    return lowest_length


if __name__ == '__main__':
    input_list = []

    with open('input.txt') as f:
        for line in f:
            for c in line:
                input_list.append(c)

    print(len(polymer(input_list)))
    print(find_lowest_possible_length(input_list))
