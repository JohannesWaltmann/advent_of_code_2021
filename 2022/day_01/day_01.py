import numpy as np

with open('../resources/test/01.txt') as f:
    test_data = f.readlines()
with open('../resources/validation/01.txt') as f:
    val_data = f.readlines()


def task_01(input_data):
    calories_per_elf = []

    elven_weight = 0
    for value in input_data:
        # Add up calories
        if value != '\n':
            elven_weight += int(value)
        # Write to the list if a new line is found
        elif value == '\n':
            calories_per_elf.append(elven_weight)
            elven_weight = 0  # Reset the calorie counter

    return calories_per_elf


def task_02(input_data):
    # Add up the calories per elf
    cals_per_elf = task_01(input_data)

    # Sort all elves iteratively
    cals_per_elf = np.sort(cals_per_elf)

    # Add up the last three entries (max. values)
    added = cals_per_elf[-1] + cals_per_elf[-2] + cals_per_elf[-3]

    return added


print(f'test 01: {task_01(test_data)}')
print(f'val 01: {task_01(val_data)}')

print(f'test 02: {task_02(test_data)}')
print(f'val 02: {task_02(val_data)}')
