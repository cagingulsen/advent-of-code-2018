import re


def parse_input():
    input_list = []

    for line in open('input.txt'):
        x, y, vx, vy = map(int, re.findall('-?\d+', line))
        input_list.append([x, y, vx, vy])

    return input_list


def print_stars(input_list):
    for t in range(100000):
        min_x = min([x for x, y, _, _ in input_list])
        max_x = max([x for x, y, _, _ in input_list])
        min_y = min([y for x, y, _, _ in input_list])
        max_y = max([y for x, y, _, _ in input_list])

        W = 100

        if min_x + W >= max_x and min_y + W >= max_y:
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x+1):
                    if (x, y) in [(px, py) for px, py, _, _ in input_list]:
                        print('#', end='')
                    else:
                        print('.', end='')
                print('')

            print(f'{t}')

        for p in input_list:
            p[0] += p[2]
            p[1] += p[3]


if __name__ == '__main__':
    input_list = parse_input()
    print_stars(input_list)
