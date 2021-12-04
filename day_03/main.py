import collections


def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [list(map(int, line.replace("\n", ""))) for line in f]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_strs_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [line.replace("\n", "") for line in f]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_bit(a: set, num_records: int, is_gamma: bool) -> str:
    if is_gamma:
        return "1" if sum(a) >= (num_records / 2) else "0"
    return "0" if sum(a) > (num_records / 2) else "1"


def get_gamma_epsilon_rate(array: list) -> int:
    num_records = len(array)
    transposed_arr = list(zip(*array))

    gamma_lst = [get_bit(a, num_records, is_gamma=True) for a in transposed_arr]
    gamma = int("".join(list(gamma_lst)), base=2)

    epsilon_lst = [get_bit(a, num_records, is_gamma=False) for a in transposed_arr]
    epsilon = int("".join(list(epsilon_lst)), base=2)

    return gamma * epsilon


def get_life_support_rating(strs: list) -> int:
    def _reduce_list(remaining: list, bit: str, idx: int):
        if len(remaining) == 1:
            return remaining
        reduced = [r for r in remaining if str(r[idx]) == bit]
        return reduced

    remaining_oxygen = strs[::]
    remaining_co2 = strs[::]
    for idx in range(len(strs[0])):
        ct_most = collections.Counter([r[idx] for r in remaining_oxygen])
        oxy_bit = "1" if ct_most["1"] >= ct_most["0"] else "0"
        remaining_oxygen = list(filter(lambda x: x[idx] == oxy_bit, remaining_oxygen))
        if len(remaining_oxygen) == 1:
            break
    for idx in range(len(strs[0])):
        ct_least = collections.Counter([r[idx] for r in remaining_co2])
        co2_bit = "0" if ct_least["1"] >= ct_least["0"] else "1"
        remaining_co2 = list(filter(lambda x: x[idx] == co2_bit, remaining_co2))
        if len(remaining_co2) == 1:
            break

    oxygen_rating = int(remaining_oxygen[0], 2)
    co2_rating = int(remaining_co2[0], 2)

    return oxygen_rating * co2_rating


if __name__ == "__main__":
    array = get_arr_from_txt("./input.txt")
    power_consumption = get_gamma_epsilon_rate(array)
    print(f"Power consumption: {power_consumption}")

    strs = get_strs_from_txt("./input.txt")
    life_support = get_life_support_rating(strs)
    print(f"Life Support Rating: {life_support}")
