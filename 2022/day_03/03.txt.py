test_path = '../resources/test/03.txt'
validation_path = '../resources/validation/03.txt'


def import_data(file_path):
    return [x.strip() for x in open(file_path)]


def task_01(file_path) -> int:
    rucksacks = import_data(file_path)
    multi_rucksack_entries = []
    priority_sum = 0

    for rucksack in rucksacks:
        # Split rucksack contents in two and order them as a set
        first_compartment = set(rucksack[:len(rucksack) // 2])
        second_compartment = set(rucksack[len(rucksack) // 2:])

        for char in first_compartment:
            # Check if any item is contained in both rucksack compartments
            if second_compartment.__contains__(char):
                multi_rucksack_entries.append(char)

    # Add up the unique sum
    for entry in multi_rucksack_entries:
        if entry.isupper():
            # Uppercase Letters have values in the range of 27 to 52
            priority_sum += (ord(entry) - ord('A') + 27)
        elif entry.islower():
            # Lowercase Letters have values in the range of 1 to 26
            priority_sum += (ord(entry) - ord('a') + 1)

    return priority_sum


def task_02(file_path) -> int:
    rucksacks = import_data(file_path)
    priority_sum = 0

    # Iterate over the number of rucksacks in batches of three
    for rucksack in [rucksacks[n:n+3] for n in range(0, len(rucksacks), 3)]:
        # Save each rucksack of one batch into a set
        first_elf = set(rucksack[0])
        second_elf = set(rucksack[1])
        third_elf = set(rucksack[2])

        # Check which character is found in each of the three rucksacks
        for character in first_elf:
            if second_elf.__contains__(character) and third_elf.__contains__(character):
                # Add up the found letters priority value
                if character.isupper():
                    # Uppercase Letters have values in the range of 27 to 52
                    priority_sum += (ord(character) - ord('A') + 27)
                elif character.islower():
                    # Lowercase Letters have values in the range of 1 to 26
                    priority_sum += (ord(character) - ord('a') + 1)

    return priority_sum


# Print solutions:
print(f'Task 01 test: {task_01(test_path)}')
print(f'Task 01 validation: {task_01(validation_path)}')

print(f'Task 02 test: {task_02(test_path)}')
print(f'Task 02 validation: {task_02(validation_path)}')
