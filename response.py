# Predefined responses
predefined_responses = {
    "hi": "Hello! How can I assist you with Python today?",
    "what is a variable": "A variable is a named reference to a value. Example:\n```python\nx = 5\nprint(x)  # Output: 5\n```",
    "path": (
        "To learn Python step-by-step:\n"
        "1. Install Python.\n"
        "2. Learn basic syntax: variables, data types, and operators.\n"
        "3. Practice control structures: loops and if-else statements.\n"
        "4. Explore Python data structures.\n"
        "5. Learn functions and error handling."
    ),
    "indentation error example": (
        "An IndentationError occurs when your code is not properly indented. Example:\n"
        "```python\n"
        "if True:\nprint('Hello')  # IndentationError\n```\n"
        "Correct it like this:\n"
        "```python\n"
        "if True:\n    print('Hello')\n```"
    ),
    "bubble sort example": (
        "Bubble sort is a simple comparison-based sorting algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.\n\n"
        "Example:\n"
        "```python\n"
        "def bubble_sort(arr):\n"
        "    n = len(arr)\n"
        "    for i in range(n):\n"
        "        for j in range(0, n-i-1):\n"
        "            if arr[j] > arr[j+1]:\n"
        "                arr[j], arr[j+1] = arr[j+1], arr[j]\n"
        "    return arr\n\n"
        "# Test the function\n"
        "arr = [64, 34, 25, 12, 22, 11, 90]\n"
        "print('Sorted array:', bubble_sort(arr))\n"
        "```\n"
        "This code implements bubble sort and sorts the array."
    ),
    "count characters": (
        "To count the characters in a word in Python, you can use the `len()` function. This function returns the length of a string, which is the number of characters it contains.\n\n"
        "Example:\n"
        "```python\n"
        "word = 'Python'\n"
        "char_count = len(word)\n"
        "print(f'The word {word} has {char_count} characters.')\n"
        "```\n"
        "This code counts the characters in the word 'Python' and prints the result."
    ),
    "product": (
        "To find the product of two numbers in Python, you can use the multiplication operator (`*`).\n\n"
        "Example:\n"
        "```python\n"
        "a = 5\n"
        "b = 3\n"
        "product = a * b\n"
        "print(f'The product of {a} and {b} is {product}')\n"
        "```\n"
        "This code multiplies two numbers and prints the result."
    ),
    "factorial": (
        "To find the factorial of a number in Python, you can use a recursive function or a loop.\n\n"
        "Example:\n"
        "```python\n"
        "def factorial(n):\n"
        "    if n == 0 or n == 1:\n"
        "        return 1\n"
        "    else:\n"
        "        return n * factorial(n-1)\n\n"
        "# Test the function\n"
        "num = 5\n"
        "print(f'The factorial of {num} is {factorial(num)}')\n"
        "```\n"
        "This code calculates the factorial of a given number recursively."
    ),
    "fibonacci": (
        "To find the Fibonacci series in Python, you can use a loop or recursion.\n\n"
        "Example:\n"
        "```python\n"
        "def fibonacci(n):\n"
        "    fib_sequence = [0, 1]\n"
        "    for i in range(2, n):\n"
        "        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])\n"
        "    return fib_sequence\n\n"
        "# Test the function\n"
        "num = 10\n"
        "print(f'The first {num} Fibonacci numbers are: {fibonacci(num)}')\n"
        "```\n"
        "This code generates the first `n` numbers in the Fibonacci series."
    ),
    "if-else": (
        "The if-else statement is used for decision-making in Python. It allows the program to execute one block of code if a condition is true, and another block if it is false.\n\n"
        "Example:\n"
        "```python\n"
        "num = 10\n"
        "if num % 2 == 0:\n"
        "    print('Even number')\n"
        "else:\n"
        "    print('Odd number')\n"
        "```\n"
        "This code checks if a number is even or odd and prints the result."
    ),
    "if else": (
        "The if-else statement is used for decision-making in Python. It allows the program to execute one block of code if a condition is true, and another block if it is false.\n\n"
        "Example:\n"
        "```python\n"
        "num = 10\n"
        "if num % 2 == 0:\n"
        "    print('Even number')\n"
        "else:\n"
        "    print('Odd number')\n"
        "```\n"
        "This code checks if a number is even or odd and prints the result."
    ),
    "what is shallow copy": (
        "A shallow copy creates a new object but references the same nested objects as the original. Changes to nested objects in the copied object will affect the original.\n\n"
        "Example:\n"
        "```python\n"
        "import copy\n"
        "original = [[1, 2, 3], [4, 5, 6]]\n"
        "shallow = copy.copy(original)\n"
        "shallow[0][0] = 100\n"
        "print('Original:', original)  # Nested list is affected\n"
        "print('Shallow:', shallow)\n"
        "```\n"
        "This code demonstrates how modifying a shallow copy affects the original object's nested elements."
    ),
    "difference between deep and shallow copy": (
        "In Python, a shallow copy creates a new object, but nested objects are shared between the copy and the original. "
        "A deep copy creates a new object and recursively copies all nested objects, ensuring complete independence.\n\n"
        "Example:\n"
        "```python\n"
        "import copy\n"
        "original = [[1, 2], [3, 4]]\n"
        "shallow = copy.copy(original)\n"
        "deep = copy.deepcopy(original)\n"
        "shallow[0][0] = 100  # Affects original\n"
        "deep[0][0] = 200  # Does not affect original\n"
        "```\n"
    ),
    "python libraries": (
        "Python libraries are collections of pre-written code that simplify tasks. Popular libraries include NumPy (numerical computing), Pandas (data analysis), "
        "and Matplotlib (data visualization). Example:\n\n"
        "```python\n"
        "import pandas as pd\n"
        "data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}\n"
        "df = pd.DataFrame(data)\n"
        "print(df)\n"
        "```\n"
        "This creates and displays a simple data table using Pandas."
    ),
    "can you provide a simple python code": (
        "Sure! Here's a simple Python code to calculate the factorial of a number:\n\n"
        "```python\n"
        "def factorial(n):\n"
        "    if n == 0 or n == 1:\n"
        "        return 1\n"
        "    else:\n"
        "        return n * factorial(n-1)\n\n"
        "# Test the function\n"
        "num = 5\n"
        "print(f'The factorial of {num} is {factorial(num)}')\n"
        "```\n"
    ),
    "explain ai": (
        "Artificial Intelligence (AI) refers to the simulation of human intelligence by machines, allowing them to perform tasks like problem-solving, decision-making, and learning."
    ),
    "datatypes examples": (
        "Sure! In Python, data types are known as classes. Here are some common data types with examples:\n\n"
        "- **Integer (`int`)**:\n"
        "   ```python\n"
        "   num = 10\n"
        "   print(type(num))  # Output: <class 'int'>\n"
        "   ```\n\n"
        "- **String (`str`)**:\n"
        "   ```python\n"
        "   text = 'Hello, World!'\n"
        "   print(type(text))  # Output: <class 'str'>\n"
        "   ```\n\n"
        "- **List (`list`)**:\n"
        "   ```python\n"
        "   items = [1, 2, 3]\n"
        "   print(type(items))  # Output: <class 'list'>\n"
        "   ```"
    ),
    "for loop": (
        "A `for` loop in Python is used to iterate over a sequence and execute a block of code for each item.\n\n"
        "Example:\n"
        "```python\n"
        "fruits = ['apple', 'banana', 'cherry']\n"
        "for fruit in fruits:\n"
        "    print(fruit)\n"
        "```\n"
        "This code prints each fruit from the list."
    ),
    "add": (
        "To add two numbers in Python, you can use the `+` operator.\n\n"
        "Example:\n"
        "```python\n"
        "a = 5\n"
        "b = 3\n"
        "result = a + b\n"
        "print(f'The sum of {a} and {b} is {result}')\n"
        "```\n"
        "This code adds two numbers and prints the result."
    ),
    "how to read a string": (
        "To read a string in Python, you can use the `input()` function. This function takes user input and returns it as a string.\n\n"
        "Example:\n"
        "```python\n"
        "name = input('Enter your name: ')\n"
        "print(f'Hello, {name}!')\n"
        "```\n"
        "This code asks the user to enter their name and then prints a greeting message."
    )

}
