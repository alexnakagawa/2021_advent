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


# basin = set()
# def get_low_point_basins(matrix: np.array, rows: int, cols: int) -> int:
#     low_points_basins = []
#     for y in range(rows):
#         for x in range(cols):
#             val = matrix[y][x]
#             if is_low_point(val, matrix, x, y, rows, cols):
#                 size_of_basin = 1

if __name__ == "__main__":
    matrix, rows, cols = get_matrix_from_txt("./input.txt")
    low_point_risk = get_low_point_risk(matrix, rows, cols)
    print(f"{low_point_risk} risk")
