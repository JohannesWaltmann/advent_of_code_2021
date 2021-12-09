# --- Day 8: Seven Segment Search ---

test_input = [[num.strip().split(' ') for num in line.split('|')]
              for line in open('resources/test_input', 'r').readlines()]

val_input = [[num.strip().split(' ') for num in line.split('|')]
             for line in open('resources/val_input', 'r').readlines()]


def find_digit_in_segments(segments : list) -> int:

    return 0


print(f'Solution test task 01: {find_digit_in_segments(test_input)}')
print(f'Solution validation task 01: {find_digit_in_segments(val_input)}')
