import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import KFold, cross_val_score
import pandas as pd
import csv


def model_predict(chat_id):

    file_name = 'survey/data_complete/' + str(chat_id) + '.csv'
    ds = pd.read_csv(file_name, delimiter=';', header=None)

    a1 = {"First statement", "Первое утверждение", "От 1 до 3 сотрудников", "From 1 to 3 employees"}
    a2 = {"Second statement", "Второе утверждение", "От 3 до 5 сотрудников", "From 3 to 5 employees"}
    a3 = {"Third statement", "Третье утверждение", "From 5 employees and above", "От 5 сотрудников и выше"}

    data_predict = ds[9].replace(a1, 1, regex=True).replace(a2, 2, regex=True).replace(a3, 3, regex=True)
    # with open('survey/recommend_data/' + str(chat_id) + '.csv', 'a+', newline='') as user_file:
    #     columns =
    #     writer = csv.writer(user_file, delimiter=';')
    #     writer.writerow(columns)

    for i in range(len(data_predict), 40):
        data_predict[i] = np.random.randint(1, 4)
    # ds = data_predict

    data_predict = data_predict[4:40].values.reshape(1, -1)

    df = pd.read_csv('survey/data_complete/data_new.csv', delimiter=';', header=None)

    X = df.loc[:, 4:39]
    y = df.loc[:, 40]

    kf = KFold(len(y), n_folds=5, random_state=1, shuffle=True)

    scores = [0.0]
    k_range = range(10, 51)
    for k in k_range:
        model = RandomForestClassifier(n_estimators=k, random_state=1, n_jobs=2)
        model.fit(X, y)
        score = np.mean(cross_val_score(model, X, y, cv=kf, scoring='r2'))
        scores.append(score)

    prediction = model.predict(data_predict)

    # ds[36] = prediction
    # user_file = 'survey/recommend_data/' + str(chat_id) + '.csv'
    # ds.to_csv(user_file, sep=';')

    return prediction


# mod = model_predict('171981736')
# print(mod)