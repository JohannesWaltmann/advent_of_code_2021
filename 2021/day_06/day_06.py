# --- Day 6: Lanternfish ---
# A massive school of glowing lanternfish swims past.
# They must spawn quickly to reach such large numbers - maybe exponentially quickly?
# You should model their growth rate to be sure.
# Although you know nothing about this specific species of lanternfish, you make some guesses about their attributes.
# Surely, each lanternfish creates a new lanternfish once every 7 days.
# However, this process isn't necessarily synchronized between every lanternfish,
# one lanternfish might have 2 days left until it creates another lanternfish, while another might have 4.
# So, you can model each fish as a single number that represents the number of days until it creates a new lanternfish.
#
# A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value).
# The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.
#
# --- Part 1 ---
# Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?
#
# --- Part 2 ---
# Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?
# How many lanternfish would there be after 256 days?


import numpy as np

test_population = np.loadtxt('resources/test_population', dtype=int, max_rows=1, delimiter=',')
validation_population = np.loadtxt('resources/validation_population', dtype=int, max_rows=1, delimiter=',')


def t01_calc_population(base_population) -> int:
    """
    Gets a starting population of fish as input and determines their number after an 80 days period.
    Each element in the starting population represents a fish and each element's value represents the
    reproduction timer.

    :param base_population: Array with information about the starting population.
    :return: The number of fish in the population
    """
    working_population = list(base_population)
    cycle = 80

    # Iterate over the 80-day cycle
    while cycle > 0:
        # Check each fish in the population
        for fish in range(len(working_population)):
            # Decrease the counter per fish
            if working_population[fish] > 0:
                working_population[fish] -= 1
            else:
                # Produce a new fish and reset the counter
                working_population[fish] = 6
                working_population.append(8)
        cycle -= 1

    return len(working_population)


def t02_calc_population(base_population) -> int:
    """
    Gets a starting population of fish as input and determines their number after an 256 days period.
    Each element in the starting population represents a fish and each element's value represents the
    reproduction timer.
    Also uses a better storage management to overcome O(log(n)) as runtime.

    :param base_population: Array with information about the starting population.
    :return: The number of fish in the population
    """
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
