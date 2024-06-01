Sure! Here’s a step-by-step guide to setting up a Python project with multiple scripts in different folders and writing unit tests for those scripts using `pytest`.

### Step 1: Set Up the Project Structure

Create a project directory with the following structure:

```
my_project/
├── src/
│   ├── __init__.py
│   ├── module1/
│   │   ├── __init__.py
│   │   └── script1.py
│   └── module2/
│       ├── __init__.py
│       └── script2.py
└── tests/
    ├── __init__.py
    ├── test_module1/
    │   ├── __init__.py
    │   └── test_script1.py
    └── test_module2/
        ├── __init__.py
        └── test_script2.py
```

### Step 2: Create Example Scripts

Create example functions in `script1.py` and `script2.py`.

**src/module1/script1.py**:
```python
# src/module1/script1.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

**src/module2/script2.py**:
```python
# src/module2/script2.py

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
```

### Step 3: Write Unit Tests

Create unit tests for the functions in `test_script1.py` and `test_script2.py`.

**tests/test_module1/test_script1.py**:
```python
# tests/test_module1/test_script1.py

import pytest
from src.module1.script1 import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
```

**tests/test_module2/test_script2.py**:
```python
# tests/test_module2/test_script2.py

import pytest
from src.module2.script2 import multiply, divide

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(1, 0)
```

### Step 4: Install `pytest`

Make sure `pytest` is installed in your environment. You can install it using pip:

```sh
pip install pytest
```

### Step 5: Run the Tests

Navigate to the `my_project` directory and run the tests using `pytest`:

```sh
cd my_project
pytest
```

This will automatically discover the tests in the `tests` directory and run them, providing you with the output of the test results.

### Summary

You now have a Python project with multiple scripts organized into different folders and unit tests for those scripts using `pytest`. This structure allows you to easily add more modules, scripts, and tests as your project grows.