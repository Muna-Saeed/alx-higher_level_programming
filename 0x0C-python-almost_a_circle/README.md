### ALX Higher Level Programming - Almost a Circle

## 0x0C. Python - Almost a circle

This directory contains the implementation of a series of Python classes for managing rectangles and squares. The project follows certain conventions:

1. **Testing:**
   - All files, classes, and methods have been unit tested using the `unittest` module.
   - Ensure PEP 8 validation for all files.

   ```bash
   guillaume@ubuntu:~/$ python3 -m unittest discover tests
   ```

2. **Base Class (models/base.py):**
   - Created a base class named `Base`.
   - Implemented a private class attribute `__nb_objects` initialized to 0.
   - Implemented a class constructor `__init__(self, id=None)`:
     - If `id` is not None, assign it to the public instance attribute `id`.
     - Otherwise, increment `__nb_objects` and assign the new value to the `id`.

   ```python
   # Example usage
   from models.base import Base

   b1 = Base()
   print(b1.id)

   b2 = Base()
   print(b2.id)

   b3 = Base()
   print(b3.id)

   b4 = Base(12)
   print(b4.id)

   b5 = Base()
   print(b5.id)
   ```

3. **First Rectangle (models/rectangle.py):**
   - Created a class `Rectangle` that inherits from `Base`.
   - Implemented private instance attributes (`__width`, `__height`, `__x`, `__y`) with public getters and setters.
   - Class constructor: `__init__(self, width, height, x=0, y=0, id=None)`.
   - Used private attributes with getters and setters to protect the attributes.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   r1 = Rectangle(10, 2)
   print(r1.id)

   r2 = Rectangle(2, 10)
   print(r2.id)

   r3 = Rectangle(10, 2, 0, 0, 12)
   print(r3.id)
   ```

4. **Validate Attributes (models/rectangle.py):**
   - Updated the `Rectangle` class to add validation to setter methods and instantiation.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   try:
       r = Rectangle(10, "2")
   except Exception as e:
       print("[{}] {}".format(e.__class__.__name__, e))

   try:
       r = Rectangle(10, 2)
       r.width = -10
   except Exception as e:
       print("[{}] {}".format(e.__class__.__name__, e))

   try:
       r = Rectangle(10, 2)
       r.x = {}
   except Exception as e:
       print("[{}] {}".format(e.__class__.__name__, e))

   try:
       r = Rectangle(10, 2, 3, -1)
   except Exception as e:
       print("[{}] {}".format(e.__class__.__name__, e))
   ```

5. **Area First (models/rectangle.py):**
   - Updated the `Rectangle` class by adding the public method `def area(self)` that returns the area value of the `Rectangle` instance.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   r1 = Rectangle(3, 2)
   print(r1.area())

   r2 = Rectangle(2, 10)
   print(r2.area())

   r3 = Rectangle(8, 7, 0, 0, 12)
   print(r3.area())
   ```

6. **Display #0 (models/rectangle.py):**
   - Updated the `Rectangle` class by adding the public method `def display(self)` that prints in stdout the `Rectangle` instance with the character '#'.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   r1 = Rectangle(4, 6)
   r1.display()

   print("---")

   r2 = Rectangle(2, 2)
   r2.display()
   ```

7. **`__str__` (models/rectangle.py):**
   - Updated the `Rectangle` class by overriding the `__str__` method to return `[Rectangle] (<id>) <x>/<y> - <width>/<height>`.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   r1 = Rectangle(4, 6, 2, 1, 12)
   print(r1)

   r2 = Rectangle(5, 5, 1)
   print(r2)
   ```

8. **Display #1 (models/rectangle.py):**
   - Updated the `Rectangle` class by improving the public method `def display(self)` to print in stdout the `Rectangle` instance with the character '#' by taking care of `x` and `y`.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   r1 = Rectangle(2, 3, 2,

 2)
   r1.display()

   print("---")

   r2 = Rectangle(3, 2, 1, 0)
   r2.display()
   ```

9. **Update `__str__` (models/rectangle.py):**
   - Updated the `__str__` method in the `Rectangle` class to return `[-] <id> <x>/<y> - <width>/<height>` for instances with `width` and `height` equal to 0.

   ```python
   # Example usage
   from models.rectangle import Rectangle

   r1 = Rectangle(0, 6)
   print(r1)

   r2 = Rectangle(5, 0)
   print(r2)

   r3 = Rectangle(0, 0)
   print(r3)
   ```

10. **Square #0 (models/square.py):**
    - Created a class `Square` that inherits from `Rectangle`.
    - Added a constructor `__init__(self, size, x=0, y=0, id=None)` with attributes `size`, `x`, `y`, and `id`.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(5)
    print(s1)
    print(s1.area())

    s2 = Square(2, 2, 2, 2)
    print(s2)
    print(s2.area())
    ```

11. **Square #1 (models/square.py):**
    - Updated the `Square` class by overriding the `__str__` method to return `[Square] (<id>) <x>/<y> - <size>`.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(5)
    print(s1)

    s2 = Square(2, 2, 2, 2)
    print(s2)
    ```

12. **Square #2 (models/square.py):**
    - Updated the `Square` class by updating the `to_dictionary` method to return the dictionary representation of a `Square`.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(10, 2, 1)
    print(s1)

    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)

    s2 = Square(1, 0, 0)
    print(s2)

    s2_dictionary = s2.to_dictionary()
    print(s2_dictionary)
    ```

13. **Square #3 (models/square.py):**
    - Updated the `Square` class by updating the `update` method to assign attributes based on the arguments passed.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(10, 2, 1)
    print(s1)

    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)

    s1.update(10, 10, 10, 10)
    print(s1)

    s2 = Square(1, 0, 0)
    print(s2)

    s2_dictionary = s2.to_dictionary()
    print(s2_dictionary)

    s2.update(**s1_dictionary)
    print(s2)
    ```

14. **Square #4 (models/square.py):**
    - Updated the `Square` class by adding a new method `def update(self, *args, **kwargs)` to assign attributes based on the arguments passed.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(10, 2, 1)
    print(s1)

    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)

    s1.update(10, 10, 10, 10)
    print(s1)

    s2 = Square(1, 0, 0)
    print(s2)

    s2_dictionary = s2.to_dictionary()
    print(s2_dictionary)

    s2.update(**s1_dictionary)
    print(s2)
    ```

15. **Square #5 (models/square.py):**
    - Updated the `Base` class to include the `to_json_string` static method.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(10, 2, 1)
    print(s1)

    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)

    s1_json = Square.to_json_string([s1_dictionary])
    print(s1_json)

    s2 = Square(1, 0, 0)
    print(s2)

    s2_dictionary = s2.to_dictionary()
    print(s2_dictionary)

    s2_json = Square.to_json_string([s2_dictionary])
    print(s2_json)
    ```

16. **Square #6 (models/square.py):**
    - Updated the `Base` class to add the `save_to_file` and `from_json_string` methods.
    - Updated the `Square` class to use these methods for serialization and deserialization.

    ```python
    # Example usage
    from models.square import Square

    s1 = Square(10, 2, 1)
    print(s1)

    s2 = Square(1, 0, 0)
    print(s2)

    Square.save_to_file([s1, s2])

    with open("Square.json", "r") as file:
        print(file.read())

    list_of_squares = Square.load_from_file()
    for square in list_of_squares:
        print(square)
    ```
