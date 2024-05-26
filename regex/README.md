Regular expressions (regex) are a powerful tool for pattern matching and text processing. Python's `re` module provides support for regular expressions.

Here's a tutorial on how to use regular expressions in Python:

### Basic Concepts

- **Pattern**: The regex pattern to search for.
- **String**: The text to search within.
- **Match**: A successful match of the pattern within the string.

### Importing the `re` Module

```python
import re
```

### Basic Functions

1. **re.match(pattern, string)**: Checks if the pattern matches at the beginning of the string.
2. **re.search(pattern, string)**: Searches for the pattern anywhere in the string.
3. **re.findall(pattern, string)**: Returns a list of all non-overlapping matches in the string.
4. **re.finditer(pattern, string)**: Returns an iterator yielding match objects for all non-overlapping matches.
5. **re.sub(pattern, repl, string)**: Replaces occurrences of the pattern in the string with `repl`.

### Basic Examples

#### 1. Matching at the Start of a String

```python
import re

pattern = r'^hello'
string = 'hello world'

match = re.match(pattern, string)
if match:
    print("Match found:", match.group())  # Output: Match found: hello
else:
    print("No match")
```

#### 2. Searching Anywhere in a String

```python
import re

pattern = r'world'
string = 'hello world'

search = re.search(pattern, string)
if search:
    print("Search found:", search.group())  # Output: Search found: world
else:
    print("No match")
```

#### 3. Finding All Matches

```python
import re

pattern = r'\d+'
string = 'There are 2 apples and 3 oranges.'

matches = re.findall(pattern, string)
print("All matches:", matches)  # Output: All matches: ['2', '3']
```

#### 4. Iterating Over Matches

```python
import re

pattern = r'\d+'
string = 'There are 2 apples and 3 oranges.'

matches = re.finditer(pattern, string)
for match in matches:
    print("Match found:", match.group())  # Output: Match found: 2
                                          #         Match found: 3
```

#### 5. Substituting Patterns

```python
import re

pattern = r'\d+'
replacement = '#'
string = 'There are 2 apples and 3 oranges.'

new_string = re.sub(pattern, replacement, string)
print("Substitution result:", new_string)  # Output: Substitution result: There are # apples and # oranges.
```

### Special Characters in Regular Expressions

- `.`: Matches any character except a newline.
- `^`: Matches the start of the string.
- `$`: Matches the end of the string.
- `*`: Matches 0 or more repetitions of the preceding pattern.
- `+`: Matches 1 or more repetitions of the preceding pattern.
- `?`: Matches 0 or 1 repetition of the preceding pattern.
- `{n}`: Matches exactly `n` repetitions of the preceding pattern.
- `{n,}`: Matches `n` or more repetitions of the preceding pattern.
- `{n,m}`: Matches between `n` and `m` repetitions of the preceding pattern.
- `[]`: Matches any one of the characters inside the brackets.
- `|`: Matches either the pattern before or the pattern after the `|`.
- `()`: Groups patterns and captures the matched text.

### Using Special Characters

#### Matching Digits and Words

```python
import re

pattern = r'\d+'  # Matches one or more digits
string = 'There are 2 apples and 3 oranges.'

matches = re.findall(pattern, string)
print("All matches:", matches)  # Output: All matches: ['2', '3']
```

#### Using Groups and Captures

```python
import re

pattern = r'(\d+) apples and (\d+) oranges'
string = 'There are 2 apples and 3 oranges.'

match = re.search(pattern, string)
if match:
    print("Apples:", match.group(1))  # Output: Apples: 2
    print("Oranges:", match.group(2))  # Output: Oranges: 3
```

#### Using Special Sequences

- `\d`: Matches any digit. Equivalent to `[0-9]`.
- `\D`: Matches any non-digit character.
- `\w`: Matches any alphanumeric character. Equivalent to `[a-zA-Z0-9_]`.
- `\W`: Matches any non-alphanumeric character.
- `\s`: Matches any whitespace character.
- `\S`: Matches any non-whitespace character.

### Example with Special Sequences

```python
import re

pattern = r'\w+'
string = 'Hello, world!'

matches = re.findall(pattern, string)
print("All matches:", matches)  # Output: All matches: ['Hello', 'world']
```

### Flags

Flags modify the behavior of the regex functions. Some common flags are:

- `re.IGNORECASE` or `re.I`: Ignore case.
- `re.MULTILINE` or `re.M`: Multi-line matching, affecting `^` and `$`.
- `re.DOTALL` or `re.S`: `.` matches any character, including newline.

### Example with Flags

```python
import re

pattern = r'^hello'
string = 'Hello world\nhello again'

match = re.search(pattern, string, re.IGNORECASE | re.MULTILINE)
if match:
    print("Match found:", match.group())  # Output: Match found: Hello
else:
    print("No match")
```

### Summary

Regular expressions in Python are a powerful tool for text processing. They allow you to search, match, and manipulate strings based on complex patterns. By understanding and utilizing the `re` module functions and regex patterns, you can perform a wide variety of text-processing tasks efficiently.