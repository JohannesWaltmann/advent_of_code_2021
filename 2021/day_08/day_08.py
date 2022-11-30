# --- Day 8: Seven Segment Search ---
# Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:
# So, to render a 1, only segments c and f would be turned on; the rest would be off.
# To render a 7, only segments a, c, and f would be turned on.
#
# For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see,
# and then write down a single four digit output value (your puzzle input).
# Using the signal patterns, you should be able to work out which pattern corresponds to which digit.
# Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value.
# Because the digits 1, 4, 7, and 8 each use a unique number of segments,
# you should be able to tell which combinations of signals correspond to those digits.
#
# --- Part 1 ---
# In the output values, how many times do digits 1, 4, 7, or 8 appear?


test_input = [[num.strip().split(" ") for num in line.split("|")]
              for line in open('resources/test_input', 'r').readlines()]
test_input_2 = [[num.strip().split(" ") for num in line.split("|")]
                for line in open('resources/test_input_2', 'r').readlines()]
val_input = [[num.strip().split(' ') for num in line.split('|')]
             for line in open('resources/val_input', 'r').readlines()]

print(test_input[0])


def find_digit_in_segments(display) -> int:
    """
    Computes how many instances of a specific digit are located in the given input.

    :param display: The input of a seven segment split at '|' as delimiter.
    :return: Sum of the counted digits.
    """
    num_digits = 0
    # Check each row of the segment display
    for digit in display:
        # Check each single segment
        for segment in digit[1]:
            # Increment the output if the number read is either of [1, 4, 7, 8]
            if len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7:
                num_digits += 1
    return num_digits


def compute_sum_output(display) -> int:
    """
    Computes the digit representation for the output of every line and returns the sum of these outputs.
    Needs to determine the character->digit mapping new for each single line.

    :param display: Line wise input of the seven segment. Split at '|' as delimiter.
    :return: Sum of the output numbers per line.
    """
    sum_output = 0

    # Filter the obvious numbers from the display input
    for digit in display:
        known = {}
        for segment in digit[0]:
            if len(segment) == 2:
                known[1] = set(segment)
            elif len(segment) == 4:
                known[4] = set(segment)

        # Filter the numbers from the output
        nums = ''
        for _segment in digit[1]:
            if len(_segment) == 2:
                nums += '1'
            elif len(_segment) == 3:
                nums += '7'
            elif len(_segment) == 4:
                nums += '4'
            elif len(_segment) == 5:
                if set(_segment).issuperset(known[1]):
                    nums += '3'
                elif len(set(_segment) & known[4]) == 3:
                    nums += '5'
                else:
                    nums += '2'
            elif len(_segment) == 6:
                if not set(_segment).issuperset(known[1]):
                    nums += '6'
                elif set(_segment).issuperset(known[4]):
                    nums += '9'
                else:
                    nums += '0'
            elif len(_segment) == 7:
                nums += '8'

        sum_output += int(nums)

    return sum_output


print(f'Solution test task 01: {find_digit_in_segments(test_input)}')
print(f'Solution test 02 task 01: {find_digit_in_segments(test_input_2)}')
print(f'Solution validation task 01: {find_digit_in_segments(val_input)}')
print('----------------------------')
print(f'Solution test task 02: {compute_sum_output(test_input)}')
print(f'Solution test 2 task 02: {compute_sum_output(test_input_2)}')
print(f'Solution validation task 02: {compute_sum_output(val_input)}')
