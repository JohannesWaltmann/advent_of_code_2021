# --- Day 5: Hydrothermal Venture ---
#
# You come across a field of hydrothermal vents on the ocean floor!
# These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
# where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end.
# These line segments include the points at both ends. In other words:
#     An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#
# --- Part 1 ---
# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap.
# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

import numpy as np

test_coordinates = np.array([[[int(z) for z in y.split(",")] for y in x.split(" -> ")]
                             for x in open('resources/test_coordinates', 'r').readlines()], dtype=int)
val_coordinates = np.array([[[int(z) for z in y.split(",")] for y in x.split(" -> ")]
                            for x in open('resources/val_coordinates', 'r').readlines()], dtype=int)
vent_grid = np.zeros((999, 999))


def find_overlaps(coordinates, grid):
    for pair in coordinates:
        x1, y1, x2, y2 = pair[0][0], pair[0][1], pair[1][0], pair[1][1]

        if x1 == x2:
            if y1 < y2:
                move = 1
            else:
                move = -1
            for increment in range(y1, y2 + move, move):
                grid[x1, increment] += 1
        elif y1 == y2:
            if x1 < x2:
                move = 1
            else:
                move = -1
            for increment in range(x1, x2 + move, move):
                grid[increment, y1] += 1

    return np.sum(np.where(grid > 1, 1, 0))

# TODO: Check why val output has offset of 5
# TODO: Work on task 2
print(find_overlaps(test_coordinates, vent_grid))
print(find_overlaps(val_coordinates, vent_grid))
