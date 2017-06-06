import numpy as np
import pandas as pd
import glob

ds = pd.read_csv('survey/data_complete/171981736.csv', delimiter=';', header=None)
a1 = {"First statement", "Первое утверждение", "От 1 до 3 сотрудников", "From 1 to 3 employees"}
a2 = {"Second statement", "Второе утверждение", "От 3 до 5 сотрудников", "From 3 to 5 employees"}
a3 = {"Third statement", "Третье утверждение", "From 5 employees and above", "От 5 сотрудников и выше"}




# ds[10] = ds[9].replace(lambda x: 1, a1)
ds1 = ds[9].replace(a1, 1, regex=True).replace(a2, 2,regex=True).replace(a3,3,regex=True)

# for i in range(0, len(ds)):
# ds[10].replace('Первое утверждение', '1')

    # if (ds.iloc[i, 9] == 'First statement') | (ds.iloc[i, 9] == 'Первое утверждение'):
    #     ds.iloc[i, 10] = 1
    # elif (ds.iloc[i, 9] == 'Second statement') | (ds.iloc[i, 9] == 'Второе утверждение'):
    #     ds.iloc[i, 10] = 2
    # else:
    #     ds.iloc[i, 10] = 3

# data_predict = ds[10].reshape(1, -1)
maturity_level = 3

for i in range(len(ds1), 36):
    ds1[i] = np.random.randint(1,4)

a = sum(ds1[0:16])/17
b = sum(ds1[17:24])/8
c = sum(ds1[24:31])/8
d = sum(ds1[31:35])/4

first = 1



print(glob.glob('survey/data_incomplete/17*.csv'))
# x.to_csv('survey/data_complete/test1.csv', sep=';', header=None)
