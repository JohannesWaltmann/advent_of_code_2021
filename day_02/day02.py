# --- Day 2: Dive! ---
#
# --- Part 1 ---
# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:
#
#   forward X increases the horizontal position by X units.
#   down X increases the depth by X units.
#   up X decreases the depth by X units.

# Note that since you're on a submarine, down and up affect your depth,
# and so they have the opposite result of what you might expect.
#
# --- Part 2 ---
# In addition to horizontal position and depth, you'll also need to track a third value
# aim, which also starts at 0. The commands also mean something entirely different than you first thought:
#
#     down X increases your aim by X units.
#     up X decreases your aim by X units.
#     forward X does two things:
#         It increases your horizontal position by X units.
#         It increases your depth by your aim multiplied by X.

test_input = [str(x).strip() for x in open('resources/test_input').readlines()]
val_input = [str(x).strip() for x in open('resources/val_input').readlines()]


def calc_position(input_data):
    """
    Computes the horizontal and depth position based on a set of different input commands.

    :param input_data: String array of different movement commands
    :return: The position based on the multiplication of the horizontal and vertical position
    """
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
    """
    Computes the horizontal and depth position based on a set of different input commands.
    Uses the aim to compute the depth position instead of using 'up' and 'down' commands directly.

    :param input_data: String array of different movement commands
    :return: The position based on the multiplication of the horizontal and vertical position
    """
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
