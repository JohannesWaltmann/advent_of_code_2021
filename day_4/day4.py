import numpy as np

# Load draws
test_draw = np.loadtxt('resources/test_input', dtype=str, max_rows=1, delimiter=',')
val_draw = np.loadtxt('resources/val_input', dtype=str, max_rows=1, delimiter=',')

# Load boards
test_boards = np.loadtxt('resources/test_input', dtype=str, skiprows=2)
val_boards = np.loadtxt('resources/val_input', dtype=str, skiprows=2)

# Reshape Boards
test_boards = test_boards.reshape(test_boards.shape[0] // test_boards.shape[1], 5, 5)
val_boards = val_boards.reshape(val_boards.shape[0] // val_boards.shape[1], 5, 5)

print(test_boards)

def bingo(boards, draws):
    bool_mask = np.zeros_like(boards, dtype=bool)

    for draw in draws:
        for i in range(boards[0]):


