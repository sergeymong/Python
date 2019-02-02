import sklearn.datasets as sld
import sklearn.preprocessing as slp
import sklearn.model_selection as slms
import sklearn.neighbors as sln
import sklearn
import pandas as pd
import numpy as np


df = sld.load_boston()

X = df['data']
y = df['target']
X = slp.scale(X)
kf = slms.KFold(n_splits=5, shuffle=True, random_state=42)


def test_regression(kf, X, y):
    cross = list()
    p_range = np.linspace(1, 10, 200) #the same as seq in R
    for p in p_range:
        model = sln.KNeighborsRegressor(n_neighbors=5, weights='distance', metric='minkowski', p=p)
        cross.append(slms.cross_val_score(model, X, y, cv=kf, scoring='neg_mean_squared_error'))
    return pd.DataFrame(cross, p_range).max(axis=1).sort_values(ascending=False)



accuracy = test_regression(kf, X, y)
top_accuracy = accuracy.head(1)
print(accuracy, top_accuracy, top_accuracy.index[0])