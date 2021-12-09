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

test_coordinates = [str(x).strip().split('->') for x in open('resources/test_coordinates', 'r').readlines()]
val_coordinates = [str(x).strip().split('->') for x in open('resources/val_coordinates', 'r').readlines()]

print(test_coordinates)


