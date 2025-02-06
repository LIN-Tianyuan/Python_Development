import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40], 'C': ['a', 'b', 'c', 'd']}
df = pd.DataFrame(data)

print(df)

print(df.loc[df['B'] > 15])
print(df.iloc[1:3])
df['D'] = df['A'] * 2
print(df)
df.drop(columns=['C'], inplace=True)
print(df)

print('----------')
data = {'A': [10, 20, 30], 'B': [100, 200, 300]}
df = pd.DataFrame(data, index=['x', 'y', 'z'])
print(df)
print(df.loc['x'])
print(df.iloc[0])
