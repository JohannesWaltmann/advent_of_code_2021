import numpy as np

test_data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
val_data = np.loadtxt('in', dtype=int)
print(val_data)
counter = 0

for i in range(3, len(val_data)):
    if (val_data[i]) > (val_data[i-3]):
        counter += 1

print(counter)
