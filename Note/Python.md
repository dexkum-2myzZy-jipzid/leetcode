# Python



## Collections Library

Certainly! Here's a table summarizing the various collections in Python's `collections` module along with examples of how to use them:

| Collection    | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `deque`       | A double-ended queue allowing fast appends/pops from both ends. |
| `Counter`     | A dictionary subclass for counting hashable items.           |
| `OrderedDict` | A dictionary subclass that remembers the order that keys were first inserted. |
| `defaultdict` | A dictionary subclass that calls a factory function to supply missing values. |
| `namedtuple`  | A factory function for creating tuple subclasses with named fields. |
| `ChainMap`    | A class that groups multiple dictionaries into a single mapping. |

These examples illustrate the basic usage of each collection type. Each collection has additional methods and functionalities that make them suitable for specific use cases. It's always a good idea to explore the Python documentation for more detailed information and advanced use cases.



### 1. `deque`

```python
from collections import deque

# Initialize a deque with some elements
d = deque(["a", "b", "c"])

# Append elements to the right end
d.append("d")  # deque becomes ["a", "b", "c", "d"]

# Append elements to the left end
d.appendleft("0")  # deque becomes ["0", "a", "b", "c", "d"]

# Pop elements from the right
d.pop()  # returns "d", deque becomes ["0", "a", "b", "c"]

# Pop elements from the left
d.popleft()  # returns "0", deque becomes ["a", "b", "c"]
```

### 2. `Counter`

```python
from collections import Counter

# Creating a Counter from a list
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

# Count of an element
print(counter['blue'])  # Outputs: 3

# Most common element
print(counter.most_common(1))  # Outputs: [('blue', 3)]
```

### 3. `OrderedDict`

```python
from collections import OrderedDict

# Preserves the order of insertion
od = OrderedDict()
od['one'] = 1
od['two'] = 2
od['three'] = 3

# Iterating in insertion order
for key, value in od.items():
    print(key, value)
```

### 4. `defaultdict`

```python
from collections import defaultdict

# Default value for int is 0
dd = defaultdict(int)

# Incrementing a non-existing key 'a'
dd['a'] += 1  # defaultdict automatically creates key 'a' with default value 0

# Default dictionary with list
dd_list = defaultdict(list)
dd_list['key'].append(1)  # Adds 1 to the list of 'key'
```

### 5. `namedtuple`

```python
from collections import namedtuple

# Creating a namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Instantiating a Point object
p = Point(11, y=22)

# Accessing elements
print(p.x, p.y)  # Outputs: 11 22
```

### 6. `ChainMap`

```python
from collections import ChainMap

# Two separate dictionaries
dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}

# ChainMap combining both dictionaries
chain = ChainMap(dict1, dict2)

# Accessing values (looks into dict1 first, then dict2)
print(chain['three'])  # Outputs: 3
print(chain['one'])    # Outputs: 1
```

These examples demonstrate basic usage and functionality of each collection type. The `collections` module offers additional methods and features for each of these collections, which can be very useful for various programming scenarios.