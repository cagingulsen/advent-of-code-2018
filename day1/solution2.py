import sys
import os


def parse_input(file_name):
    inputs = []

    with open(os.path.join(sys.path[0], file_name)) as f:
        for line in f:
            try:
                num = int(line)
                inputs.append(num)
            except ValueError:
                print('{} is not a number!'.format(line))

    return inputs


input_list = parse_input(sys.argv[1])

sum = 0
frequencies = set()

while True:
    for line in input_list:
        frequencies.add(sum)
        sum += line

        if sum in frequencies:
            print(sum)
            exit()
