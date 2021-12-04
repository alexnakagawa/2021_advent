def get_arr_from_txt(filepath: str) -> list:
    with open(filepath) as f:
        ret = [line.split() for line in f]

    num_records = len(ret)
    print(f"There are {num_records} records in the input")

    return ret


def get_distance_from_arr(directions: list) -> int:
    depth, horizontal = 0, 0
    for d in directions:
        direction, length = d[0], int(d[1])
        if direction == "forward":
            horizontal += length
            
        elif direction == "down":
            depth += length
        elif direction == "up":
            depth -= length
        else:
            continue
    result = depth * horizontal
    return result


def get_distance_by_aim(directions: list) -> int:
    depth, aim, horizontal = 0, 0, 0
    for d in directions:
        direction, length = d[0], int(d[1])
        if direction == "forward":
            horizontal += length
            depth += (aim * length)
        elif direction == "down":
            aim += length
        elif direction == "up":
            aim -= length
        else:
            continue
    result = depth * horizontal
    return result


if __name__ == "__main__":
    directions = get_arr_from_txt("./input.txt")
    result = get_distance_from_arr(directions)
    print(f"NO AIM Result: {result}")
    aim_result = get_distance_by_aim(directions)
    print(f"AIM Result: {aim_result}")
