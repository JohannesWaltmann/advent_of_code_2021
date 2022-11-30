import numpy as np


def read_input(file_path):
    digits, commands = set(), []

    for line in open(file_path, 'r'):
        if ',' in line:
            digits.add(tuple(map(int, line.split(','))))
        elif '=' in line:
            commands += line.strip().split(',')

    return digits, commands


def fold_once(input_file):
    sheet_markers, commands = read_input(input_file)
    fold_command = ''

    # Find the first folding command
    if 'y' in commands[0]:
        fold_command = commands[0][commands[0].find('y'):]
    elif 'x' in commands[0]:
        fold_command = commands[0][commands[0].find('x'):]
    # And split it at '='
    fold_command = fold_command.split('=')

    # Fill array with dots
    base_matrix = np.full((1 + np.max([[x[0] for x in sheet_markers]]),
                           1 + np.max([[x[1] for x in sheet_markers]])), '.')

    # Replace '.' with '#' according to sheet_marker positions
    for marker in sheet_markers:
        y_pos = marker[1] if marker[1] > 0 else marker[1]
        x_pos = marker[0] if marker[0] > 0 else marker[0]
        base_matrix[x_pos][y_pos] = '#'

    if fold_command[0] == 'x':
        temp_matrix = np.full((len(base_matrix)- (1 + int(fold_command[1])), len(base_matrix[0])), '.')
        pass
    elif fold_command[0] == 'y':
        # New matrix with size after the fold filled with '.'
        temp_matrix = np.full((len(base_matrix), len(base_matrix[0])-(1+int(fold_command[1]))), '.')
        print(temp_matrix.shape)
        print(temp_matrix)
        np.copyto(temp_matrix, base_matrix, where="Werte mit Y-Koordinate <= 7")
        # TODO: Fix where condition above
        for x in range(0, len(base_matrix)):
            base_matrix[x][7] = 'X'

    #base_matrix = base_matrix.T
    print(base_matrix)


fold_once('resources/test')
