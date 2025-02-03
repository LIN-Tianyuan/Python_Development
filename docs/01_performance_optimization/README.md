# Performance optimization
1. How to perform Python code performance analysis?

Profiling tools
 - `cProfile` for **overall function performance**:
```python
import cProfile
cProfile.run('my_function()')
```
 - `line_profiler` for **per-line performance**:
```python
from line_profiler import LineProfiler
lp = LineProfiler()
lp.add_function(my_function)
lp.enable()
my_function()
lp.print_stats()
```
 - `memory_profiler` for **memory usage**:
```python
from memory_profiler import profile
@profile
def my_function():
    return [i**2 for i in range(100000)]
my_function()
```
By using these tools, we can **pinpoint the slowest parts of my code and optimize them**.

2. How does Python manage memory? How can we optimize memory usage?

- Use `__slots__`to reduce object memory footprint:
```python
class MyClass:
    __slots__ = ['name', 'age']  # Limit attributes to reduce memory footprint
    def __init__(self, name, age):
        self.name = name
        self.age = age

# For large numbers of small objects, which reduces Python's default __dict__ overhead.
```
 - Avoid large in-memory lists, use generators instead:
```python
def squares(n):
    for i in range(n):
        yield i ** 2  # The generator does not store all the data at once
lst = squares(1000000)  # O(1) memory footprint instead of O(n)

# Suitable for streaming data processing, avoiding one-time use of large amounts of memory
```
 - Manually trigger garbage collection if necessary
```python
import gc
gc.collect()  # Force garbage collection to avoid memory leaks
```
3. Cython / NumPy Acceleration
 
Why is Python slow, and how can we speed it up?

Python is **slow** because:

- It is an **interpreted language** (instead of compiled).
- It has **dynamic typing**, leading to additional runtime overhead.
- It is constrained by the **Global Interpreter Lock (GIL)**.

Optimization techniques:

Use NumPy for numerical operations (vectorization)
```python
import numpy as np
arr = np.arange(1000000)
arr = arr ** 2  # NumPy vectorization，faster than Python for-loop
```
 - NumPy calls C code directly to perform calculations, avoiding the overhead of the Python interpreter.

Use Cython for performance-critical code
```python
# example.pyx (Cython code)
cdef int square(int x):
    return x * x
```
 - Cython can convert Python code to C code for improved performance.

Use multiprocessing to bypass the GIL
```python
from multiprocessing import Pool
def square(x): return x * x
with Pool(4) as p:
    result = p.map(square, range(1000000))
```
 - For CPU-intensive tasks such as deep learning, numerical computation.
