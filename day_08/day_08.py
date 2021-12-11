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


def find_digit_in_segments(display) -> int:
    """
    Computes how many instances of a specific digit are located in the given input.

    :param display:
    :return:
    """
    num_digits = 0
    for digit in display:
        for segment in digit[1]:
            if len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7:
                num_digits += 1
    return num_digits


def compute_sum_output(display) -> int:

    sum_output = 0
    for digit in display:
        current_digit = ''
        len5_segments, len6_segments = [], []
        for segment in digit[1]:
            if len(segment) == 2:
                current_digit += '1'
            elif len(segment) == 3:
                current_digit += '7'
            elif len(segment) == 4:
                current_digit += '4'
            elif len(segment) == 5:
                len5_segments.append(segment)
            elif len(segment) == 6:
                len6_segments.append(segment)
            elif len(segment) == 7:
                current_digit += '8'

    return 0

def determine_len5_segments():


def determine_len6_segments():


print(f'Solution test task 01: {find_digit_in_segments(test_input)}')
print(f'Solution test 02 task 01: {find_digit_in_segments(test_input_2)}')
print(f'Solution validation task 01: {find_digit_in_segments(val_input)}')

print(f'Solution test task 02: {compute_sum_output(test_input)}')
#print(f'Solution test 2 task 02: {compute_sum_output(test_input_2)}')
#print(f'Solution validation task 02: {compute_sum_output(val_input)}')
