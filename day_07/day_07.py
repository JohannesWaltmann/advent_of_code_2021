import numpy as np

test_input = np.loadtxt('resources/test_input', dtype=int, delimiter=',')
val_input = np.loadtxt('resources/validation_input', dtype=int, delimiter=',')


def print_fuel_cost(_input):
    """
    Determines the total fuel cost which can be achieved by the least possible steps to
    align each input value.
    Takes the median value of the input
    and determines the cost from each input value to the median.

    :param _input: Array with different position values as integer.
    :return: Sum of fuel costs for each entry of the input to the median value.
    """
    median_pos = np.median(_input)
    fuel_count = 0

    for step in _input:
        cost = (step - median_pos)
        if cost < 0:
            cost *= -1
        fuel_count += cost

    print(int(fuel_count))


def print_fuel_cost_scaling(_input):
    """
    Determines the total fuel cost to be achieved by the least possible steps.
    For each step taken the cost is equal to the number of steps taken for that specific input.

    The cost is computed by aligning all values to the average value and taking the gaussian sum of the
    number of steps from starting position to the average.

    :param _input: Array with different position values as integer.
    :return: Sum of fuel costs for each entry of the input to the average value.
    """
    avg_pos = np.average(_input)
    avg_pos = int(avg_pos)

    fuel_count = 0

    for step in _input:
        cost = np.abs(step - avg_pos)
        fuel_count += gauss_sum(cost)

    print(int(fuel_count))


def gauss_sum(number):
    """ Computes the gaussian sum for an input number. """
    return (number * (number + 1)) / 2


print('Task 01 test: '), print_fuel_cost(test_input)
print('Task 01 val: '), print_fuel_cost(val_input)

print('Task 02 test: '), print_fuel_cost_scaling(test_input)
print('Task 02 val: '), print_fuel_cost_scaling(val_input)
