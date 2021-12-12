def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [int(v) for v in f.read().strip().split(",")]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_num_fishes(fishes: list, num_days: int):
    age_counts = [0] * 9

    # Each idx represents number of fishes at that index
    for age in fishes:
        age_counts[int(age)] += 1

    for _ in range(num_days):
        # Zeroes become sixes
        zeroes = age_counts.pop(0)
        age_counts[6] += zeroes
        # New ones become eights
        age_counts.append(zeroes)

    return sum(age_counts)


if __name__ == "__main__":
    fishes = get_arr_from_txt("./input.txt")
    num_fishes_after_80_days = get_num_fishes(fishes, num_days=80)
    print(f"{num_fishes_after_80_days} fishes now exist after 80 days.")
    num_fishes_after_256_days = get_num_fishes(fishes, num_days=256)
    print(f"{num_fishes_after_256_days} fishes now exist after 256 days.")
