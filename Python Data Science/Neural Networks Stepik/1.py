import numpy as np
import numpy.linalg as npla
import random
import pandas as pd

from urllib.request import urlopen

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[1, 2, 3, 6], [4, 5, 6, 6], [11, 12, 13, 14]])

A = np.asmatrix(A)
B = np.asmatrix(B)

C = np.matmul(A, B)

C = np.eye(N=3, M=4, k=1) + np.eye(N=3, M=4) * 2


def first_practice():
    print(A, '\n\n', A.flatten())  # flatten распрямляет массив
    print(A, '\n\n', A.transpose())
    print(A, '\n\n', A.reshape(6, 1))


w = np.array(random.sample(range(1000), 12))
w = w.reshape(2, 2, 3)


def second_practice(w):
    print(w)  # first argument set, nums of matrix (if you set 3 arguments)
    print(w.transpose(2, 1, 0))  # we can change axises
    print(w.transpose(1, 0, 2))  # we can change axises
    print('\n', "w == w.transpose(0, 1, 2)", '\n')
    print(w.transpose(0, 1, 2))
    print('\n', "w == w.transpose(1, 0, 2)", '\n')
    print(w.transpose(1, 0, 2))
    print('\n', "w == w.transpose(1, 2, 0)", '\n')
    print(w.transpose(1, 2, 0))
    print('\n', "w == w.transpose(0, 2, 1)", '\n')
    print(w.transpose(0, 2, 1))
    print('\n', "w == w.transpose(2, 0, 1)", '\n')
    print(w.transpose(2, 0, 1))
    print('\n', "w == w.transpose(2, 1, 0)", '\n')
    print(w.transpose(2, 1, 0))


def third_practice():
    mat = np.eye(N=3, M=4, k=1) + np.eye(N=3, M=4) * 2
    print(mat.reshape(12, 1))
    print(mat.mean(axis=None))  # mean by whole massive, axis=0 -- columns, axis=1 -- rows
    print(mat.sum(axis=None))


def fourth_practice(w):
    print(w.dot([1, 2, 3]))  # matrix multiply


# matrices multiply
def fifth_practice():
    x_shape = tuple(map(int, input().split()))
    X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
    y_shape = tuple(map(int, input().split()))
    Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)
    try:
        print(np.dot(X, Y.transpose()))
    except ValueError:
        print("matrix shapes do not match")


def sixth_practice():
    name = input()
    f = urlopen(name)
    print(np.loadtxt(f, delimiter=',', skiprows=1).mean(axis=0))


# create beta scores
def seventh_practice():
    X = np.array([[1, 1, 1], [60, 50, 75]]).transpose()
    y = np.array([10, 7, 12])

    mat_multiple_1 = npla.inv(X.transpose().dot(X))
    mat_multiple_2 = X.transpose().dot(y)
    print(np.dot(mat_multiple_1, mat_multiple_2).round(3))


def eighth_practice():
    data = pd.read_csv("https://stepic.org/media/attachments/lesson/16462/boston_houses.csv")  # load data to work with
    y = data.iloc[:, 0]
    X = data.iloc[:, 1:]
    X.insert(0, column='free', value=1)
    beta = npla.inv(X.T.dot(X)).dot(X.T).dot(y)
    print(" ".join(map(str, beta)))


