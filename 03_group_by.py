import pandas as pd

data = {'A': ['x', 'y', 'x', 'y', 'z'], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Calculate the mean value of B within each A group
df_mean = df.groupby('A')['B'].mean()
print(df_mean)


df_agg = df.groupby('A')['B'].agg(['max', 'min'])
print(df_agg)