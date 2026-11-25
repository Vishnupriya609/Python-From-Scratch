
# Day 2 - Python Variables, Type Conversion & String Formatting

## 1. Variables

Variables are containers used to store data in Python.

Example:

```python
name = "Priya"
age = 21
height = 5.4

print(name)
print(age)
print(height)
```

### Variable Naming Conventions

**Camel Case:** First word starts with lowercase; subsequent words start with uppercase.

```python
studentName = "Priya"
firstName = "Priya"
```

**Snake Case:** Words are separated by underscores.

```python
student_name = "Priya"
first_name = "Priya"
```

Python convention: Use snake_case for variable names.

## 2. Python Data Types

A data type defines the type of value stored in a variable.

| Data Type | Description | Example |
|---|---|---|
| int | Integer numbers | 10, 25 |
| float | Decimal numbers | 10.5, 5.6 |
| complex | Complex numbers | 2+3j |
| str | Text | "Python" |
| bool | True or False | True |
| list | Ordered, mutable collection | [1, 2, 3] |
| tuple | Ordered, immutable collection | (1, 2, 3) |
| range | Sequence of numbers | range(5) |
| set | Collection of unique values | {1, 2, 3} |
| dict | Key-value pairs | {"name": "Priya"} |
| NoneType | Absence of a value | None |

### Checking Data Types

Use the `type()` function.

```python
name = "Priya"
age = 21

print(type(name))
print(type(age))
```

Output:

```text
<class 'str'>
<class 'int'>
```

## 3. Type Conversion (Type Casting)

Type conversion means converting one data type into another.

### A. Implicit Type Conversion

Python automatically converts one data type into another.

```python
a = 10
b = 5.5

result = a + b

print(result)
print(type(result))
```

Output:

```text
15.5
<class 'float'>
```

### B. Explicit Type Conversion

Manually converting one data type into another using built-in functions.

| Function | Purpose | Example |
|---|---|---|
| int() | Converts to integer | int("25") |
| float() | Converts to float | float(10) |
| str() | Converts to string | str(100) |
| bool() | Converts to boolean | bool(1) |
| list() | Converts to list | list("cat") |
| tuple() | Converts to tuple | tuple([1, 2]) |
| set() | Converts to set | set([1, 2, 2]) |
| dict() | Creates a dictionary from key-value pairs | dict([("a", 1)]) |

Example:

```python
age = "21"
age = int(age)

print(age)
print(type(age))
```

Output:

```text
21
<class 'int'>
```

### Important: String and Integer

```python
age = "12"

# Correct
my_age = int(age) + 9

print(my_age)
```

Output:

```text
21
```

Remember:

- "12" + "9" = "129" (String concatenation)
- 12 + 9 = 21 (Addition)
- "12" + 9 = TypeError

## 4. String Formatting

String formatting is used to insert variables and values into a string.

Python provides three common methods.

### A. String Concatenation (+)

Combining two or more strings using the + operator.

```python
name = "Priya"

print("Hello " + name)
```

Output:

```text
Hello Priya
```

To combine a string and an integer, use str().

```python
age = 21

print("My age is " + str(age))
```

### B. format() Method

The format() method inserts values into curly brace placeholders {}.

```python
name = "Priya"
age = 21

print("My name is {} and I am {} years old.".format(name, age))
```

Output:

```text
My name is Priya and I am 21 years old.
```

### C. f-Strings

f-strings allow variables and expressions to be inserted directly into strings.

Add the letter f before the opening quotation mark.

```python
name = "Priya"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Priya and I am 21 years old.
```

### Calculations Inside f-Strings

```python
a = 10
b = 20

print(f"The sum is {a + b}")
```

Output:

```text
The sum is 30
```

### Decimal Formatting

Use :.2f to display two digits after the decimal point.

```python
price = 99.98765

print(f"Price: {price:.2f}")
```

Output:

```text
Price: 99.99
```

### Comparison

| Method | Example |
|---|---|
| Concatenation | "Hello " + name |
| format() | "Hello {}".format(name) |
| f-string | f"Hello {name}" |

Recommended: Use f-strings for readable and convenient string formatting.

## 5. Working with Date and Time

Python provides the datetime module to work with dates and times.

### Importing datetime

```python
from datetime import datetime
```

### Getting Current Date and Time

```python
print(datetime.now())
```

### Getting Current Year

```python
current_year = datetime.now().year
print(current_year)
```

### Getting Current Month

```python
current_month = datetime.now().month
print(current_month)
```

### Getting Month Name

```python
current_month = datetime.now().strftime("%B")
print(current_month)
```

### Useful Date and Time Attributes

| Attribute | Description |
|---|---|
| .year | Current year |
| .month | Current month |
| .day | Current day |
| .hour | Current hour |
| .minute | Current minute |
| .second | Current second |

### Age Calculation

```python
from datetime import datetime

birth_year = int(input("Enter your birth year: "))

current_year = datetime.now().year

age = current_year - birth_year

print(f"You are approximately {age} years old.")
```

Note: This calculates approximate age. Exact age 

## 6. Practical Project - Personalized Greeting Program

### Project Objective

Create a Python program that collects user information and generates a personalized greeting.

