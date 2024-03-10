X = [1, 3, 7]
y = [2, 6, 14]
lr = 0.01
w1 = 0
w0 = 0
epochs = 500
for epoch in range(1, epochs + 1):
    for i in range(len(X)):
        prediction = w1 * X[i] + w0
        w1 += 2 * lr * X[i] * (y[i] - prediction)
        w0 += 2 * lr * (y[i] - prediction)
print('w1 = ', w1, 'wo = ', w0)