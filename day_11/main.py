from copy import copy


def get_matrix_from_txt(filepath: str) -> list:
    matrix = []
    with open(filepath) as f:
        for line in f:
            row = [int(i) for i in line.replace("\n", "")]
            matrix.append(row)

    print(f"Number of rows: {len(matrix)}")
    print(f"Number of cols: {len(matrix[0])}")

    return matrix


def get_number_of_flashes(matrix):
    queue = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] += 1
            if matrix[r][c] > 9:
                queue.append((r, c))

    flashed = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) in flashed:
            continue
        flashed.add((r, c))
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                r_adj = r + dr
                c_adj = c + dc
                if r_adj < 0 or r_adj >= len(matrix):
                    continue
                if c_adj < 0 or c_adj >= len(matrix[0]):
                    continue
                matrix[r_adj][c_adj] += 1
                if matrix[r_adj][c_adj] > 9:
                    queue.append((r_adj, c_adj))
    for f in flashed:
        r, c = f
        matrix[r][c] = 0
    return len(flashed)


def get_number_of_total_flashes(matrix: list) -> int:
    cur_matrix = copy(matrix)

    i = 0
    cur_flashes = 0
    for _ in range(100):
        cur_flashes += get_number_of_flashes(cur_matrix)

    return cur_flashes


def get_first_step_all_flash(matrix: list) -> int:
    cur_matrix = copy(matrix)

    i = 0
    while True:
        i += 1
        num_flashes = get_number_of_flashes(cur_matrix)
        if num_flashes == 100:
            break

    return i


if __name__ == "__main__":
    matrix = get_matrix_from_txt("./input.txt")
    total_flashes = get_number_of_total_flashes(matrix)
    print(f"Total number of flashes: {total_flashes}")
    all_flash_time = get_first_step_all_flash(matrix)
    print(f"All flash at step: {all_flash_time}")
