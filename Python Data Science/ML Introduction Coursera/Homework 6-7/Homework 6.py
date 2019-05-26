import pandas as pd
import numpy as np
from sklearn.svm import SVC

data = pd.read_csv('svm-data.csv', header=None)
print(data)


y = data[0]
X = data[[1, 2]]
#print(y, X == X1)

model = SVC(kernel='linear', C=100000, random_state=241)  # kernel and C -- main parameters in SVC
model.fit(X, y)

vectors = model.support_

print(1, ' '.join([str(n + 1) for n in vectors]))
