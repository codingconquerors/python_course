x = 10
y = -3

print(type(x))
print(x)

z = 13.23
print(type(z))
print(z)

greeting = "Hello, World!"
print(greeting)       # Hello, World!
print(greeting[0])    # H
print(greeting[7:12]) # World
print(type(greeting)) # <class 'str'>

fruits = ["apple", "banana", "cherry"]
print(fruits)         # ['apple', 'banana', 'cherry']
print(fruits[1])      # banana returns 2nd element since they index starts with the 0th element
fruits.append("date")
fruits.reverse()
print(fruits)         # ['apple', 'banana', 'cherry', 'date']
print(type(fruits))   # <class 'list'>

coordinates = (10.0, 20.0)
print(coordinates)         # (10.0, 20.0)
print(coordinates[0])      # 10.0
# coordinates[0] = 15.0   # This would raise an error
print(type(coordinates))   # <class 'tuple'>

#set
unique_numbers = {11, 2, 3, 4, 14, 5}
print(unique_numbers)     # {1, 2, 3, 4, 5}
unique_numbers.add(6) # press control + tab
print(unique_numbers)     # {1, 2, 3, 4, 5, 6}
print(type(unique_numbers))  # <class 'set'>

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(person)             # {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(person["name"])     # Alice
person["email"] = "alice@example.com"
print(person.items())             # {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}
print(type(person))       # <class 'dict'>


is_active = True
is_deleted = False
print(is_active)       # True
print(is_deleted)      # False
print(type(is_active)) # <class 'bool'>

nothing = None
print(nothing)         # None
print(type(nothing))   # <class 'NoneType'>