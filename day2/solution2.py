import sys
import os


def parse_input(file_name):
    inputs = []

    with open(os.path.join(sys.path[0], file_name)) as f:
        for line in f:
            inputs.append(line)

    return inputs


def count_different_characters(str1, str2):
    count = 0
    common_str = ''

    for i, c in enumerate(str1):
        if str1[i] != str2[i]:
            count += 1
        else:
            common_str += str1[i]

    return count, common_str


input_list = parse_input(sys.argv[1])

for i, line1 in enumerate(input_list):
    for j, line2 in enumerate(input_list):
        # will not iterate same string couples
        if j >= i:
            break

        diff_count, commons = count_different_characters(line1, line2)

        if diff_count == 1:
            print(commons)
