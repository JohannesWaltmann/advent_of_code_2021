# --- Day 4: Giant Squid ---
#
# You're already almost 1.5km (almost a mile) below the surface of the ocean,
# already so deep that you can't see any sunlight.
# What you can see, however, is a giant squid that has attached itself to the outside of your submarine.
#
# Maybe it wants to play bingo?
#
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
# Numbers are chosen at random, and the chosen number is marked on all boards on which it appears.
# (Numbers may not appear on all boards.)
# If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

import numpy as np

# Load draws
test_draw = np.loadtxt('resources/test_input', dtype=str, max_rows=1, delimiter=',')
val_draw = np.loadtxt('resources/val_input', dtype=str, max_rows=1, delimiter=',')

# Load boards
test_boards = np.loadtxt('resources/test_input', skiprows=2)
val_boards = np.loadtxt('resources/val_input', skiprows=2)


def task_01_bingo(boards, draws):
    """
    Computes a bingo on one of the given boards based on a given series of drawn numbers.

    :param boards: Three dim np-array containing a set of bingo boards.
    :param draws: Np-array with the set of drawn numbers.

    :returns: The sum of all non-marked numbers on the winning board multiplied by the winning number.
    """
    single_boards = np.array(np.split(boards, len(boards) / 5))
    bool_mask = np.zeros_like(single_boards, dtype=bool)

    for draw in draws:
        # Take every drawn number
        bool_mask[single_boards == int(draw)] = True

        num_board = 0
        for masked_board in bool_mask:
            # Flip the bool mask of each board to true if a drawn number is matched
            row_bingo = np.all(masked_board, axis=1)
            col_bingo = np.all(masked_board, axis=0)
            row_solved = np.any(row_bingo, axis=0)
            col_solved = np.any(col_bingo, axis=0)

            if row_solved or col_solved:
                # Compute the boardsum if a row or col is fully true
                winning_board = single_boards[num_board]
                winning_board[masked_board == True] = 0
                return int(np.sum(winning_board) * int(draw))
            num_board += 1


def task_02_bingo(boards, draws):
    """
    Computes a bingo on one of the given boards based on a given series of drawn numbers.

    :param boards: Three dim np-array containing a set of bingo boards.
    :param draws: Np-array with the set of drawn numbers.

    :returns: The sum of all non-marked numbers on the last winning board multiplied by its winning number.
    """
    single_boards = np.array(np.split(boards, len(boards) / 5))
    bool_mask = np.zeros_like(single_boards, dtype=bool)

    # Extra variables to keep track of the current last winner
    last_draw, last_board = -1, np.zeros((5, 5))
    last_marked = np.zeros_like(last_board, dtype=bool)

    for draw in draws:
        # Take every drawn number
        bool_mask[single_boards == int(draw)] = True

        num_board = 0

        for masked_board in bool_mask:
            # Flip the bool mask of each board to true if a drawn number is matched
            row_bingo = np.all(masked_board, axis=1)
            col_bingo = np.all(masked_board, axis=0)
            row_solved = np.any(row_bingo, axis=0)
            col_solved = np.any(col_bingo, axis=0)

            if row_solved or col_solved:
                # Set the current winning board as last winning board
                last_board = np.copy(single_boards[num_board])
                last_draw = draw
                last_marked = np.copy(masked_board)
                single_boards[num_board] = None
                bool_mask[num_board] = None
            num_board += 1

    # Compute the board sum of the last winning board
    last_board[last_marked == True] = 0
    return int(np.sum(last_board) * int(last_draw))


print(f"Task 01 test output: {task_01_bingo(test_boards, test_draw)}")
print(f"Task 01 validation output: {task_01_bingo(val_boards, val_draw)}")

print(f"Task 02 test output: {task_02_bingo(test_boards, test_draw)}")
print(f"Task 02 validation output: {task_02_bingo(val_boards, val_draw)}")
