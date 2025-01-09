 # Initialize quiz state

quiz_questions = {
    "beginner": [
        {"question": "What is the correct syntax to print a message in Python?",
         "options": ["A. echo 'Hello'", "B. printf('Hello')", "C. print('Hello')", "D. write('Hello')"],
         "answer": "C"},
        {"question": "What is a correct variable name in Python?",
         "options": ["A. 1variable", "B. variable1", "C. variable-1", "D. variable@1"],
         "answer": "B"},
        {"question": "Which of the following is a Python data type?",
         "options": ["A. list", "B. array", "C. stack", "D. queue"],
         "answer": "A"},
        {"question": "What does `len()` do in Python?",
         "options": ["A. Calculates length of a string or list", "B. Slices a list", "C. Joins strings", "D. Sorts a list"],
         "answer": "A"},
        {"question": "What is the output of `print(type(10))`?",
         "options": ["A. int", "B. float", "C. str", "D. None"],
         "answer": "A"}
    ],
    "intermediate": [
        {"question": "Which keyword is used to handle exceptions in Python?",
         "options": ["A. catch", "B. handle", "C. try", "D. except"],
         "answer": "C"},
        {"question": "What is the result of `3 == 3.0` in Python?",
         "options": ["A. True", "B. False", "C. Error", "D. None"],
         "answer": "A"},
        {"question": "Which of the following is an immutable data type?",
         "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
         "answer": "B"},
        {"question": "What does the `join()` method do?",
         "options": ["A. Joins lists", "B. Joins elements of a list into a string", "C. Combines dictionaries", "D. Concatenates two strings"],
         "answer": "B"},
        {"question": "What does `list.pop()` do?",
         "options": ["A. Removes and returns the last element of the list", "B. Removes a random element", "C. Sorts the list", "D. Reverses the list"],
         "answer": "A"}
    ],
    "advanced": [
        {"question": "What is the purpose of the `@staticmethod` decorator in Python?",
         "options": ["A. To define a method that doesn't require an instance",
                     "B. To define a method that can modify a class attribute",
                     "C. To define a method that requires an instance",
                     "D. To define a private method"],
         "answer": "A"},
        {"question": "What is the time complexity of searching for an element in a dictionary?",
         "options": ["A. O(1)", "B. O(n)", "C. O(log n)", "D. O(n^2)"],
         "answer": "A"},
        {"question": "What does the `zip()` function do in Python?",
         "options": ["A. Combines multiple iterables element-wise",
                     "B. Compresses a list",
                     "C. Converts a tuple into a dictionary",
                     "D. Creates a list of pairs from two dictionaries"],
         "answer": "A"},
        {"question": "What is the difference between `deepcopy()` and `copy()`?",
         "options": ["A. `copy()` creates a shallow copy, `deepcopy()` creates a deep copy",
                     "B. `copy()` is faster than `deepcopy()`",
                     "C. `deepcopy()` is for strings only",
                     "D"],
         "answer": "A. `copy()` creates a shallow copy, `deepcopy()` creates a deep copy"},
        {"question": "What does the `yield` keyword do?",
         "options": ["A. Returns multiple values from a function",
                     "B. Converts a function into a generator",
                     "C. Pauses a function and resumes it later",
                     "D. Both B and C"],
         "answer": "D"}
    ]
}