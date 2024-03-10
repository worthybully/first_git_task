import matplotlib.pyplot as plt
X = [1, 3, 7]
y = [2, 6, 14]
lr = 0.01
w1 = 1.992696552961867
w0 = 0.051124129266931474
plt.scatter(X, y, color='blue')
plt.plot([0, 7], [w0, w1 * 7 + w0])
plt.xlabel('X')
plt.ylabel('y')
plt.grid()
plt.show()