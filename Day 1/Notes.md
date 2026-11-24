# **Day 1 – Python Basics**

**Today's goal:** Learn how to display output, work with strings, take user input, and change letter cases.



## **1. Print Statement**

The `print()` function is used to display output on the screen.

**Print text:**

```
print("Hello World")print("Welcome to Python")
```

Output:

```
Hello World
Welcome to Python
```

**Print numbers:**

```
print(100)print(10 + 20)print(50 - 10)print(5 * 2)
```

Output:

```
100
30
40
10
```

**Print text and numbers together:**

```
print("My age is", 21)print("My marks are", 95)
```

## **2. String Formatting**

String formatting allows you to insert variables into a string.

Using an f-string:

```
name = "Priya"age = 21print(f"My name is {name}")print(f"My age is {age}")print(f"My name is {name} and my age is {age}")
```

Output:

```
My name is Priya
My age is 21
My name is Priya and my age is 21
```

## **3. User Input**

The `input()` function is used to get information from the user.

```
name = input("Enter your name: ")print("Hello", name)
```

Example:

```
Enter your name: Priya
Hello Priya
```

**Important:** `input()` returns data as a string by default.

To accept numbers:

```
age = int(input("Enter your age: "))print(f"My age is {age}")
```

## **4. String Case Conversion**

Python provides built-in string methods to change uppercase and lowercase letters.

Assume:

```
text = "hello python world"
```

**1. capitalize()**

Converts the first character to uppercase and the remaining characters to lowercase.

```
print(text.capitalize())
```

Output: `Hello python world`

**2. upper()**

Converts all letters into uppercase.

```
print(text.upper())
```

Output: `HELLO PYTHON WORLD`

**3. lower()**

Converts all letters into lowercase.

```
text = "HELLO PYTHON WORLD"print(text.lower())
```

Output: `hello python world`

**4. swapcase()**

Converts uppercase letters into lowercase and lowercase letters into uppercase.

```
text = "Hello PYTHON"print(text.swapcase())
```

Output: `hELLO python`

**5. title()**

Converts the first letter of each word into uppercase.

```
text = "welcome to python programming"print(text.title())
```

Output: `Welcome To Python Programming`

## **5. Quick Revision**

| Method         | Purpose                             |
| -------------- | ----------------------------------- |
| `print()`      | Displays output                     |
| `input()`      | Takes user input                    |
| `capitalize()` | First character uppercase           |
| `upper()`      | All uppercase                       |
| `lower()`      | All lowercase                       |
| `swapcase()`   | Swaps letter cases                  |
| `title()`      | First letter of each word uppercase |


Day 1 – Practical Project: [Welcome Message Generator](https://github.com/Vishnupriya609/Python-From-Scratch/tree/main/Day%201/Day1-Welcome_Message_Generator)
- Create a Python program that asks the user for their details and generates a personalized welcome message.
