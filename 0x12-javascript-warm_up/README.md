## README.md Tasks

### Project: 0x12-javascript-warm_up

#### Task 0: First constant, first print
- File: `0-javascript_is_amazing.js`
- Description:
  - Create a constant variable called `myVar` with the value "JavaScript is amazing".
  - Use `console.log(...)` to print the output.
  - Do not use `var`.
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./0-javascript_is_amazing.js 
  JavaScript is amazing
  ```

#### Task 1: 3 languages
- File: `1-multi_languages.js`
- Description:
  - Write a script that prints three lines:
    1. "C is fun"
    2. "Python is cool"
    3. "JavaScript is amazing"
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./1-multi_languages.js 
  C is fun
  Python is cool
  JavaScript is amazing
  ```

#### Task 2: Arguments
- File: `2-arguments.js`
- Description:
  - Write a script that prints a message depending on the number of arguments passed:
    - If no arguments are passed, print "No argument".
    - If only one argument is passed, print "Argument found".
    - Otherwise, print "Arguments found".
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
  - Reference: `process.argv`
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./2-arguments.js 
  No argument
  guillaume@ubuntu:~/0x12$ ./2-arguments.js Best
  Argument found
  guillaume@ubuntu:~/0x12$ ./2-arguments.js Best School
  Arguments found
  ```

#### Task 3: Value of my argument
- File: `3-value_argument.js`
- Description:
  - Write a script that prints the first argument passed to it:
    - If no arguments are passed, print "No argument".
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
  - Do not use `length`.
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./3-value_argument.js 
  No argument
  guillaume@ubuntu:~/0x12$ ./3-value_argument.js School
  School
  ```

#### Task 4: Create a sentence
- File: `4-concat.js`
- Description:
  - Write a script that prints two arguments passed to it in the format: " is ".
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./4-concat.js c cool
  c is cool
  guillaume@ubuntu:~/0x12$ ./4-concat.js c 
  c is undefined
  guillaume@ubuntu:~/0x12$ ./4-concat.js
  undefined is undefined
  ```

#### Task 5: An Integer
- File: `5-to_integer.js`
- Description:
  - Write a script that prints "My number: " followed by the first argument converted to an integer.
  - If the argument can't be converted to an integer, print "Not a number".
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
  - Do not use `try/catch`.
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./5-to_integer.js 
  Not a number
  guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89
  My number: 89
  guillaume@ubuntu:~/0x12$ ./5-to_integer.js "89"
  My number: 89
  guillaume@ubuntu:~/0x12$ ./5-to_integer.js 89.89
  My number: 89
  guillaume@ubuntu:~/0x12$ ./5-to_integer.js School
  Not a number
  ```

#### Task 6: Loop to languages
- File: `6-multi_languages_loop.js`
- Description:
  - Write a script that prints three lines (like `1-multi_languages.js`) but using an array of strings and a loop.
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
  - Do not use any if/else statement.
  - Use only one `console.log`.
  - Use a loop (while, for, etc.).
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./6-multi_languages_loop.js 
  C is fun
  Python is cool
  JavaScript is amazing
  ```

#### Task 7: I love C
- File: `7-multi_c.js`
- Description:
  - Write a script that prints "C is fun" `x` times, where `x` is the first argument.
  - If the first argument can't be converted to an integer, print "Missing number of occurrences".
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
  - Use only two `console.log`.
  - Use a loop (while, for, etc.).
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./7-multi_c.js 2
  C is fun
  C is fun
  guillaume@ubuntu:~/0x12$ ./7-multi_c.js 5
  C is fun
  C is fun
  C is fun
  C is fun
  C is fun
  guillaume@ubuntu:~/0x12$ ./7-multi_c.js 
  Missing number of occurrences
  guillaume@ubuntu:~/0x12$ ./7-multi_c.js -3
  guillaume@ubuntu:~/0x12$
  ```

#### Task 8: Square
- File: `8-square.js`
- Description:
  - Write a script that prints a square using the character 'X'.
  - The first argument is the size of the square.
  - If the first argument can't be converted to an integer, print "Missing size".
  - You must use the character 'X' to print the square.
  - Use `console.log(...)` to print all output.
  - Do not use `var`.
  - Use a loop (while, for, etc.).
- Example:
  ```bash
  guillaume@ubuntu:~/0x12$ ./8-square.js
  Missing size
  guillaume@ubuntu:~/0x12$ ./8-square.js School
  Missing size
  guillaume@ubuntu:~/0x12$ ./8-square.js 2
  XX
  XX
  guillaume@ubuntu:~/0x12$ ./
