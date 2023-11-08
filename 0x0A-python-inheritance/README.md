#0x0A. Python - Inheritance

This directory contains Python scripts and modules that demonstrate various concepts related to inheritance in Python. The tasks range from creating classes with inheritance, defining methods, and handling exceptions. Below is an overview of each task along with a brief description.

### Task 0: Lookup
- Filename: `0-lookup.py`
- Description: A Python function `lookup(obj)` is defined, which returns the list of available attributes and methods of an object. It does not require any module imports.

### Task 1: My List
- Filename: `1-my_list.py`
- Description: A Python class `MyList` is created, inheriting from the built-in `list` class. It provides a `print_sorted` method that prints the list in ascending order.

### Task 2: Exact Same Class
- Filename: `2-is_same_class.py`
- Description: A Python function `is_same_class(obj, a_class)` is defined, which returns `True` if the object is exactly an instance of the specified class, otherwise `False`.

### Task 3: Same Class or Inherit From
- Filename: `3-is_kind_of_class.py`
- Description: A Python function `is_kind_of_class(obj, a_class)` is implemented. It returns `True` if the object is an instance of, or inherits from, the specified class.

### Task 4: Only Sub Class Of
- Filename: `4-inherits_from.py`
- Description: A Python function `inherits_from(obj, a_class)` is created, which returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

### Task 5: Geometry Module
- Filename: `5-base_geometry.py`
- Description: An empty class `BaseGeometry` is defined. This task focuses on creating an empty class without any specific attributes or methods.

### Task 6: Improve Geometry
- Filename: `6-base_geometry.py`
- Description: An improved version of the `BaseGeometry` class is provided. It includes an `area` method that raises an exception with the message "area() is not implemented."

### Task 7: Integer Validator
- Filename: `7-base_geometry.py`
- Description: The `BaseGeometry` class is further enhanced by adding an `integer_validator` method. This method validates the input value, raising specific exceptions if the value is not an integer or less than or equal to 0.

### Task 8: Rectangle
- Filename: `8-rectangle.py`
- Description: A `Rectangle` class is created, inheriting from the `BaseGeometry` class. It implements instantiation with `width` and `height` attributes, which are validated as positive integers.

### Task 9: Full Rectangle
- Filename: `9-rectangle.py`
- Description: The `Rectangle` class from the previous task is extended. The `area()` method is implemented, and the class's `print()` and `str()` methods display a rectangle description.

### Task 10: Square #1
- Filename: `10-square.py`
- Description: A `Square` class is defined, inheriting from the `Rectangle` class. It implements instantiation with a `size` attribute, validated as a positive integer.

### Task 11: Square #2
- Filename: `11-square.py`
- Description: The `Square` class created in the previous task is further enhanced. The class's `print()` and `str()` methods display a square description.

### Task 12: My Integer
- Filename: `100-my_int.py`
- Description: A class `MyInt` is created, which inherits from the built-in `int` class. This class reverses the behavior of `==` and `!=` operators.

### Task 13: Can I?
- Filename: `101-add_attribute.py`
- Description: A Python function `add_attribute(obj, attr, value)` is defined. It adds a new attribute to an object if it's possible; otherwise, it raises a `TypeError` exception.

For each task, sample scripts are provided in `tests` for testing the implemented functions or classes. Simply run the respective test scripts to verify the functionality of each task.
