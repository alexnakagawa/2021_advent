import numpy as np


def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = np.array([int(v) for v in f.read().strip().split(",")])

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_fuel_consumption_constant(crabs: np.ndarray) -> int:
    min_crab, max_crab = np.min(crabs), np.max(crabs)
    return np.min(
        [np.sum((np.abs(crabs - t))) for t in np.arange(min_crab, max_crab + 1)]
    )


def get_fuel_consumption_triangular(crabs: np.ndarray) -> int:
    min_crab, max_crab = np.min(crabs), np.max(crabs)
    triangulars = [
        np.floor_divide((np.abs(crabs - t) + 1) * (np.abs(crabs - t)), 2)
        for t in np.arange(min_crab, max_crab + 1)
    ]
    return np.min([np.sum(triangulars, axis=1)])


if __name__ == "__main__":
    crabs = get_arr_from_txt("./input.txt")
    constant_fuel = get_fuel_consumption_constant(crabs)
    print(f"{constant_fuel} used from constant burn")
    triangular_fuel = get_fuel_consumption_triangular(crabs)
    print(f"{triangular_fuel} used from triangular burn")
