import re


class Claim():
    def __init__(self, claim_str):
        claim_str = claim_str.replace(" ", "")
        self.id = int(re.search('#(.*)@', claim_str).group(1))
        self.column = int(re.search('@(.*),', claim_str).group(1))
        self.row = int(re.search(',(.*):', claim_str).group(1))
        self.width = int(re.search(':(.*)x', claim_str).group(1))
        self.height = int(re.search('x(.*)', claim_str).group(1))


def read_claims():
    with open('input.txt') as f:
        claims = []

        for line in f:
            new_claim = Claim(line)
            claims.append(new_claim)

        return claims


def prepare_matrix(claims):
    max_dimension = get_max_dimension(claims)

    matrix = [[0] * max_dimension for _ in range(max_dimension)]

    fill_matrix(matrix, claims)

    return matrix


def get_max_dimension(claims):
    max_dimension = 0

    for claim in claims:
        if claim.column + claim.width > max_dimension:
            max_dimension = claim.column + claim.width
        if claim.row + claim.height > max_dimension:
            max_dimension = claim.row + claim.height

    return max_dimension


def fill_matrix(matrix, claims):
    for claim in claims:
        for i in range(claim.row, claim.row + claim.height):
            for j in range(claim.column, claim.column + claim.width):
                matrix[i][j] += 1


def count_overlapping_squares(matrix):
    count = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] > 1:
                count += 1

    return count


def check_if_claim_overlap(matrix, claim):
    for i in range(claim.row, claim.row + claim.height):
        for j in range(claim.column, claim.column + claim.width):
            if matrix[i][j] != 1:
                return True

    return False


def find_non_overlapping_claim(matrix, claims):
    for claim in claims:
        if not check_if_claim_overlap(matrix, claim):
            return claim


if __name__ == '__main__':
    claims = read_claims()
    matrix = prepare_matrix(claims)

    print(count_overlapping_squares(matrix))
    print(find_non_overlapping_claim(matrix, claims).id)
