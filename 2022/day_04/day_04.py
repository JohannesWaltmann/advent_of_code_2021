
test_path = '../resources/test/04.txt'
validation_path = '../resources/validation/04.txt'


def import_data(file_path):
    return [x.strip().split(',') for x in open(file_path, 'r').readlines()]


def task_01(file_path) -> int:
    cleaning_pairs = import_data(file_path)
    subset_pairs = 0

    for pair in cleaning_pairs:
        a, b = pair[0].split('-')
        c, d = pair[1].split('-')

        if int(a) >= int(c) and int(b) <= int(d):
            subset_pairs += 1
        elif int(c) >= int(a) and int(d) <= int(b):
            subset_pairs += 1

    return subset_pairs


def task_02(file_path) -> int:
    cleaning_pairs = import_data(file_path)
    total_overlaps = 0

    for pair in cleaning_pairs:
        a, b = pair[0].split('-')
        c, d = pair[1].split('-')

        if int(b) >= int(c) and int(d) >= int(a):
            total_overlaps += 1

    return total_overlaps


# Print solutions:
print(f'Task 01 testing: {task_01(test_path)}')
print(f'Task 01 validation: {task_01(validation_path)}')

print(f'Task 02 testing: {task_02(test_path)}')
print(f'Task 02 validation: {task_02(validation_path)}')
