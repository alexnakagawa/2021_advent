from collections import defaultdict


def get_lines_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [
            [list(map(int, i[0].split(","))), list(map(int, i[1].split(",")))]
            for i in [line.replace("\n", "").split(" -> ") for line in f]
        ]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_overlap_from_lines(lines, only_straight=True):
    map_points = defaultdict(int)

    points = []
    for line in lines:
        x_1, y_1, x_2, y_2 = [coords for sublist in line for coords in sublist]
        x_delta, y_delta = (x_1 - x_2), (y_1 - y_2)
        if y_delta == 0:
            points = (
                [(i, y_2) for i in range(x_1, x_2 + 1)]
                if x_delta < 0
                else [(i, y_2) for i in range(x_2, x_1 + 1)]
            )
        elif x_delta == 0:
            points = (
                [(x_1, r) for r in range(y_2, y_1 + 1)]
                if y_delta >= 0
                else [(x_1, r) for r in range(y_1, y_2 + 1)]
            )
        if only_straight is False:
            if abs(x_delta) == abs(y_delta):
                if x_delta == y_delta:
                    points = (
                        zip(range(x_1, x_2 + 1), range(y_1, y_2 + 1))
                        if x_delta < 0
                        else zip(range(x_2, x_1 + 1), range(y_2, y_1 + 1))
                    )
                else:
                    points = (
                        zip(range(x_1, x_2 + 1), range(y_1, y_2 - 1, -1))
                        if x_delta < 0
                        else zip(range(x_1, x_2 - 1, -1), range(y_1, y_2 + 1))
                    )

        for i in points:
            map_points[i] += 1

        points = []

    map_points = dict(map_points)

    return sum(list(map(lambda x: x >= 2, map_points.values())))


if __name__ == "__main__":
    lines = get_lines_from_txt("./input.txt")
    straight_overlaps = get_overlap_from_lines(lines, only_straight=True)
    print(f"Total overlaps from straight lines: {straight_overlaps}")
    all_overlaps = get_overlap_from_lines(lines, only_straight=False)
    print(f"Total overlaps from straight and diagonal lines: {all_overlaps}")
