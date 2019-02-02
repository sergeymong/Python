import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 0])
# clf = DecisionTreeClassifier()
# clf.fit(X, y)

# importances = clf.feature_importances_

np.isnan(X)

df = pd.read_csv('titanic.csv')
df1 = df[['Pclass', 'Fare', 'Age', 'Sex']]
df1 = df1.dropna()
df1 = df1.replace(["male", "female"], [0, 1])

Y = df['Survived'][df1.index.values]

clf = DecisionTreeClassifier(random_state=241)
clf.fit(df1, Y)
importances = clf.feature_importances_

res = list(zip(list(df1), importances))
res = pd.DataFrame(res, columns=['Names', 'Values'])
res = res.sort_values(by=['Values'], ascending=False)
res = res.reset_index(drop=False)




print(res[['Names']].head(2))
print(res)

