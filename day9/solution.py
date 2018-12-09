from collections import deque, defaultdict


def play_game(file_name):
    player_count = -1
    last_marble = -1

    with open(file_name) as f:
        for line in f:
            words = line.split(' ')
            player_count = int(words[0])
            last_marble = int(words[6])

    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % player_count] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0


if __name__ == '__main__':
    print(play_game('input1.txt'))
    print(play_game('input2.txt'))
