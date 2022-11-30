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
    Takes a multi line string of different parenthesis and computes a sum dependant
    of the number of corrupt lines in the string.
    A corrupt line is a line where an opened parenthesis is closed using the wrong type of parenthesis.
    Each kind of parenthesis has another value which is added to the error score.

    :param data: String with a random ordering of opened and closed parenthesis.
    :return: The error score.
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
    Takes a multi line input and computes the sum for the missing closing parenthesis
    if the current line is not a corrupted line.
    Each kind of parenthesis has a different value.

    For the sum the current number of points is multiplied by five
    before adding the next parenthesis value.

    :param data: String with a random ordering of opened and closed parenthesis.
    :return: The middle score out of all computed sums per line.
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


print('Task 01 test output: ', compute_error_score(test_data))
print('Task 01 val output: ', compute_error_score(val_data))

print('Task 02 test output: ', compute_incomplete_lines(test_data))
print('Task 02 val output: ', compute_incomplete_lines(val_data))
