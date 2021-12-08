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


def get_oxygen(data, index=0):
    index_inc = index
    cache_save = data

    while len(cache_save) >= 1:
        for elem in range(len(cache_save[0])):
            _count_zeroes = 0
            _count_ones = 0

            for bit in range(len(cache_save)):
                if int(cache_save[bit][elem]) == 0:
                    _count_zeroes += 1
                elif int(cache_save[bit][elem]) == 1:
                    _count_ones += 1

            if _count_ones > _count_zeroes:
                cache_save = [x for x in cache_save if x[index_inc] == '1']
            elif _count_zeroes > _count_ones:
                cache_save = [x for x in cache_save if x[index_inc] == '0']
            else:
                cache_save = [x for x in cache_save if x[index_inc] == '1']
            index_inc += 1

        if len(cache_save) == 1: break
        get_oxygen(cache_save, index_inc)

    return cache_save


def get_co2(data, index=0):
    index_inc = index
    cache_save = data

    while len(cache_save) > 1:
        for elem in range(len(cache_save[0])):
            _count_zeroes = 0
            _count_ones = 0

            for bit in range(len(cache_save)):
                if int(cache_save[bit][elem]) == 0:
                    _count_zeroes += 1
                elif int(cache_save[bit][elem]) == 1:
                    _count_ones += 1

            if _count_ones > _count_zeroes:
                cache_save = [x for x in cache_save if x[index_inc] == '0']
            elif _count_zeroes > _count_ones:
                cache_save = [x for x in cache_save if x[index_inc] == '1']
            else:
                cache_save = [x for x in cache_save if x[index_inc] == '0']
            index_inc += 1

            if len(cache_save) == 1: break
        get_oxygen(cache_save, index_inc)

    return cache_save


def calc_life_support_rate(data) -> int:
    oxygen = get_oxygen(data)[0]
    co2 = get_co2(data)[0]

    return int(oxygen, 2) * int(co2, 2)


""" Eval test_data. """
print(f'Task 01 tests power consumption: {calc_power_consumption(test_data)}')
print(f'Task 02 tests oxygen: {get_oxygen(test_data)[0]}')
print(f'Task 02 tests co2: {get_co2(test_data)}')

""" Eval val_data. """
print(f'Task 01 validation: {calc_power_consumption(val_data)}')
print(f'Task 02 validation: {calc_life_support_rate(val_data)}')
