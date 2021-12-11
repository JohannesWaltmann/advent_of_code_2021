test_data = [str(x).strip() for x in open('resources/test', 'r').readlines()]
val_data = [str(x).strip() for x in open('resources/val', 'r').readlines()]

points_per_char_illegal = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

points_per_char_incomplete = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

parenthesis_map = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}


def compute_error_score(data) -> int:
    """
    TODO: Add commentary

    :param data:
    :return:
    """
    total_points = 0
    opened_parenthesis_ordered = list()
    for line in data:
        for char in line:
            if char in ['(', '{', '<', '[']:
                opened_parenthesis_ordered.append(char)
            if char in [')', ']', '>', '}']:
                if opened_parenthesis_ordered.pop(-1) != parenthesis_map[char]:
                    total_points += points_per_char_illegal[char]
                    break

    return total_points


def compute_incomplete_lines(data) -> int:
    """
    TODO: Add commentary

    :param data:
    :return:
    """
    closing_parenthesis_ordered = list()
    total_points = []
    for line in data:
        opened_parenthesis_ordered = list()
        for char in line:
            if char in ['(', '{', '<', '[']:
                opened_parenthesis_ordered.append(char)
            if char in [')', ']', '>', '}']:
                if opened_parenthesis_ordered.pop(-1) != parenthesis_map[char]:
                    opened_parenthesis_ordered = list()
                    break

        if len(opened_parenthesis_ordered) != 0:
            closing_parenthesis_ordered = ([parenthesis_map[key] for key in opened_parenthesis_ordered])
            closing_parenthesis_ordered.reverse()

            points = 0
            for parenthesis in closing_parenthesis_ordered:
                points *= 5
                points += points_per_char_incomplete[parenthesis]
            total_points.append(points)

    return sorted(total_points)[len(total_points)//2]


print(compute_error_score(test_data))
print(compute_error_score(val_data))

print(compute_incomplete_lines(test_data))
print(compute_incomplete_lines(val_data))
