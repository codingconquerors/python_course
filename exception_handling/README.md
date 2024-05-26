Exception handling in Python allows you to handle errors and exceptions gracefully. This tutorial covers the basics of exception handling, including how to use try, except, else, and finally blocks, as well as how to raise exceptions and create custom exceptions.

### 1. Basics of Exception Handling

#### Try and Except

The basic syntax for exception handling in Python is the `try` and `except` blocks. The `try` block contains the code that might throw an exception, and the `except` block contains the code that runs if an exception occurs.

```python
try:
    # Code that might throw an exception
    x = 1 / 0
except ZeroDivisionError:
    # Code that runs if a ZeroDivisionError occurs
    print("Cannot divide by zero.")
```

#### Catching Specific Exceptions

You can catch specific exceptions by specifying the exception type in the `except` block.

```python
try:
    x = int("hello")
except ValueError:
    print("Invalid literal for int().")
```

#### Catching Multiple Exceptions

You can catch multiple exceptions by specifying them as a tuple in the `except` block.

```python
try:
    x = int("hello")
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")
```

### 2. Using Else and Finally

#### Else Block

The `else` block runs if no exceptions are raised in the `try` block.

```python
try:
    x = int("10")
except ValueError:
    print("Invalid literal for int().")
else:
    print("No exceptions occurred. x =", x)
```

#### Finally Block

The `finally` block runs no matter what, whether an exception occurred or not. It is typically used for cleanup actions.

```python
try:
    x = int("10")
except ValueError:
    print("Invalid literal for int().")
finally:
    print("This runs no matter what.")
```

### 3. Raising Exceptions

You can raise exceptions using the `raise` statement.

```python
def check_positive(number):
    if number < 0:
        raise ValueError("Number must be positive.")
    return number

try:
    check_positive(-10)
except ValueError as e:
    print(e)
```

### 4. Custom Exceptions

You can define your own exceptions by creating a new class that inherits from the `Exception` class.

```python
class CustomError(Exception):
    pass

def check_even(number):
    if number % 2 != 0:
        raise CustomError("Number is not even.")
    return number

try:
    check_even(3)
except CustomError as e:
    print(e)
```

### 5. Exception Hierarchy

Python exceptions are organized in a hierarchy, with the base class being `BaseException`. Most user-defined exceptions should inherit from `Exception`, which is a subclass of `BaseException`.

### 6. Best Practices

- **Be Specific with Exceptions**: Catch specific exceptions to avoid masking other errors.
- **Use Finally for Cleanup**: Use the `finally` block to release resources or perform cleanup actions.
- **Avoid Bare Except**: Avoid using a bare `except` clause as it catches all exceptions, including system-exiting ones.
- **Reraise Exceptions**: Reraise exceptions using `raise` when you need to handle an exception but also want to propagate it.

### Example Program

Here's a comprehensive example that demonstrates exception handling in a real-world scenario.

```python
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading file.")
    finally:
        print("Finished file operation.")

def process_data(data):
    try:
        # Simulating a processing error
        if not data:
            raise ValueError("Data is empty.")
        print("Processing data...")
    except ValueError as e:
        print(e)

def main():
    file_path = "example.txt"
    data = read_file(file_path)
    process_data(data)

if __name__ == "__main__":
    main()
```

In this example:
- The `read_file` function attempts to read a file and handles `FileNotFoundError` and `IOError`.
- The `process_data` function processes the data and raises a `ValueError` if the data is empty.
- The `main` function orchestrates the file reading and data processing.

By following this tutorial, you should have a good understanding of how to handle exceptions in Python, raise your own exceptions, and create custom exception classes.