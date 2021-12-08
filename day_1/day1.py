import numpy as np


def import_data(filename) -> []:
    return np.loadtxt(filename, dtype=int)


def count_measurements(set_name) -> int:
    dataset = import_data(set_name)
    _counter = 0

    for measurement in range(len(dataset)):
        if dataset[measurement] > dataset[measurement - 1]:
            _counter += 1

    return _counter


def count_measurements_windowed(set_name) -> int:
    _dataset = import_data(set_name)
    _counter = 0

    for i in range(3, len(_dataset)):
        if (_dataset[i]) > (_dataset[i - 3]):
            _counter += 1

    return _counter


""" Test implementation """
task_01_test = count_measurements('test_data')
task_02_test = count_measurements_windowed('test_data')

print(f'Task 01 test: {task_01_test}\nTask 02 test: {task_02_test}')

""" Solution Output """
task_01_output = count_measurements('val_data')
task_02_output = count_measurements_windowed('val_data')

print(f'Task 01 output: {task_01_output}\nTask 02 output: {task_02_output}')
