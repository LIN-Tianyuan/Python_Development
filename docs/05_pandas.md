# Pandas
## 1. DataFrame manipulation
```python
import pandas as pd

# Create DataFrame
data = {'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40], 'C': ['a', 'b', 'c', 'd']}
df = pd.DataFrame(data)

"""
   A   B  C
0  1  10  a
1  2  20  b
2  3  30  c
3  4  40  d
"""

# Access to data
print(df.loc[df['B'] > 15])   # Filter by condition
"""
   A   B  C
1  2  20  b
2  3  30  c
3  4  40  d
"""
print(df.iloc[1:3])           # Filter by row number
"""
   A   B  C
1  2  20  b
2  3  30  c
"""
df['D'] = df['A'] * 2         # Add a new column
"""
   A   B  C  D
0  1  10  a  2
1  2  20  b  4
2  3  30  c  6
3  4  40  d  8
"""
df.drop(columns=['C'], inplace=True)  # Delete column
"""
   A   B  D
0  1  10  2
1  2  20  4
2  3  30  6
3  4  40  8
"""
```
How to filter out rows with `A > 2` and `B < 35`?
```python
df_filtered = df[(df['A'] > 2) & (df['B'] < 35)]
print(df_filtered)
```
How do we add a column `D = A * B` to a DataFrame?
```python
df['D'] = df['A'] * df['B']
```
What is the difference between `df.loc[]` and `df.iloc[]`?

- **`loc[]` is used for label-based indexing**.
- **`iloc[]` is used for position-based indexing**.
```python
import pandas as pd

data = {'A': [10, 20, 30], 'B': [100, 200, 300]}
df = pd.DataFrame(data, index=['x', 'y', 'z'])

# Use loc[] to access by index name
print(df.loc['x'])  # Select the row corresponding to index 'x

# Use iloc[] to access by line number
print(df.iloc[0])  # Select the data in row 0

"""
A     10
B    100
Name: x, dtype: int64
"""
```
## 2. Data Cleaning
```python
# Handle of missing values
df.fillna(0)  # Fill missing values with 0
df.dropna()   # Delete the line with the missing value

# Handle of duplicate values
df.drop_duplicates()

# data type conversion
df['A'] = df['A'].astype(float)
```
How to remove rows containing NaN in DataFrame?
```python
import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, np.nan, 8]}
df = pd.DataFrame(data)
print(df)

"""
     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  NaN
3  4.0  8.0
"""

# Remove rows containing NaN
df_cleaned = df.dropna()
print(df_cleaned)

"""
     A    B
0  1.0  5.0
3  4.0  8.0
"""

# Delete only rows with NaN in a column
df_cleaned = df.dropna(subset=['A'])
print(df_cleaned)
"""
     A    B
0  1.0  5.0
1  2.0  NaN
3  4.0  8.0
"""
```
How to delete only the rows with NaN in a particular column?
```python
df.dropna(subset=['A'])
```
How do we remove a column containing NaN?
```python
df.dropna(axis=1)
```
How do we fill in missing values with the previous value?
```python
df_filled = df.fillna(method='ffill')  # Fill with the previous value
print(df_filled)

df_filled_b = df.fillna(method='bfill')  # Fill with the latter value
print(df_filled_b)
```

How to convert a column of type `object` to `datetime`?
```python
df = pd.DataFrame({'date': ['2023-01-01', '2023/02/15', 'invalid_date']})

# Convert to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

print(df)

"""
        date
0 2023-01-01
1        NaT
2        NaT
"""
```
How do we specify the time format?
```python
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
```
How do we extract the year, month and day?
```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
```
## 3. groupby & aggregate
```python
# group by column
df.groupby('A')['B'].sum()  # Group by A and sum over B

# Multiple aggregations using agg()
df.groupby('A').agg({'B': ['sum', 'mean']})
```
How do you calculate the mean of column B for each A?
```python
import pandas as pd

data = {'A': ['x', 'y', 'x', 'y', 'z'], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Calculate the mean value of B within each A group
df_mean = df.groupby('A')['B'].mean()
print(df_mean)

"""
A
x    20.0
y    30.0
z    50.0
"""
```
How do we preserve the DataFrame structure (to avoid Series returns)?
```python
df_mean = df.groupby('A', as_index=False)['B'].mean()

"""
   A     B
0  x  20.0
1  y  30.0
2  z  50.0

"""
```
How to calculate the maximum and minimum values of column B at the same time?
```python
df_agg = df.groupby('A')['B'].agg(['max', 'min'])
print(df_agg)

"""
    max  min
A           
x    30   10
y    40   20
z    50   50
"""
```
If we want to use different aggregation methods for different columns.
```python
df_agg = df.groupby('A').agg({'B': ['max', 'min']})
print(df_agg)
```
Difference between groupby().apply() and groupby().agg()?

 - agg() is used to quickly compute aggregated values and is suitable for straightforward operations such as sum, mean, min, max.
 - apply() is good for complex operations where you can perform custom functions on each set of data, for example:
   - Returns data in a different format than agg() (e.g. DataFrame).
   - Sort within a group, transforming data, etc.
