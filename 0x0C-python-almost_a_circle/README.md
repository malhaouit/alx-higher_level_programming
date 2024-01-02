# Python Project - Python is Almost a Circle

## Introduction

This project covers various concepts of Python, including the use of classes, constructors, getters, setters, private attributes, special methods, inheritance, JSON and many more. 

**Note:** As a student at ALX Software Engineering School, and in adherence to privacy regulations and in deference to the proprietary rights of the curriculum owner, I am unable to share all the comprehensive details about the project and each task.  
For more information, please refer to the README file inside the [repository](https://github.com/malhaouit/alx-system_engineering-devops/blob/master/README.md) of this project.

## Project Structure

This project includes 20 mandatory tasks and 2 advanced tasks.  

### Mandatory Tasks

- **Task 0:** __If it's not tested it doesn't work__

- **Task 1:** __Base class__  
	+ Files: [models/base.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py), [models/\_\_init\_\_.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/__init__.py)  

	With the file `__init__.py` the the folder `models` will become a Python package.  

	In this task a Base class will be created.  

	Inside the class Base:  
		+ create private class attribute `__nb_objects = 0`  
		+ implement a class constructor: `def __init__(self, id=None):`  

	**Note:** This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code.

- **Task 2:** __First Rectangle__  
	+ File: [models/rectangle.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)  

	Inside the file `rectangle.py`  
	+ write a class `Rectangle` that inherits from `Base`:  
	+ write private instance attributes (`__width`, `__height`, `__x`, `__y`)  
	+ each attribute has its own public getter and setter  
	+ implement a class constructor: `def __init__(self, width, height, x=0, y=0, id=None)` that calls the super class with `id`
	 
- **Task 3:** __Validate attributes__   
	+ File: The same previous file [models/rectangle.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)  

	Update the class Rectangle by adding validation of all setter methods and instantiation (`id` excluded).  

	 

- **Task 4:** `Area first`  

- **Task 5:** `Display #0`  

- **Task 6:** ` __str__`  

- **Task 7:** `Display #1`  

- **Task 8:** __Update #0__  
	+ File: [models/rectangle.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)  

	Update the class Rectangle by adding the public method `def update(self, *args):` that assigns an argument to each attribute:  
	+ 1st argument should be the `id` attribute  
	+ 2nd argument should be the `width` attribute  
	+ 3rd argument should be the `height` attribute  
	+ 4th argument should be the `x` attribute  
	+ 5th argument should be the `y` attribute  
	
	Note: Argument order is super important.

- **Task 9:** __Update #1__ 
	+ File: [models/rectangle.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py) 

	Update the class Rectangle by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:  
	+ `**kwargs` must be skipped if `*args` exists and is not empty  
	+ Each key represents an attribute to the instance  

	Note: Argument order is not important.

- **Task 10:** __And now, the Square!__  
	+ File: [models/square.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)  

	In the file `square.py`:
	+ Write a class `Square` inherits from `Rectangle`  
	+ Implement a class constructor: `def __init__(self, size, x=0, y=0, id=None):`  
	+ Use the logic of the `__init__` of the `Rectangle` class
	+ The overloading `__str__` method should return `[Square] (<id>) <x>/<y> - <size>` - in our case, `width` or `height` (in a square the width and height are equal)  
  
- **Task 11:** __Square size__  
	+ File: [models/square.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)  

	Update the class `Square` by adding the public getter and setter `size`.
	+ The setter should assign (in this order) the `width` and the `height` - with the same value  
	+ The setter should have the same value validation as the `Rectangle` for `width` and `height` - No need to change the exception error message (It should be the one from `width`)

- **Task 12:** __Square update__  
	+ File: [models/square.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)  

	Update the class `Square` by adding the public method `def update(self, *args, **kwargs)` that assigns attributes:  
	+ `**kwargs` must be skipped if `*args` exists and is not empty

- **Task 13:** __Rectangle instance to dictionary representation__  
	+ File: [models/rectangle.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/rectangle.py)  

	Update the class Rectangle by implementing the public method `def to_dictionary(self): that returns the dictionary representation of a `Rectangle`.  

- **Task 14:** __Square instance to dictionary representation__  
	+ File: [models/square.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/square.py)
	
	Update the class Square by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.

- **Task 15:** __Dictionary to JSON string__  
	+ File: [models/base.py](https://github.com/malhaouit/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/models/base.py)  

	Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`.  

- **Task 16:** `JSON string to file`  

- **Task 17:** `JSON string to dictionary`  

- **Task 18:**  `Dictionary to Instance`  

- **Task 19:** `File to instances`  

### Advanced Tasks

- **Task 20:** `JSON ok, but CSV?`  

- **Task 21:** `Let's draw it`
