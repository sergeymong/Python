import numpy as np
import sklearn.linear_model as sllm
import sklearn.metrics as slm
import sklearn.preprocessing as slp
import pandas as pd


def examples():
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    clf = sllm.Perceptron()
    clf.fit(X, y)
    predictions = clf.predict(X)

    print(predictions)

    slm.accuracy_score()  # metrics of accuracy
    scaler = slp.StandardScaler()
    scaler.fit_transform()  # находит параметры нормализации (средние и дисперсии каждого признака) по выборке,
    # и сразу же делает нормализацию выборки с использованием этих параметров

    scaler = StandardScaler()
    X_train = np.array([[100.0, 2.0], [50.0, 4.0], [70.0, 6.0]])
    X_test = np.array([[90.0, 1], [40.0, 3], [60.0, 4]])
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return 0


names = ['y', 'X1', 'X2']
train = pd.read_csv('perceptron-train.csv', names=names)
test = pd.read_csv('perceptron-test.csv', names=names)

clf = sllm.Perceptron(random_state=241)
clf.fit(X=train[['X1', 'X2']], y=train['y'])

predictions = clf.predict(test[['X1', 'X2']])
accuracy = slm.accuracy_score(test['y'], predictions)

scaler = slp.StandardScaler()
X_train_s = scaler.fit_transform(train[['X1', 'X2']])
X_test_s = scaler.transform(test[['X1', 'X2']])

clf.fit(X=X_train_s, y=train['y'])

predictions_s = clf.predict(X_test_s)
accuracy_s = slm.accuracy_score(test['y'], predictions_s)

answer = round(accuracy_s - accuracy)

print(accuracy, accuracy_s, answer)
