import pandas as pd
import numpy as np
import scipy as sp
import re

df = pd.read_csv('titanic.csv', index_col='PassengerId')

print(list(df))

male = sum(df['Sex'] == 'male')
female = sum(df['Sex'] == 'female')

survived = sum(df['Survived'] == 1) / df.shape[0] * 100
first_p = sum(df['Pclass'] == 1) / df.shape[0] * 100

median_age = np.nanmedian(df['Age'])
mean_age = np.nanmean(df['Age'])
print(mean_age, median_age)

cor = round(np.corrcoef(df['SibSp'], df['Parch'])[1][0], 2)

df['Name'][df['Sex'] == 'female'].to_excel('test.xlsx')

tt = df['Name'][df['Sex'] == 'female']


def match_names(expr, name):
    if name.find('(') == -1:
        try:
            name = re.findall(expr, name)[0][0]
        except:
            try:
                name = re.findall(expr, name)[1][0]
            except:
                try:
                    name = re.findall(expr, name)[0][1]
                except:
                    try:
                        name = re.findall(expr, name)[1][1]
                    except:
                        name = ""
    else:
        try:
            name = re.findall(expr, name)[1][1]
        except:
            try:
                name = re.findall(expr, name)[1][0]
            except:
                try:
                    name = re.findall(expr, name)[0][1]
                except:
                    try:
                        name = re.findall(expr, name)[0][0]
                    except:
                        name = ""
    return name


expr = r'(?:Mrs\.|Miss\.|Dr\.) (\w+)|\((\w+)'
res = list()
for i in tt:
    res.append(match_names(expr, i))

res = pd.DataFrame({'Names': res})

print(res.reset_index().groupby(['Names']).sum())
