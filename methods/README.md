Certainly! Here’s a tutorial on methods in Python, covering both instance methods and class methods, with examples.

### What is a Method?

In Python, a method is a function that is associated with an object. Methods are defined inside a class body and are used to perform operations using the attributes of that class. Methods are categorized into instance methods, class methods, and static methods.

### 1. Instance Methods

Instance methods are functions defined inside a class that operates on instances of the class. They can access and modify the object state. The first parameter of an instance method is always `self`, which refers to the instance calling the method.

#### Example of Instance Method:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")

    def get_age(self):
        return self.age

# Creating an instance of Dog
my_dog = Dog("Rex", 5)

# Calling instance methods
my_dog.bark()  # Output: Rex is barking.
print(my_dog.get_age())  # Output: 5
```
#### More about instance methods:

Instance methods in Python can modify the state of an object by accessing and modifying the instance variables (attributes) of that object. These instance variables are typically defined in the `__init__` method of the class, which serves as the constructor. Instance methods use the `self` keyword to refer to the instance on which they are called, allowing them to read and write the attributes of that instance.

Here's a detailed explanation with examples:

### Example Class with Instance Methods

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# Creating an instance of Dog
my_dog = Dog("Rex", 5)

# Calling instance methods to modify the object's state
my_dog.bark()              # Output: Rex is barking.
print(my_dog.get_age())    # Output: 5

my_dog.set_age(6)          # Modifying the age attribute
print(my_dog.get_age())    # Output: 6

my_dog.birthday()          # Output: Happy Birthday Rex! You are now 7 years old.
print(my_dog.get_age())    # Output: 7
```

### How Instance Methods Modify Object State

1. **Accessing Instance Variables**:
    - Instance methods can access the instance variables through the `self` keyword.
    - In the `get_age` method, `self.age` is used to return the current age of the dog.

2. **Modifying Instance Variables**:
    - Instance methods can modify instance variables, which in turn changes the state of the object.
    - In the `set_age` method, `self.age = new_age` sets the age attribute to a new value.
    - In the `birthday` method, `self.age += 1` increments the age attribute by 1.

3. **Performing Actions Based on Instance Variables**:
    - Instance methods can perform actions that depend on the state of the instance variables.
    - The `bark` method prints a message that includes the dog's name.

### Detailed Example

Here's a more detailed example with additional instance methods:

```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and <= current balance")

    def get_balance(self):
        return self.balance

# Creating an instance of BankAccount
account = BankAccount("Alice", 1000.0)

# Using instance methods to modify object state
account.deposit(500.0)          # Output: Deposited 500.0. New balance: 1500.0
account.withdraw(200.0)         # Output: Withdrew 200.0. New balance: 1300.0
print(account.get_balance())    # Output: 1300.0
```

### Key Points

- **Instance Methods**: These methods operate on an instance of the class and can access or modify the object's state via the `self` parameter.
- **Modifying State**: Methods like `set_age` and `birthday` in the `Dog` class or `deposit` and `withdraw` in the `BankAccount` class demonstrate how to change the instance variables.
- **Accessing State**: Methods like `get_age` and `get_balance` return the current state of the object's attributes.

Instance methods provide a way to encapsulate the behavior that acts on the data (attributes) of objects, promoting a clear and organized structure in your code.

### 2. Class Methods

Class methods are methods that are bound to the class and not the instance of the class. They can modify the class state that applies across all instances of the class. To define a class method, use the `@classmethod` decorator, and the first parameter is `cls`, which refers to the class itself.

#### Example of Class Method:

```python
class Dog:
    species = "Canis lupus"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        return cls.species

# Calling a class method
print(Dog.get_species())  # Output: Canis lupus
```

### 3. Static Methods

Static methods do not access or modify the class state. They are utility-type methods that perform a task in isolation. To define a static method, use the `@staticmethod` decorator.

#### Example of Static Method:

```python
class Dog:
    @staticmethod
    def is_adult(age):
        return age >= 3

# Calling a static method
print(Dog.is_adult(5))  # Output: True
print(Dog.is_adult(2))  # Output: False
```

### Putting It All Together

Here’s a class that uses instance methods, class methods, and static methods together:

```python
class Dog:
    species = "Canis lupus"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")

    def get_age(self):
        return self.age

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def is_adult(age):
        return age >= 3

# Creating an instance of Dog
my_dog = Dog("Rex", 5)

# Calling instance methods
my_dog.bark()  # Output: Rex is barking.
print(my_dog.get_age())  # Output: 5

# Calling a class method
print(Dog.get_species())  # Output: Canis lupus

# Calling a static method
print(Dog.is_adult(5))  # Output: True
print(Dog.is_adult(2))  # Output: False
```

### Summary

- **Instance Methods**: Operate on instances of the class and can modify object state. The first parameter is `self`.
- **Class Methods**: Operate on the class itself and can modify class state. The first parameter is `cls`. Use the `@classmethod` decorator.
- **Static Methods**: Utility methods that perform tasks in isolation. Use the `@staticmethod` decorator.

This tutorial provides a foundational understanding of methods in Python, showcasing how to define and use instance methods, class methods, and static methods within a class.