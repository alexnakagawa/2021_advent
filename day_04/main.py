import numpy as np

def get_matrices_from_txt(filepath: str) -> list:
    drawn = []
    matrices = []
    num_lines = 0
    with open(filepath) as f:
        text = f.readlines()
        num_lines = len(text)

    with open(filepath) as f:
        matrix = []
        for idx, line in enumerate(f):
            if idx == 0:
                drawn = list(map(int, line.replace("\n", "").split(",")))
                continue

            if idx > 1 and ((idx-1) % 6 == 0):
                matrices.append(np.array(matrix))
                matrix = []
                continue

            if idx >= 2:
                matrix.append(np.array(list(map(int, line.replace("\n", "").split()))))

            if (idx+1) == num_lines:
                matrices.append(np.array(matrix))

    num_drawn = len(drawn)
    num_matrices = len(matrices)
    print(f"There were {num_drawn} numbers drawn")
    print(f"There are {num_matrices} matrices in the input")

    return drawn, matrices


def is_bingo(matrix):
    for i in range(5):
        row_remain = np.count_nonzero(matrix[i:,] != -1)
        col_remain = np.count_nonzero(matrix[:,i] != -1)
        if not row_remain or not col_remain:
            print("BINGO!")
            return True
    return False


def get_winning_board_and_number(drawn, matrices, is_first=True):
    boards_remaining = set(np.arange(len(matrices)))
    for i, d in enumerate(drawn):
        for idx in range(len(matrices)):
            # check for drawn d
            m = matrices[idx]
            matrices[idx] = np.where(m == d, -1, m)
            if is_bingo(matrices[idx]):
                boards_remaining.discard(idx)
                if is_first:
                    return matrices[idx], d
                else:
                    print(boards_remaining)
                    if len(boards_remaining) == 1:
                        for j in range(i+1, len(drawn)):
                            cur_drawn = drawn[j]
                            m = matrices[idx]
                            matrices[idx] = np.where(m == cur_drawn, -1, m)
                            if is_bingo(matrices[idx]):
                                return matrices[idx], cur_drawn
        
    return "No board found"


def get_final_score(board, num):
    remain = np.where(board == -1, 0, board)
    sum_remain = np.sum(remain)
    return sum_remain * num


if __name__ == "__main__":
    drawn, matrices = get_matrices_from_txt("./input.txt")
    win_board, win_number = get_winning_board_and_number(drawn, matrices)
    print(win_board)
    print(f"First win number: {win_number}")
    final_score = get_final_score(win_board, win_number)
    print(f"FIRST BINGO FINAL SCORE: {final_score}")
    last_win_board, last_win_number = get_winning_board_and_number(drawn, matrices, False)
    print(last_win_board)
    print(f"Last win number: {last_win_number}")
    last_final_score = get_final_score(last_win_board, last_win_number)
    print(f"LAST FINAL SCORE: {last_final_score}")
