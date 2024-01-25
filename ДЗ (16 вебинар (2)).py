import numpy as np
import matplotlib.pyplot as plt
X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)
sizes = 1000 * np.random.rand(3000)
colors = np.random.rand(3000)
plt.scatter(X, Y, c=colors, s=sizes, marker='+', alpha=0.5)
plt.grid()
plt.title('Диаграмма рассеяния')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()