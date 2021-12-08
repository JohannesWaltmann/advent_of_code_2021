import numpy as np

test_data = [str(x).strip() for x in open('test_data').readlines()]
val_data = [str(x).strip() for x in open('val_data').readlines()]


def get_gamma_rate(data):
    _count_zeroes = 0
    _count_ones = 0
    _output = ''

    for elem in data:
        print(elem)
        for bit in range(len(elem)):
            print(elem[bit])
            if elem[bit] == '0':
                _count_zeroes += 1
            elif elem[bit] == '1':
                _count_ones += 1

        if _count_ones > _count_zeroes:
            print(f'output: {_output}')
            _output += '1'
        else:
            print(f'output: {_output}')
            _output += '0'

        _count_ones = 0
        _count_zeroes = 0

    return _output


print(get_gamma_rate(test_data))
