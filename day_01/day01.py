# --- Day 1: Sonar Sweep ---
# As the submarine drops below the surface of the ocean,
# it automatically performs a sonar sweep of the nearby sea floor.
# On a small screen, the sonar sweep report (your puzzle input) appears:
# each line is a measurement of the sea floor depth as the sweep looks further and further away from the submarine.
#
# This report indicates that, scanning outward from the submarine
# the sonar sweep found depths of 199, 200, 208, 210, and so on.
#
# --- Part 1 ---
# The first order of business is to figure out how quickly the depth increases,
# just so you know what you're dealing with
# - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.
#
# To do this, count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement.)
#
# --- Part 2 ---
# Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.
# Instead, consider sums of a three-measurement sliding window.
# Your goal now is to count the number of times
# the sum of measurements in this sliding window increases from the previous sum.
# So, compare A with B, then compare B with C, then C with D, and so on.
# Stop when there aren't enough measurements left to create a new three-measurement sum.


import numpy as np


def import_data(filename) -> []:
    """ Imports content from a given file into a np-array. """
    return np.loadtxt(filename, dtype=int)


def count_measurements(set_name) -> int:
    """
    Counts the number of times a depth measurement increases from the previous measurement.
    (There is no measurement before the first measurement.)

    :param set_name: Name of the set of measurements.
    :returns: Number of increases between measurements.
    """
    dataset = import_data(set_name)
    _counter = 0

    for measurement in range(len(dataset)):
        if dataset[measurement] > dataset[measurement - 1]:
            _counter += 1

    return _counter


def count_measurements_windowed(set_name) -> int:
    """
    Counts the number of times a depth measurement increases from the previous measurement.
    The sliding window can be shortened to only the first and third entry of each window.
    (There is no measurement before the first measurement.)

    :param set_name: Name of the set of measurements.
    :returns: Number of increases between each window of measurements.
    """
    _dataset = import_data(set_name)
    _counter = 0

    for i in range(3, len(_dataset)):
        if (_dataset[i]) > (_dataset[i - 3]):
            _counter += 1

    return _counter


""" Test implementation """
task_01_test = count_measurements('resources/test_data')
task_02_test = count_measurements_windowed('resources/test_data')

print(f'Task 01 test: {task_01_test}\nTask 02 test: {task_02_test}')

""" Solution Output """
task_01_output = count_measurements('resources/val_data')
task_02_output = count_measurements_windowed('resources/val_data')

print(f'Task 01 output: {task_01_output}\nTask 02 output: {task_02_output}')
