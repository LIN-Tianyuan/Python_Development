import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)

# Remove rows containing NaN
df_cleaned = df.dropna()
print(df_cleaned)

# Delete only rows with NaN in a column
df_cleaned = df.dropna(subset=['A'])
print(df_cleaned)

df = pd.DataFrame({'date': ['2023-01-01', '2023/02/15', 'invalid_date']})

# Convert to datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
print(df)
