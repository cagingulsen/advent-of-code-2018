from collections import Counter


def parse_input():
    inputs = []

    with open('input.txt') as f:
        for line in f:
            inputs.append(line)

    return inputs


def find_two_three_letter_counts(input_list):
    three_letter_count = 0
    two_letter_count = 0

    for line in input_list:
        occurrences = Counter(line).most_common()

        three_flag = 0
        two_flag = 0

        for (key, value) in occurrences:
            if value == 3 and three_flag != 1:
                three_letter_count += 1
                three_flag = 1
            elif value == 2 and two_flag != 1:
                two_letter_count += 1
                two_flag = 1
            elif value < 2:
                continue

    return two_letter_count * three_letter_count


def count_different_characters(str1, str2):
    count = 0
    common_str = ''

    for i, c in enumerate(str1):
        if str1[i] != str2[i]:
            count += 1
        else:
            common_str += str1[i]

    return count, common_str


def get_common_letters(input_list):
    for i, line1 in enumerate(input_list):
        for j, line2 in enumerate(input_list):
            # will not iterate same string couples
            if j >= i:
                break

            diff_count, commons = count_different_characters(line1, line2)

            if diff_count == 1:
                return commons


if __name__ == '__main__':
    input_list = parse_input()

    print(find_two_three_letter_counts(input_list))
    print(get_common_letters(input_list))
