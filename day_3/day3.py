test_data = [str(x).strip() for x in open('ressources/test_data', 'r').readlines()]
val_data = [str(x).strip() for x in open('ressources/val_data', 'r').readlines()]


def get_gamma_rate(data) -> str:

    _output = ''

    for elem in range(len(data[0])):
        _count_zeroes = 0
        _count_ones = 0

        for bit in range(len(data)):
            if int(data[bit][elem]) == 0:
                _count_zeroes += 1
            elif int(data[bit][elem]) == 1:
                _count_ones += 1

        if _count_ones > _count_zeroes:
            _output += '1'
        else:
            _output += '0'

    return _output


def get_epsilon_rate(data) -> str:

    _output = ''

    for elem in range(len(data[0])):
        _count_zeroes = 0
        _count_ones = 0

        for bit in range(len(data)):
            if int(data[bit][elem]) == 0:
                _count_zeroes += 1
            elif int(data[bit][elem]) == 1:
                _count_ones += 1

        if _count_ones > _count_zeroes:
            _output += '0'
        else:
            _output += '1'

    return _output


def calc_power_consumption(data) -> int:
    gamma_rate, epsilon_rate = get_gamma_rate(data), get_epsilon_rate(data)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


""" Eval test_data. """
print(f'Task 01 tests: {calc_power_consumption(test_data)}')
# print(f'Task 02 tests: {}')

""" Eval val_data. """
print(f'Task 01 validation: {calc_power_consumption(val_data)}')
# print(f'Task 02 validation: {}')
