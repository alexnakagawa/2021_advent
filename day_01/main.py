def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [int(line) for line in f]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_num_increases(depths: list) -> int:
    num_depths = len(depths)
    if num_depths == 0 or num_depths == 1:
        return 0

    ctx = 0
    for i in range(num_depths - 1):
        ctx += (1 if depths[i] < depths[i+1] else 0)

    return ctx


if __name__ == "__main__":
    increases = get_num_increases("./input.txt")
    print(f"There are {increases} increases in depth in the input")
