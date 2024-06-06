from typing import Optional

class Dog:
    def __init__(self, name: str, age: Optional[int] = None):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Daisy")

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog1.age)   # Output: 3
print(dog2.name)  # Output: Daisy
print(dog2.age)   # Output: None
dog1.bark()       # Output: Buddy says woof!
dog2.bark()       # Output: Daisy says woof!
