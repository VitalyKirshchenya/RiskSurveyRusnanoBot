import pandas as pd
import numpy as np

file_name = 'recommend_data/171981736.csv'
ds1 = pd.read_csv(file_name, delimiter=';', header=None)
#
# a1 = {"First statement", "Первое утверждение", "От 1 до 3 сотрудников", "From 1 to 3 employees"}
# a2 = {"Second statement", "Второе утверждение", "От 3 до 5 сотрудников", "From 3 to 5 employees"}
# a3 = {"Third statement", "Третье утверждение", "From 5 employees and above", "От 5 сотрудников и выше"}
#
# data_predict = ds[9].replace(a1, 1, regex=True).replace(a2, 2, regex=True).replace(a3, 3, regex=True)
# for i in range(len(data_predict), 36):
#     data_predict[i] = np.random.randint(1, 4)
# data_predict.to_csv('recommend_data/1.csv', sep=';')
p1 = sum(ds1.iloc[0:16, 1]) / 17
p2 = sum(ds1.iloc[17:24, 1]) / 8
p3 = sum(ds1.iloc[24:31, 1]) / 8
p4 = sum(ds1.iloc[31:35, 1]) / 4

b = []
b.append(sum(ds1.iloc[0:2, 1]) / 3)
b.append(sum(ds1.iloc[3:6, 1]) / 4)
b.append(sum(ds1.iloc[7:12, 1]) / 6)
b.append(sum(ds1.iloc[13:14, 1]) / 2)
b.append(sum(ds1.iloc[15:16, 1]) / 2)
b.append(sum(ds1.iloc[17:19, 1]) / 3)
b.append(sum(ds1.iloc[20:22, 1]) / 3)
b.append(ds1.iloc[23, 1])
b.append(ds1.iloc[24, 1])
b.append(sum(ds1.iloc[25:29, 1]) / 5)
b.append(sum(ds1.iloc[30:31, 1]) / 2)
b.append(sum(ds1.iloc[32:33, 1]) / 2)
b.append(sum(ds1.iloc[34:35, 1]) / 2)

print(p1, p2, p3, p4, (ds1.iloc[36, 1] + 1) / 2, ds1.mean())
print(b)

