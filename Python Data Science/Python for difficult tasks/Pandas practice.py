import pandas as pd
import numpy as np
# 1
# print(pd.__version__)  # check version of pandas

# 2
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

pdser1 = pd.Series(mylist)
pdser2 = pd.Series(myarr)
pdser3 = pd.Series(mydict)

# print(pdser1, pdser2, pdser3)

# 3
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = ser.to_frame().reset_index()
# print(df)

# 4
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.concat([ser1, ser2], axis=1)
# or
df2 = pd.DataFrame({'ser1': ser1, 'ser2':ser2})
# print(df, '\n\n', df2)

# 5
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser.name = 'alphabet'

# print(ser)

# 6
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

print(ser1 ^ ser2)