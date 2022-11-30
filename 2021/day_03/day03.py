# --- Day 3: Binary Diagnostic ---
# The diagnostic report (your puzzle input) consists of a list of binary numbers which,
# when decoded properly, can tell you many useful things about the conditions of the submarine.
# The first parameter to check is the power consumption.
#
# --- Part 1 ---
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers
# (called the gamma rate and the epsilon rate).
# The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
#
# --- Part 2 ---
# Next, you should verify the life support rating,
# which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.


test_data = [str(x).strip() for x in open('resources/test_data', 'r').readlines()]
val_data = [str(x).strip() for x in open('resources/val_data', 'r').readlines()]


def get_gamma_rate(data) -> str:
    """
    Computes the gamma rate by taking the most common bit for each bit in all binary entries of the given data set.

    :param data: Array of binary numbers arranged as Strings.
    :return: Gamma rate as a string of binary values.
    """
    _output = ''

    for elem in range(len(data[0])):
        _count_zeroes = 0
        _count_ones = 0

        # Iterate over each bit of the entries
        for bit in range(len(data)):
            if int(data[bit][elem]) == 0:
                _count_zeroes += 1
            elif int(data[bit][elem]) == 1:
                _count_ones += 1

        # Check if there are more '1' or '0' for the current bit
        if _count_ones > _count_zeroes:
            _output += '1'
        else:
            _output += '0'

    return _output


def get_epsilon_rate(data) -> str:
    """
    Computes the epsilon rate by taking the least common bit for each bit in all binary entries of the given data set.

    :param data: Array of binary numbers arranged as Strings.
    :return: Epsilon rate as a string of binary values.
    """
    _output = ''

    for elem in range(len(data[0])):
        _count_zeroes = 0
        _count_ones = 0

        # Iterate over each bit of the entries
        for bit in range(len(data)):
            if int(data[bit][elem]) == 0:
                _count_zeroes += 1
            elif int(data[bit][elem]) == 1:
                _count_ones += 1

        # Check if there are more '1' or '0' for the current bit
        if _count_ones > _count_zeroes:
            _output += '0'
        else:
            _output += '1'

    return _output


def calc_power_consumption(data) -> int:
    """
    Takes an array of binary strings as input to compute the power consumption
    using both the gamma and epsilon rate.

    :param data: Array of binary numbers arranged as Strings.
    :return: The power consumption gained from multiplying the decimal representation of both gamma and epsilon rate.
    """
    gamma_rate, epsilon_rate = get_gamma_rate(data), get_epsilon_rate(data)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def get_oxygen(data, index=0):
    """
    Determines the oxygen rating by recursively removing all values with the least sum per bit for each bit.

    :param data: Array of binary numbers as Stings.
    :param index: Starting index for the recursion.
    :return: The last remaining binary number of the complete input data.
    """
    index_inc = index
    cache_save = data

    # Go on until only one entry is left
    while len(cache_save) >= 1:
        for elem in range(len(cache_save[0])):
            _count_zeroes = 0
            _count_ones = 0

            # Walks over each bit in the samples
            for bit in range(len(cache_save)):
                if int(cache_save[bit][elem]) == 0:
                    _count_zeroes += 1
                elif int(cache_save[bit][elem]) == 1:
                    _count_ones += 1

            # Check for the max amount of bits per different bit per sample
            if _count_ones > _count_zeroes:
                cache_save = [x for x in cache_save if x[index_inc] == '1']
            elif _count_zeroes > _count_ones:
                cache_save = [x for x in cache_save if x[index_inc] == '0']
            else:
                # Take the entries with '1' if the count is the same
                cache_save = [x for x in cache_save if x[index_inc] == '1']
            index_inc += 1

        if len(cache_save) == 1: break
        get_oxygen(cache_save, index_inc)

    return cache_save


def get_co2(data, index=0):
    """
    Determines the co2 rating by recursively removing all values with the maximum sum per bit for each bit.

    :param data: Array of binary numbers as Stings.
    :param index: Starting index for the recursion.
    :return: The last remaining binary number of the complete input data.
    """
    index_inc = index
    cache_save = data

    # Go on until only one sample is left
    while len(cache_save) > 1:
        for elem in range(len(cache_save[0])):
            _count_zeroes = 0
            _count_ones = 0

            # Walks over each bit in the samples
            for bit in range(len(cache_save)):
                if int(cache_save[bit][elem]) == 0:
                    _count_zeroes += 1
                elif int(cache_save[bit][elem]) == 1:
                    _count_ones += 1

            # Check for the max amount of bits per different bit per sample
            if _count_ones > _count_zeroes:
                cache_save = [x for x in cache_save if x[index_inc] == '0']
            elif _count_zeroes > _count_ones:
                cache_save = [x for x in cache_save if x[index_inc] == '1']
            else:
                # Take the entries with '0' if the count is the same
                cache_save = [x for x in cache_save if x[index_inc] == '0']
            index_inc += 1

            if len(cache_save) == 1: break
        get_oxygen(cache_save, index_inc)

    return cache_save


def calc_life_support_rate(data) -> int:
    """
    Calculates the life support rate out of the given data input.

    :param data: Array of binary numbers as Strings.
    :return: Multiplies the decimal representations of oxygen rate and co2 rate to gain life support rate.
    """
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
