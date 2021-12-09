test_input = [str(x).strip() for x in open('resources/test_input').readlines()]
val_input = [str(x).strip() for x in open('resources/val_input').readlines()]


def calc_position(input_data):
    _depth, _horizontal = 0, 0

    for elem in input_data:
        if elem[:-2] == 'forward':
            _horizontal += int(elem[-1])
        elif elem[:-2] == 'up':
            _depth -= int(elem[-1])
        elif elem[:-2] == 'down':
            _depth += int(elem[-1])

    return _horizontal * _depth


def calc_position_aimed(input_data):
    _aim, _depth, _horizontal = 0, 0, 0

    for elem in input_data:
        if elem[:-2] == 'forward':
            _horizontal += int(elem[-1])
            _depth += (_aim * int(elem[-1]))
        elif elem[:-2] == 'up':
            _aim -= int(elem[-1])
        elif elem[:-2] == 'down':
            _aim += int(elem[-1])

    return _horizontal * _depth


""" Output testing. """
print(f'Test part 1: {calc_position(test_input)}')
print(f'Test part 2: {calc_position_aimed(test_input)}')

""" Output validation. """
print(f'Output part 1: {calc_position(val_input)}')
print(f'Output part 2: {calc_position_aimed(val_input)}')
