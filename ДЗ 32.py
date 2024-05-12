from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import scikitplot as skplt
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

mnist = fetch_openml(data_id554)
type(mnist.data), type(mnist.categories), type(mnist.feature_names), type(mnist.target)
data = np.array(mnist.data)
targets = np.array(mnist.target)

plt.figure(figsize=(20, 4))
for index, (image, label) in enumerate(zip(data[0:5], targets[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (28, 28)), cmap='gray')
    plt.title('Train: ' + label)

X_train, X_test, y_train, y_test = train_test_split(data[:10000, :], targets[:10000].astype('int'), test_size=0.2)
X_train.shape, X_test.shape

clf = LogisticRegression(solver='saga', penalty='l2', n_jobs=5, tol=0.01, max_iter=1000)
clf.fit(X_train, y_train)

accuracy = np.mean(y_pred == y_test)
print('Test accuracy: %Sf' % accuracy)

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: ', accuracy)
precision = precision_score(y_test, y_pred, average='weighted')
print('Precision: ', precision)
recall = recall_score(y_test, y_pred, average='weighted')
print('Recall: ', recall)
f1 = f1_score(y_test, y_pred, average='weighted')
print('F1: ', f1)

skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True)
print(classification_report(y_test, y_pred))