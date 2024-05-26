Certainly! Here's a tutorial on Python data types, covering the most commonly used types with examples and explanations.

## Python Data Types Tutorial

Python has several built-in data types. These can be classified into different categories such as numeric, sequence, set, and mapping types.

### 1. Numeric Types
Python supports three types of numeric data: integers, floats, and complex numbers.

#### Integers
Integers are whole numbers, positive or negative, without decimals.

```python
x = 10
y = -3
print(type(x))  # <class 'int'>
print(type(y))  # <class 'int'>
```

#### Floats
Floats are numbers with a decimal point.

```python
a = 10.5
b = -3.14
print(type(a))  # <class 'float'>
print(type(b))  # <class 'float'>
```

### 2. Sequence Types
Sequence types include strings, lists, and tuples.

#### Strings
Strings are sequences of characters.

```python
greeting = "Hello, World!"
print(greeting)       # Hello, World!
print(greeting[0])    # H
print(greeting[7:12]) # World
print(type(greeting)) # <class 'str'>
```

#### Lists
Lists are ordered collections of items, which can be of different types.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)         # ['apple', 'banana', 'cherry']
print(fruits[1])      # banana
fruits.append("date")
print(fruits)         # ['apple', 'banana', 'cherry', 'date']
print(type(fruits))   # <class 'list'>
```

#### Tuples
Tuples are similar to lists but are immutable (cannot be changed).

```python
coordinates = (10.0, 20.0)
print(coordinates)         # (10.0, 20.0)
print(coordinates[0])      # 10.0
# coordinates[0] = 15.0   # This would raise an error
print(type(coordinates))   # <class 'tuple'>
```

### 3. Set Types
Sets are unordered collections of unique items.

```python
unique_numbers = {1, 2, 3, 4, 4, 5}
print(unique_numbers)     # {1, 2, 3, 4, 5}
unique_numbers.add(6)
print(unique_numbers)     # {1, 2, 3, 4, 5, 6}
print(type(unique_numbers))  # <class 'set'>
```

### 4. Mapping Types
The most commonly used mapping type is the dictionary.

#### Dictionaries
Dictionaries are collections of key-value pairs.

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)             # {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(person["name"])     # Alice
person["email"] = "alice@example.com"
print(person)             # {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
print(type(person))       # <class 'dict'>
```

### 5. Boolean Type
Booleans represent one of two values: `True` or `False`.

```python
is_active = True
is_deleted = False
print(is_active)       # True
print(is_deleted)      # False
print(type(is_active)) # <class 'bool'>
```

### 6. None Type
The `None` type represents the absence of a value or a null value.

```python
nothing = None
print(nothing)         # None
print(type(nothing))   # <class 'NoneType'>
```

### Examples and Usage

#### Arithmetic Operations
Numeric types support arithmetic operations.

```python
x = 10
y = 3
print(x + y)  # 13
print(x - y)  # 7
print(x * y)  # 30
print(x / y)  # 3.3333333333333335
print(x // y) # 3 (Floor division)
print(x % y)  # 1 (Modulus)
print(x ** y) # 1000 (Exponentiation)
```

#### List Operations
Lists support various operations like indexing, slicing, and methods like `append()`, `remove()`, and `sort()`.

```python
numbers = [5, 3, 9, 1]
print(numbers[0])     # 5
print(numbers[1:3])   # [3, 9]
numbers.append(4)
print(numbers)        # [5, 3, 9, 1, 4]
numbers.remove(3)
print(numbers)        # [5, 9, 1, 4]
numbers.sort()
print(numbers)        # [1, 4, 5, 9]
```

#### Dictionary Operations
Dictionaries support operations like adding, removing, and accessing key-value pairs.

```python
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}
print(car["brand"])        # Toyota
car["year"] = 2021
print(car)                 # {'brand': 'Toyota', 'model': 'Corolla', 'year': 2021}
car.pop("model")
print(car)                 # {'brand': 'Toyota', 'year': 2021}
```

This tutorial covers the basic data types in Python, along with examples and common operations. Understanding these data types and how to manipulate them is fundamental to programming in Python.