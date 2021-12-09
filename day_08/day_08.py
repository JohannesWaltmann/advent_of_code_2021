# --- Day 8: Seven Segment Search ---

test_input = [[num.strip().split(' ') for num in line.split('|')]
              for line in open('resources/test_input', 'r').readlines()]

val_input = [[num.strip().split(' ') for num in line.split('|')]
             for line in open('resources/val_input', 'r').readlines()]

print(test_input)


def find_digit_in_segments(display: list) -> int:
    num_digits = 0
    for digit in display:
        for segment in digit[1]:
            if len(segment) == 2 or len(segment) == 3 or len(segment) == 4 or len(segment) == 7:
                num_digits += 1
    return num_digits


print(f'Solution test task 01: {find_digit_in_segments(test_input)}')
print(f'Solution validation task 01: {find_digit_in_segments(val_input)}')
