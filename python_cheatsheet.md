---
title: Python Cheatsheet
---

## [Data Structures](https://docs.python.org/3.6/tutorial/datastructures.html)

```python
# List
# mutable

[1, 2, 3]
```

```python
# Tuple
# immutable

(1, 2, 3)
```

```python
# Dict

{'a': 1, 'b': 2}
```

```python
# How to merge two dicts in Python 3.5+

>>> x = {'a': 1, 'b': 2}
>>> y = {'b': 3, 'c': 4}
>>> z = {**x, **y}
>>> z
{'c': 4, 'a': 1, 'b': 3}
```

```python
# Set
# unordered collection
# no duplicate elements

{'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
```

Note: to create an empty set you have to use `set()`, not `{}`

---

```python
# If-Else

>>> [a if a else 2 for a in [0, 1, 0, 3]]
[2, 1, 2, 3]
```


```python
# Map

>>> map(lambda x: x+1, range(10))
[1, 2, ..., 10]

# Filter
>>> filter(lambda x: x>5, range(10))
[6, 7, ..., 9]

# Reduce
from functools import reduce
>>> reduce(lambda p, x: p+x, range(10))
45
```


```python
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1
```

## Refs
https://gto76.github.io/python-cheatsheet/
https://dbader.org/blog/