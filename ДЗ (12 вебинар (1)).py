import numpy as np
vector = np.random.randint(1, 10, 100)
res = vector[vector > 7]
print(res)
percent = np.size(res)
print(percent)