```python
df.groupby('A')['B'].agg(['sum', 'mean'])

"""
    sum  mean
A           
x    40  20.0
y    60  30.0
z    50  50.0
"""

df.groupby('A')['B'].apply(lambda x: x.max() - x.min())
"""
A
x    20
y    20
z     0
Name: B, dtype: int64
"""
```
When to use apply() instead of agg()?
 - When we need to perform custom calculations within a group, such as calculating normalized data within a group.
```python
df.groupby('A')['B'].apply(lambda x: (x - x.mean()) / x.std())
```
Why is apply() slow?
 - Because apply() requires a separate Python function for each group, and agg() is C-optimized underneath, which is faster.
## 4. Performance optimization
```python
# Vectorization (faster than apply())
df['D'] = df['A'] + df['B']   # recommended
df['D'] = df.apply(lambda row: row['A'] + row['B'], axis=1)  # slow

# itertuples() vs iterrows()
for row in df.itertuples():
    print(row.A, row.B)  # itertuples() faster
```
Why is `apply()` slow? How to optimize it?
- `apply()` **Row-by-row or column-by-column** calls Python-level functions (**interpreted language, slow**).
- Pandas'internal vectorization operations (e.g. `df['A'] + df['B']`) are optimized based on the **C language** and run faster.

How can we reduce the memory footprint of my DataFrame?
- Pandas defaults to `int64` and `float64`, which take up more memory.
- Optimization methods:
    - **Reduce data type precision** (`int64 → int32`, `float64 → float32`).
    - **Convert object type to category or datetime**.
    - **Avoid storing duplicate values (category)**.

How do we check the data type of a DataFrame?
```python
df.dtypes
```
How to optimize DataFrame quickly?
```python
df = df.convert_dtypes()
```
What is the difference between `iterrows()` and `itertuples()`?
- `iterrows()` **Returns Pandas Series** line by line, slower.
- `itertuples()` **Returns namedtuple** row by row, faster and takes less memory.
## 5. Handle large-scale data
```python
# Read large data with chunksize
import pandas as pd

chunksize = 100000  # Reads 100,000 lines at a time
for i, chunk in enumerate(pd.read_csv("large_file.csv", chunksize=chunksize)):
    print(f"Chunk {i+1}: {chunk.shape}")  # Print the number of rows and columns in each chunk

# Sample output (assuming a CSV file with 450000 rows and 5 columns):
"""
Chunk 1: (100000, 5)
Chunk 2: (100000, 5)
Chunk 3: (100000, 5)
Chunk 4: (100000, 5)
Chunk 5: (50000, 5)
"""
```
How can we be more efficient when `read_csv()`?
- **Reduce datatype footprint**: Use `dtype` to specify the appropriate datatype, avoiding the default `object` type.
- **Read only some columns**: use `usecols` to load only needed columns.
- Increases parsing speed:
    - Use `low_memory=False` to avoid `mixed dtypes` parsing errors.
    - Use `engine='c'` (C parser, faster).
- **Incremental read**: for large files, use `chunksize` for chunking.
```python
import pandas as pd

# Efficiency-enhancing read_csv()
df = pd.read_csv(
    "large_file.csv",
    dtype={'id': 'int32', 'name': 'category', 'price': 'float32'},  # 指定数据类型
    usecols=['id', 'name', 'price'],  # Read only specific columns
    engine='c',  # Use the C Parser
    low_memory=False  # Avoid mixed type parsing problems
)
```
Why does `low_memory=True` cause problems?

- Pandas will **read CSV** in chunks by default, and may parse data from the same column into different data types.
- For example, one part is a number and one part is a string, resulting in **inconsistent data types**.
- Solution: Use `low_memory=False` to let Pandas **parse the whole file at once**.

How to read only the first 1000 rows of a CSV?
```python
df = pd.read_csv("large_file.csv", nrows=1000)
print(df.shape)  # Output (1000, number of columns)
```
What if we just want to skip the first 1000 lines and start reading from 1001?
```python
df = pd.read_csv("large_file.csv", skiprows=1000)
```
Want to read only the first 5% of a CSV file?
```python
total_rows = sum(1 for _ in open("large_file.csv"))  # Get total rows
df = pd.read_csv("large_file.csv", nrows=int(total_rows * 0.05))
```
How to use `chunksize` for large files?
- `chunksize` **Incrementally reads** CSV instead of loading the whole file at once, reducing memory usage.
- Ideal for **large datasets** where data can be processed chunk by chunk to improve efficiency.

How to calculate the sum while `chunksize` is being read?
```python
total_price = 0
for chunk in pd.read_csv("large_file.csv", usecols=['price'], chunksize=100000):
    total_price += chunk['price'].sum()
print("Total Price:", total_price)
```
How to combine multiple chunks into a DataFrame?
```python
df_list = [chunk for chunk in pd.read_csv("large_file.csv", chunksize=100000)]
df = pd.concat(df_list, ignore_index=True)
```
How to filter `chunksize` reads?
```python
for chunk in pd.read_csv("large_file.csv", chunksize=100000):
    filtered_chunk = chunk[chunk['price'] > 100]  # Filtering High-Priced Goods
    print(filtered_chunk.shape)
```