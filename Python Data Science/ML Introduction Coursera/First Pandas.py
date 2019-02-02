from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import os
import numpy.random as np

import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib

import random

# Enable inline plotting


print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

names = ['Jess', 'Sergey', 'Roman', 'Julia', 'Emil']
births = [555, 518, 712, 123, 958]

BabyDataSet = list(zip(names, births))
print(BabyDataSet)

df = pd.DataFrame(BabyDataSet, columns=['Names', 'Births'])
print(df)

df.to_csv('Babydataset.csv', index=False, header=False)

Location = os.getcwd() + '/' + 'Babydataset.csv'
dfd = pd.read_csv(Location, header=None)  # without header (NOT FALSE)
dfd = pd.read_csv(Location, names=['Names', 'Births'], )
# print(dfd)

df.Births.dtypes  # you can view column type
df.dtypes  # or all dataframe types

# sorting values
# Method 1:
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)

df['Births'].max()

# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
#plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0),
 #                xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used

#plt.interactive(True)
#plt.show()
#######################



# Function to generate test data
def CreateDataSet(Number=1):
    Output = []

    for i in range(Number):
        # Create a weekly (mondays) date range
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')

        # Create random data
        data = np.randint(low=25, high=1000, size=len(rng))

        # Status pool
        status = [1, 2, 3]

        # Make a random list of statuses
        random_status = [status[np.randint(low=0, high=len(status))] for i in range(len(rng))]

        # State pool
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']

        # Make a random list of states
        random_states = [states[np.randint(low=0, high=len(states))] for i in range(len(rng))]

        Output.extend(zip(random_states, random_status, data, rng))

    return Output

dataset = CreateDataSet(4)
df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'CustomCount', 'StatusDate'])

df.head()

df.to_excel('Lesson3.xlsx', index=False)

Location = os.getcwd() + '/' + 'Lesson3.xlsx'

# This section attempts to clean up the data for analysis.
# Make sure the state column is all in upper case
# Only select records where the account status is equal to "1"
# Merge (NJ and NY) to NY in the state column
# Remove any outliers (any odd results in the data set)

dff = pd.read_excel(Location, 0, index_col='StatusDate')
print(df.dtypes)

print(df.index)

print(df['State'].unique())
df['State'] = df.State.apply(lambda x: x.upper())

print(df['State'].unique())

mask = df['Status'] == 1
df = df[mask]

mask = df.State == 'NJ'

print(df.Status)

df['State'][mask] = 'NY'

df['CustomCount'].plot(figsize=(15,5))
plt.show()



