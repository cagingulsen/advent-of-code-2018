import sys
from collections import Counter


with open(sys.argv[1]) as f:
    three_letter_count = 0
    two_letter_count = 0

    for line in f:
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

    print(two_letter_count * three_letter_count)
