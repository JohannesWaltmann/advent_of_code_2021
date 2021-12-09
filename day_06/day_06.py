import numpy as np

test_population = np.loadtxt('resources/test_population', dtype=int, max_rows=1, delimiter=',')
validation_population = np.loadtxt('resources/validation_population', dtype=int, max_rows=1, delimiter=',')


def t01_calc_population(base_population) -> int:

    working_population = np.copy(base_population)
    cycle = 80

    for round in cycle:

