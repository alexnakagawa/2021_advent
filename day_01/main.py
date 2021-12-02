def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [int(line) for line in f]
    return ret


def get_num_decreases(filepath: str) -> int:
    depths = get_arr_from_txt(filepath)
    num_depths = len(depths)

    print(f"There are {num_depths} depths in the input")

    if num_depths == 0 or num_depths == 1:
        return 0

    ctx = 0
    for i in range(num_depths - 1):
        ctx += (1 if depths[i] < depths[i+1] else 0)

    return ctx


if __name__ == "__main__":
    decreases = get_num_decreases("./input.txt")
    print(f"There are {decreases} decreases in depth in the input")