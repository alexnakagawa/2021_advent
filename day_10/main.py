from math import floor

OPEN_CHAR_MAP = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

def get_strs_from_txt(filepath: str) -> list:
    lines = []
    with open(filepath) as f:
        for line in f:
            lines.append(line.replace("\n", ""))

    print(f"Number of lines: {len(lines)}")

    return lines


def get_syntax_error_score(lines: list) -> int:
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    scores = []
    for line in lines:
        opened_stack = []
        for char in line:
            if char in OPEN_CHAR_MAP:
                opened_stack.append(char)
            else:
                to_close = opened_stack.pop()
                if char != OPEN_CHAR_MAP[to_close]:
                    scores.append(points[char])
        if len(opened_stack) > 0:
            continue # line is incomplete

    return sum(scores)


def get_middle_autocomplete_score(lines: list) -> int:
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []
    for line in lines:
        opened_stack = []
        is_valid = True
        for char in line:
            if char in OPEN_CHAR_MAP:
                opened_stack.append(char)
            else:
                to_close = opened_stack[-1]
                if char != OPEN_CHAR_MAP[to_close]:
                    is_valid = False
                    break
                else:
                    opened_stack.pop()

        if is_valid and opened_stack:
            line_score = 0
            closed_stack = [OPEN_CHAR_MAP[o] for o in opened_stack[::-1]]
            for close_char in closed_stack:
                line_score = line_score * 5 + points[close_char]
            scores.append(line_score)

    scores.sort()
    return scores[floor(len(scores)/2)]


if __name__ == "__main__":
    lines = get_strs_from_txt("./input.txt")
    syntax_error_score = get_syntax_error_score(lines)
    print(f"Syntax Error Score: {syntax_error_score}")
    middle_score = get_middle_autocomplete_score(lines)
    print(f"Middle Autocomplete Score: {middle_score}")
