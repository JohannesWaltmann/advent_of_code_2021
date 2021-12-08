
test_input = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
val_input = [str(x).strip() for x in open('input').readlines()]
print(val_input)


def calc_position(input):
    _depth = 0
    _horizontal = 0
    _aim = 0

    for elem in input:
        if elem[:-2] == 'forward':
            _horizontal += int(elem[-1])
            _depth += (_aim * int(elem[-1]))
        elif elem[:-2] == 'up':
            _aim -= int(elem[-1])
        elif elem[:-2] == 'down':
            _aim += int(elem[-1])

    return _horizontal * _depth


print(calc_position(val_input))
