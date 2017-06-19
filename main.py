from loader import load
from sklearn import svm
import pandas as pd
import numpy as np

# Accuracy function
def accuracy(error):
    num = 0
    for item in error:
        if item == 0:
            num = num + 1
    return (num/len(error))*100

# Data Preparation
data = load()
np.random.shuffle(data)
data = pd.DataFrame(data)
y1_train = data[data.columns[1]]
y2_train = data[data.columns[14]]
data = data.drop(data.columns[[1,14]], axis=1)
x_train = data
x_train = np.array(x_train.as_matrix(), dtype=np.float64)
y1_train = np.array(y1_train.values, dtype=np.float64)
y2_train = np.array(y2_train.values, dtype=np.float64)
print x_train
print y1_train
print y2_train