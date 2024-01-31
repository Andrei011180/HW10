# Исходный код
#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI':lst})
#data.head()


# 1. Вариант
#one_hot_encoded = pd.get_dummies(data['whoAmI'])
#result = pd.concat([data, one_hot_encoded], axis=1)
#result.head()


# 2. Вариант
#import pandas as pd

# Создаем DataFrame
#lst = ['robot']  *  10
#lst += ['human']  *  10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI': lst})

# Преобразуем в one hot вид
#one_hot_data = pd.get_dummies(data['whoAmI'])

# Объединяем исходный DataFrame и one hot DataFrame
#data = pd.concat([data, one_hot_data], axis=1)

# Удаляем исходный столбец
#data = data.drop('whoAmI', axis=1)

# Выводим DataFrame

#print(data.head())
