test_path = '../resources/test/02.txt'
validation_path = '../resources/validation/02.txt'

moves = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }

predictions = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }


def import_data(file_path):
    return [x.strip() for x in open(file_path).readlines()]


def task(file_path, given_moves) -> int:
    match_guide = import_data(file_path)

    scores = 0
    for game in match_guide:
        # Add up the possible result scores from the given_moves map
        scores += given_moves[game]

    return scores


print(f'Task 01 test: {task(test_path, moves)}')
print(f'Task 01 validation: {task(validation_path, moves)}')

print(f'Task 02 test: {task(test_path, predictions)}')
print(f'Task 02 validation: {task(validation_path, predictions)}')
