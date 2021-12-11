import numpy as np

test_input = np.loadtxt('resources/test_input', dtype=int, delimiter=',')
val_input = np.loadtxt('resources/validation_input', dtype=int, delimiter=',')


def print_fuel_cost(_input):
    median_pos = np.median(_input)

    fuel_count = 0

    for step in _input:
        cost = (step - median_pos)
        if cost < 0:
            cost *= -1
        fuel_count += cost

    print(int(fuel_count))


def print_fuel_cost_scaling(_input):
    avg_pos = np.average(_input)
    avg_pos = int(avg_pos)

    fuel_count = 0

    for step in _input:
        cost = np.abs(step - avg_pos)
        fuel_count += gauss_sum(cost)

    print(int(fuel_count))


def gauss_sum(number):
    return (number * (number + 1)) / 2


print_fuel_cost(test_input)
print_fuel_cost(val_input)

print_fuel_cost_scaling(test_input)
print_fuel_cost_scaling(val_input)
