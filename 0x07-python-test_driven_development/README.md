# Project Title

0x07. Python - Test-driven development

## Table of Contents

- [Project Title](#project-title)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Tests](#tests)


## Description

This project contains several tasks related to test-driven development in Python. Each task focuses on a specific concept or function. The tasks remaining to be completed are:

### 0. Add integers

In this task, you need to write a function that takes two integers as input and returns their sum. The function should have the following prototype: `def add_integer(a, b=98)`. The function should handle both positional and keyword arguments. If either of the arguments is not an integer, a `TypeError` should be raised. If the sum of the two integers exceeds the maximum value that can be represented by an integer, a `OverflowError` should be raised.

### 2. Say my name

In this task, you need to write a function that takes a string as input and prints "My name is <<name>>" where <<name>> is the provided string. The function should have the following prototype: `def say_my_name(first_name, last_name="")`. If either of the arguments is not a string, a `TypeError` should be raised.

### 3. Print square

This task involves writing a function that prints a square of a specific size made of the character '#'. The function should have the following prototype: `def print_square(size)`. The `size` parameter specifies the size of the square, which should be an integer greater than 0. If the `size` argument is not a valid integer, a `TypeError` should be raised.

### 4. Text indentation

In this task, you need to write a function that prints a text with indentation. The function should have the following prototype: `def text_indentation(text)`. The `text` parameter is a string that may contain multiple sentences separated by '.', '?' or ':'. The function should print the text with each sentence on a new line and indented with two spaces. If the `text` argument is not a string, a `TypeError` should be raised.

### 5. Max integer - Unittest

In this task, you need to write unittests for the `max_integer` function. The function finds and returns the maximum integer in a list of integers. If the list is empty, the function returns None.

To execute the unittests, follow these steps:

1. Create a new folder named `tests`.
2. Inside the `tests` folder, create a Python file named `6-max_integer_test.py`.
3. Write unittests for the `max_integer` function using the `unittest` module.
4. Save the file.
5. Open a terminal and navigate to the project directory.
6. Execute the command `python3 -m unittest tests.6-max_integer_test` to run the unittests.
7. Ensure that all tests pass.

### 6. Matrix multiplication

This task involves writing a function that multiplies two matrices. The function should meet the following requirements:

- Prototype: `def matrix_mul(m_a, m_b)`.
- The input matrices `m_a` and `m_b` must be validated with specific requirements.
- If the input is not valid, raise appropriate exceptions with specific error messages.
- You are not allowed to import any module.

### 7. Lazy matrix multiplication

In this task, you need to write a function that multiplies two matrices using the NumPy module. The function should have the following prototype: `def lazy_matrix_mul(m_a, m_b)`. The requirements and test cases are the same as in Task 6, but you should use the NumPy module for matrix multiplication.

To install the NumPy module, use the command `pip3 install numpy==1.15.0`.

### 8. CPython #3: Python Strings

The final task involves creating a function that prints Python strings. The function should have the following prototype: `void print_python_string(PyObject *p)`. It should print information about the given string object, including its type, length, and value. If the provided object is not a valid string, an error message should be printed.

Please refer to the source code file `102-python.c` for the implementation details.

## Installation

Clone the repository from GitHub:
git clone https://github.com/Muna-Saeed/alx-higher_level_programming.git
Copy

## Usage

Navigate to the project directory:

cd repository-name

Execute the Python scripts for the respective tasks:

python3 script_name.py

## Tests

To run the tests for the tasks, follow the instructions provided in each task description.
