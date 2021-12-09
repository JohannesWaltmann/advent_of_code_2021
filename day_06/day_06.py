import numpy as np

test_population = np.loadtxt('resources/test_population', dtype=int, max_rows=1, delimiter=',')
validation_population = np.loadtxt('resources/validation_population', dtype=int, max_rows=1, delimiter=',')


def t01_calc_population(base_population) -> int:
    working_population = list(base_population)
    cycle = 80

    while cycle > 0:
        for fish in range(len(working_population)):
            if working_population[fish] > 0:
                working_population[fish] -= 1
            else:
                working_population[fish] = 6
                working_population.append(8)
        cycle -= 1

    return len(working_population)


def t02_calc_population(base_population) -> int:

    arr = [0 for i in range(9)]
    for i in base_population:
        arr[i] += 1

    for i in range(256):
        births = arr.pop(0)
        arr.append(births)
        arr[6] += births
    return sum(arr)


print(f"Task 01 test solution: {t01_calc_population(test_population)}")
print(f"Task 01 validation solution: {t01_calc_population(validation_population)}")

print(f"Task 02 test solution: {t02_calc_population(test_population)}")
print(f"Task 02 validation solution: {t02_calc_population(validation_population)}")
