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