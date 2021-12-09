import numpy as np

test_coordinates = [str(x).strip().split('->') for x in open('resources/test_coordinates', 'r').readlines()]
val_coordinates = [str(x).strip().split('->') for x in open('resources/val_coordinates', 'r').readlines()]

print(test_coordinates)


