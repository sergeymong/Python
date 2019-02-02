import sklearn.model_selection as sklms
import sklearn.neighbors as skln
import sklearn.preprocessing as sklp
import numpy as np
import pandas as pd


names = ['Class', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols',
         'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue',
         'OD280/OD315 of diluted wines', 'Proline']
df = pd.read_csv('wine.data', names=names)

X = df.loc[:,'Alcohol':]
y = df['Class']

kf = sklms.KFold(n_splits=5, shuffle=True, random_state=42)

def test_accuracy(kf, X, y):
    scores = list()
    k_range = range(1, 50)
    for k in k_range:
        model = skln.KNeighborsClassifier(n_neighbors=k)
        scores.append(sklms.cross_val_score(model, X, y, cv=kf, scoring='accuracy'))
    return pd.DataFrame(scores, k_range).mean(axis=1).sort_values(ascending=False)


print(test_accuracy(kf, X, y))

accuracy = test_accuracy(kf, X, y)
top_accuracy = accuracy.head(1)
print(1, top_accuracy.index[0])  # if best index is 1, perhaps this is not best way of classification
print(2, top_accuracy.values[0])

X = sklp.scale(X)
accuracy = test_accuracy(kf, X, y)
top_accuracy = accuracy.head(1)
print(3, top_accuracy.index[0])
print(4, top_accuracy.values[0])  # after scaling our classification more accuracy

