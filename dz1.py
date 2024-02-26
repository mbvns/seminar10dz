#/usr/bin/python:

import pandas as pd
import random
from sklearn.preprocessing import OneHotEncoder

# Исходный код генерирующий pandas data frame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(f"Исходный data frame:\n{data}")

# Для создания one-hot вида исходного data frame воспользуемся классом
# OneHotEncoder из библиотеки scikit-learn, кот нужно сначала установить с помощью pip

# создадим экземпляр OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)

# передаем в метод fit_transformation наш data frame
onehot = encoder.fit_transform(data)

print(f"В виде one-hot:\n{onehot}")
