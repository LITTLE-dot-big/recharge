import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import linear_model as lm
from sklearn.metrics import mean_squared_error as mse
import matplotlib.pyplot as plt

file = open('data.csv')
data1 = np.loadtxt(file, delimiter=',', dtype=np.float16)
print(data1)
label = data1[:, 0]
features = data1[:, 1:]
print(label)
print(features)
# model = tree.DecisionTreeClassifier()
model = lm.LinearRegression()
model.fit(X=features, y=label)
pdt = model.predict(features)
print(pdt)
print('MSE: ', np.sqrt(mse(pdt, label)))

plt.scatter(features[:, 1], label)
plt.plot(features[:, 1], label)
plt.scatter(features[:, 1], label)
plt.plot(features[:, 1], label)
plt.show()

while True:
    print('Enter amount of data in GB: ', end='')
    mb = int(input())
    print('Enter validity in days: ', end='')
    days = int(input())
    print('Price predicted: ', model.predict([[mb, days]])[0], end='\n')
