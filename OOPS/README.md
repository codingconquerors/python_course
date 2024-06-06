Object-Oriented Programming (OOP) in Python is a paradigm that uses objects and classes to structure software in a way that models real-world entities. Here are the main OOP concepts with examples in Python:

### 1. Classes and Objects

**Class**: A blueprint for creating objects.
**Object**: An instance of a class.

#### Example:

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Daisy", 5)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
dog1.bark()       # Output: Buddy says woof!
```

### 2. Inheritance

Inheritance allows a class to inherit attributes and methods from another class.

#### Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says woof!
print(cat.speak())  # Output: Whiskers says meow!
```

### 3. Encapsulation

Encapsulation restricts access to some of an object's components, which can prevent the accidental modification of data.

#### Example:

```python
class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

car = Car("Toyota", 2020)
print(car.get_model())  # Output: Toyota
car.set_model("Honda")
print(car.get_model())  # Output: Honda
```

### 4. Polymorphism

Polymorphism allows different classes to be treated as instances of the same class through a common interface.

#### Example:

```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        print("Ostrich can't fly")

def let_it_fly(bird):
    bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

let_it_fly(sparrow)  # Output: Sparrow is flying
let_it_fly(ostrich)  # Output: Ostrich can't fly
```

### 5. Abstraction

Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.

#### Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 7)
print(rect.area())      # Output: 28
print(rect.perimeter()) # Output: 22
```

### Summary

These examples illustrate the fundamental OOP concepts:

1. **Classes and Objects**: Define and create instances.
2. **Inheritance**: Create a class that inherits from another class.
3. **Encapsulation**: Restrict access to certain components.
4. **Polymorphism**: Define methods in different classes with the same name.
5. **Abstraction**: Use abstract classes and methods to define interfaces.

Using these principles, you can create robust and reusable code structures that model real-world entities and relationships effectively.