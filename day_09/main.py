import numpy as np


def get_matrix_from_txt(filepath: str) -> list:
    matrix = []
    with open(filepath) as f:
        for line in f:
            matrix.append([int(i) for i in line.replace("\n", "")])

    matrix = np.array([np.array(i) for i in matrix])
    rows = len(matrix)
    cols = len(matrix[0])

    return matrix, rows, cols


def is_low_point(val: int, matrix: np.array, x: int, y: int, rows: int, cols: int):
    idx = []
    if x > 0:
        idx.append((x - 1, y))
    if y > 0:
        idx.append((x, y - 1))
    if x + 1 < cols:
        idx.append((x + 1, y))
    if y + 1 < rows:
        idx.append((x, y + 1))

    adj_vals = [matrix[k][j] for j, k in idx]
    below_val = adj_vals > val

    return np.all(below_val)


def get_low_point_risk(matrix: np.array, rows: int, cols: int) -> int:
    low_points = []
    val = None
    for y in range(rows):
        for x in range(cols):
            val = matrix[y][x]
            if is_low_point(val, matrix, x, y, rows, cols):
                low_points.append(val)

    return sum(low_points) + (len(low_points))


def get_adjacent_indices(x, y, rows, cols):
    idx = []
    if x > 0:
        idx.append((x - 1, y))
    if y > 0:
        idx.append((x, y - 1))
    if x + 1 < cols:
        idx.append((x + 1, y))
    if y + 1 < rows:
        idx.append((x, y + 1))
    return idx


def get_basin_size_product(matrix: np.array, rows: int, cols: int) -> int:
    basin_sizes = []
    for y in range(rows):
        for x in range(cols):
            basin_size = 0
            to_visit = [(x, y)]
            visited = []

            while len(to_visit) > 0:
                cur_x = to_visit[0][0]
                cur_y = to_visit[0][1]
                if matrix[cur_y][cur_x] != 9 and (to_visit[0] not in visited):
                    basin_size += 1
                    visited.append(to_visit[0])
                    adjacent_indices = get_adjacent_indices(cur_x, cur_y, rows, cols)
                    to_visit.extend(adjacent_indices)

                to_visit.pop(0)

            for i in visited:
                matrix[i[1]][i[0]] = 9

            if basin_size > 0:
                basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)

    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    matrix, rows, cols = get_matrix_from_txt("./input.txt")
    low_point_risk = get_low_point_risk(matrix, rows, cols)
    print(f"{low_point_risk} risk")
    basin_size_product = get_basin_size_product(matrix, rows, cols)
    print(f"Basin size product: {basin_size_product}")
