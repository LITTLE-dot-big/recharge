import pandas as pd

data = pd.read_excel('data.xlsx', index_col=None, header=None)
print(data)
data.to_csv('data.csv', index=None, header=None)
input()