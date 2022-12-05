test_path = '../resources/test/05.txt'
validation_path = '../resources/validation/05.txt'


def import_data(file_path):
    with open(file_path) as f:
        data = f.read()
    # Split read content into the stacks and instructions
    stacks_content, instructions = [part.split('\n') for part in data.split('\n\n')]

    # Order up the stacks and remove their enumeration
    # An extra empty leading stack is added to process the instructions easier
    stacks = [''] * (int(stacks_content[-1][-1]) + 1)
    for line in stacks_content[:-1]:
        for i, box in enumerate(line[1::4]):
            if box != ' ':
                stacks[i + 1] += box

    return stacks, instructions


def split_instructions_to_int(instruction):
    # Takes one instruction line and extracts the amount to move and the source and destination stacks
    _, amount, _, source, _, destination = instruction.split()
    amount = int(amount)
    source = int(source)
    destination = int(destination)

    return amount, source, destination


def task_01(file_path) -> str:
    # Get stacks and instructions
    stacks, instructions = import_data(file_path)
    topmost_items = ''

    for instruction in instructions:
        # Get the Instruction Values and cast them to integers
        amount, source, destination = split_instructions_to_int(instruction)

        for i in range(amount):
            # Move the amount of elements form the source to the destination stack
            current_element = stacks[source][0]
            stacks[source] = stacks[source][1:]
            current_destination_value = stacks[destination]
            stacks[destination] = (current_element + current_destination_value)

    for item in stacks:
        # Adds the topmost element of each stack to the output, skipping the empty leading stack
        if item != '':
            topmost_items += item[0]

    return topmost_items


def task_02(file_path) -> str:
    # Get stacks and instructions
    stacks, instructions = import_data(file_path)
    topmost_items = ''

    for instruction in instructions:
        # Get the Instruction Values and cast them to integers
        amount, source, destination = split_instructions_to_int(instruction)

        if amount == 0:
            # Behaves as in task_01 if only one element is moved
            current_elements = stacks[source][0]
            stacks[source] = stacks[source][1:]
            current_destination = stacks[destination]
            stacks[destination] = (current_elements + current_destination)

        elif amount > 0:
            # Moves all elements at once if more than one element are to be moved
            current_elements = stacks[source][0:amount]
            stacks[source] = stacks[source][amount:]
            current_destination = stacks[destination]
            stacks[destination] = (current_elements + current_destination)

    for item in stacks:
        # Adds the topmost element of each stack to the output, skipping the empty leading stack
        if item != '':
            topmost_items += item[0]

    return topmost_items


# Print solutions:
print(f'Testing Task 01: {task_01(test_path)}')
print(f'Testing Task 01: {task_01(validation_path)}')
print('---')
print(f'Testing Task 02: {task_02(test_path)}')
print(f'Testing Task 02: {task_02(validation_path)}')
