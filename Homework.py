import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = data['whoAmI'].unique()
one_hot_encoding = pd.DataFrame([[1 if cat == val else 0 for cat in categories] for val in data['whoAmI']],
                                columns=categories)

data_one_hot = pd.concat([data, one_hot_encoding], axis=1)

data_one_hot = data_one_hot.drop('whoAmI', axis=1)
