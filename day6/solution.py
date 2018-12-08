def get_map_dimension(coordinates):
    return max(max(coordinates, key=lambda item: max(item[0], item[1]))) + 1


def calculate_manhattan_distance(i, j, k, l):
    distance = abs(i - k) + abs(j - l)
    return distance


def search_map(dimension, coordinates, inner_region_limit):
    inner_region_count = 0
    for i in range(dimension):
        for j in range(dimension):
            min_distance = float('inf')
            min_coord = ''
            min_multiple = False
            sum = 0

            for coord in coordinates:
                manhattan_distance = calculate_manhattan_distance(i, j, coord[1], coord[0])
                if manhattan_distance < min_distance:
                    min_distance = manhattan_distance
                    min_multiple = False
                    min_coord = coord
                elif manhattan_distance == min_distance:
                    min_multiple = True

                sum += manhattan_distance

            if sum < inner_region_limit:
                inner_region_count += 1

            if not min_multiple:
                if min_coord[2] >= 0 and (i == 0 or j == 0 or i == dimension-1 or j == dimension-1):
                    min_coord[2] = -1
                if min_coord[2] >= 0:
                    min_coord[2] += 1

    print(max(coordinates, key=lambda item: item[2])[2])
    print(inner_region_count)


if __name__ == '__main__':
    coordinates = []

    with open('input.txt') as f:
        for index, line in enumerate(f):
            a, b = line.replace(' ', '').rstrip().split(',')
            coordinates.append([int(a), int(b), 0])

    dimension = get_map_dimension(coordinates)
    search_map(dimension, coordinates, 10000)
