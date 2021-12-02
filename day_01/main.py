def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [int(line) for line in f]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_three_sliding_window_sums(depths: list, window_size:int=3) -> list:
    num_depths = len(depths)
    if num_depths < window_size:
        return []

    ret_sums = list()
    for i in range(num_depths - window_size + 1):
        ret_sums.append(sum(depths[i:i+window_size]))

    return ret_sums


def get_num_increases(lst_depths: list) -> int:
    num_depths = len(lst_depths)
    if num_depths == 0 or num_depths == 1:
        return 0

    ctx = 0
    for i in range(num_depths - 1):
        ctx += (1 if lst_depths[i] < lst_depths[i+1] else 0)

    return ctx


if __name__ == "__main__":
    depths = get_arr_from_txt("./input.txt")
    increases = get_num_increases(depths)
    print(f"There are {increases} increases in depth in the input")
    sliding_window_sums = get_three_sliding_window_sums(depths)
    window_increases = get_num_increases(sliding_window_sums)
    print(f"There are {window_increases} sliding window increases")
