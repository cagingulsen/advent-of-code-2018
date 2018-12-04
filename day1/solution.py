def find_sum():
    with open('input.txt') as f:
        sum = 0

        for line in f:
            sum += int(line)

        return sum


def parse_input():
    inputs = []

    with open('input.txt') as f:
        for line in f:
            num = int(line)
            inputs.append(num)

    return inputs


def find_twice_read_frequency():
    input_list = parse_input()

    sum = 0
    frequencies = set()

    while True:
        for line in input_list:
            frequencies.add(sum)
            sum += line

            if sum in frequencies:
                print(sum)
                exit()

    sum = 0

    for line in f:
        sum += int(line)

    return sum


if __name__ == '__main__':
    print(find_sum())
    print(find_twice_read_frequency())
