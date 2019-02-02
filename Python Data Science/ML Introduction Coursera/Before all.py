import numpy as np

#print(np.random.normal(1, 10, (1000, 50)))

X = np.random.normal(loc=1, scale=10, size=(1000, 50))


mean = np.mean(X, axis=0) #one -- rows, zero -- cols
#print(mean)

sd = np.std(X, axis=0)

X_norm = (X - mean)/sd
#print(X_norm)


Z = np.array([[4, 5, 0],
             [1, 9, 3],
             [5, 1, 1],
             [3, 3, 3],
             [9, 9, 9],
             [4, 7, 1]])

r = np.sum(Z, axis=1)

#print(np.nonzero(r > 10)) #nonzero is numer of elements. this is which from R


one = np.eye(3) # generate matrix with 1 ob diagonal
two = np.eye(3)

three = np.vstack((one, two)) # vstack like a rbind, hstack like a cbind

#print(three)


