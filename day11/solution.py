def generate_grid(serial, grid_size):
    grid = []

    for x in range(0, grid_size):
        row = []
        for y in range(0, grid_size):
            # print(f'{x} {y}')
            rack_id = x + 11
            power_level = rack_id * (rack_id * (y + 1) + serial)
            # print(power_level)

            hundreds_digit = 0
            if len(str(power_level)) > 2:
                hundreds_digit = int(str(power_level)[-3])

            row.append(hundreds_digit - 5)

        grid.append(row)

    return grid


def find_max_power(grid, s):
    max_power = float('-inf')
    coordinates = (0, 0)

    for i in range(0, len(grid) - s + 1):
        for j in range(0, len(grid) - s + 1):
            total_power = sum(grid[i_][j_] for i_ in range(i, i+s) for j_ in range(j, j+s))

            if total_power > max_power:
                max_power = total_power
                coordinates = (i+1, j+1)

    return max_power, coordinates


def find_max_power_all(grid):
    # csum[(x, y)] is the cumulative sum of d[i][j] for all i <= x and j <= y
    csum = {}
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            csum[(i, j)] = grid[i][j] + csum.get((i - 1, j), 0) + csum.get((i, j - 1), 0) - csum.get((i - 1, j - 1), 0)

    max_power = float('-inf')
    solution = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            for s in range(0, len(grid) - max(i, j)):
                # After submitting that these indices should all be one smaller since the bounds of the square are
                # i <= x < i + s, j <= y < j + s
                local_power = csum[(i + s, j + s)] + csum[(i, j)] - csum[(i + s, j)] - csum[(i, j + s)]
                if local_power > max_power:
                    max_power = local_power
                    solution = (i+2, j+2, s)

    return max_power, solution


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        data = int(f.read())

    grid = generate_grid(data, 300)

    _, coordinates1 = find_max_power(grid, 3)
    print(coordinates1)

    _, coordinates2 = find_max_power_all(grid)
    print(coordinates2)
