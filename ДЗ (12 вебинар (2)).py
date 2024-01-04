import numpy as np
count = 0
total = 0
while count != 1001:
    vector = np.random.randint(1, 10, 100)
    res = vector[vector > 7]
    percent = np.size(res)
    if percent == 20:
        total += 1
    count += 1
print(count)
print(total)
part_of_twenties = total / 1000
print(part_of_twenties)