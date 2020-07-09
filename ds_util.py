
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def my_train_val_test_split(df):
  train_1, test = train_test_split(df, test_size=0.15, random_state=42)
  train, val = train_test_split(train_1, test_size=0.15, random_state=42)
  return train, val, test

def find_nulls_func(df):
  my_list = []
  my_list = df.isnull().sum().tolist()
  new_series = pd.Series(my_list, index = df.columns) 
  return new_series


def enlarge(n):
    """ Will multiply the input by 100 """
    return n * 100

if __name__ == '__main__': 
    y = int(input("Choose a number: "))
    print(y, enlarge(y))

# ZEROS = np.zeros(5)
# ONES = np.ones(10)

# def train_validation_test_split(
#     x, y, trains_size=0.7, val_size=0.1, test_size=0.2,
#     random_state=None, shuffle=True):

#     assert train_size + val_size + test_size == 1

#     x_train_val, x_test, y_train_val, y_test = train_test_split(
#         x, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

#     x_train, x_val, y_train, y_val = train_test_split(
#         x_train_val, y_train_val, test_size=val_size/(train_size + val_size),
#         random_state=random_state, shuffle=shuffle)

#     return x_train, x_val, y_train, y_val, y_test
