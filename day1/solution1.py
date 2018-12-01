import sys

with open(sys.argv[1]) as f:
    sum = 0

    for line in f:
        try:
            num = int(line)
            sum += num
        except ValueError:
            print('{} is not a number!'.format(line))

    print(sum)
