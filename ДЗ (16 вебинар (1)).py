import numpy as np
import matplotlib.pyplot as plt

def my_func(X):
    return np.exp(X ** 2)

X = np.linspace(1, 12, 200)
Y = my_func(X)
plt.plot(X, Y, label='Вот такая моя функция', dashes=[6, 3], color='green', alpha=0.5)
plt.legend()
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График')
plt.show()