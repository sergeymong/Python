import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm, model_selection

newsgroups = datasets.fetch_20newsgroups(subset='all', categories=['alt.atheism', 'sci.space'])
newsgroups.data  # texts
newsgroups.target  # class numbers

# for work with text data we should create numeric view of text. One of this methods -- TF-IDF
print(newsgroups)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups.data) # fit transform -- learning data, transform - test data
y = vectorizer.transform(newsgroups.data)

feature_mapping = vectorizer.get_feature_names()
print(feature_mapping[2])

grid = {'C': np.power(10.0, np.arange(-5, 6))}
cv = model_selection.KFold(n_splits=5, random_state=241, shuffle=True)
clf = svm.SVC(kernel='linear', random_state=241)
gs = model_selection.GridSearchCV(clf, grid, scoring='accuracy', cv=cv)
gs.fit(X, y)
