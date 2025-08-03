# 🐍 PyPlayground - Comprehensive Python Learning Documentation

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org)
[![NLP](https://img.shields.io/badge/NLP-Gemini_API-green.svg)](https://ai.google.dev)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-red.svg)](https://docs.python.org/3/library/tkinter.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**The Complete Python Programming Reference & Learning Guide**

A meticulously crafted Python learning repository containing 30+ interactive Jupyter notebooks, real-world projects, and comprehensive documentation. This repository serves as both a learning resource and reference documentation for Python programming concepts from basics to advanced topics including GUI development, NLP applications, and interview preparation.

## 📝 Repository Purpose

This repository is designed to:

1. **Provide progressive learning** from foundational to advanced Python concepts
2. **Demonstrate practical applications** through real-world examples and projects
3. **Offer interactive examples** for hands-on learning
4. **Serve as a reference guide** for Python programming techniques
5. **Prepare learners for technical interviews** with comprehensive practice problems

---

## 📖 **Documentation Overview**

This documentation provides detailed coverage of every Python concept with practical examples extracted from the actual codebase. Each section includes:
- **Concept explanations** with theoretical background
- **Live code examples** from the repository
- **Practice problems** with solutions
- **Real-world applications** and use cases
- **Best practices** and coding standards

---

## 📚 **Table of Contents**

### 🔰 **Foundation Level**
- [Repository Architecture](#repository-architecture)
- [Python Fundamentals](#python-fundamentals)
- [Input/Output Operations](#inputoutput-operations)  
- [Data Types & Variables](#data-types--variables)
- [Control Structures](#control-structures)

### 🧮 **Data Structures Mastery**
- [Lists Deep Dive](#lists-deep-dive)
- [Tuples & Immutability](#tuples--immutability)  
- [Sets & Unique Collections](#sets--unique-collections)
- [Dictionaries & Key-Value Mapping](#dictionaries--key-value-mapping)
- [Data Structure Comparisons](#data-structure-comparisons)

### 🔧 **Functional Programming**
- [Functions Architecture](#functions-architecture)
- [Function Arguments & Parameters](#function-arguments--parameters)
- [Scope & Namespaces](#scope--namespaces)
- [Lambda Expressions](#lambda-expressions)
- [Higher-Order Functions](#higher-order-functions)

### 🏗️ **Object-Oriented Programming**
- [Classes & Objects](#classes--objects)
- [Encapsulation & Data Hiding](#encapsulation--data-hiding)
- [Inheritance Hierarchies](#inheritance-hierarchies)
- [Polymorphism & Abstraction](#polymorphism--abstraction)
- [Magic Methods & Operator Overloading](#magic-methods--operator-overloading)

### 🚀 **Advanced Concepts**
- [Exception Handling](#exception-handling)
- [Recursion & Algorithmic Thinking](#recursion--algorithmic-thinking)
- [Decorators & Metaprogramming](#decorators--metaprogramming)
- [Iterators & Iterator Protocol](#iterators--iterator-protocol)
- [Generators & Lazy Evaluation](#generators--lazy-evaluation)

### 💾 **File Operations & Persistence**
- [File I/O Operations](#file-io-operations)
- [JSON Data Handling](#json-data-handling)
- [Object Serialization (Pickle)](#object-serialization-pickle)
- [Context Managers](#context-managers)

### 🎯 **Real-World Applications**
- [NLP GUI Application](#nlp-gui-application)
- [Database Integration](#database-integration)
- [API Integration](#api-integration)
- [Interview Preparation](#interview-preparation)

### 🛠️ **Development Environment**
- [Setup & Installation](#setup--installation)
- [IDE Configuration](#ide-configuration)
- [Best Practices](#best-practices)
- [Contributing Guidelines](#contributing-guidelines)

---

## 🏛️ **Repository Architecture**

```
PyPlayground/                           # Root directory
│
├── 📁 Core Python Fundamentals/
│   ├── 1_basicPython.ipynb           # I/O, variables, basic operations
│   ├── 2_basicPython.ipynb           # Control structures, conditionals  
│   └── 3_basicPython.ipynb           # Loops, string manipulation
│
├── 📁 Data Structures Deep Dive/
│   ├── 4_PythonList.ipynb            # Lists: creation, methods, comprehensions
│   ├── 5_PythonList2.ipynb           # Advanced list operations
│   ├── 6_python_tuple_sets_dictionary.ipynb  # Core data structures
│   └── 7_python_tuple_sets_dictionary.ipynb  # Advanced data manipulation
│
├── 📁 Functional Programming/
│   ├── 8_functions.ipynb             # Function definition, scope, arguments
│   └── 9_taskOfFunction.ipynb        # Function exercises and applications
│
├── 📁 Object-Oriented Programming/
│   ├── 10_OOP1.ipynb                 # Classes, objects, constructors
│   ├── 11_OOP2.ipynb                 # Methods, attributes, encapsulation
│   ├── 12_OOP3.ipynb                 # Object references, static variables
│   ├── 13_OOP4.ipynb                 # Inheritance, access modifiers
│   ├── 14_OOP5.ipynb                 # Polymorphism, method overriding
│   ├── 15_OOP6.ipynb                 # Abstract classes, composition
│   └── 16_OOP_Project1.ipynb         # Complete OOP project implementation
│
├── 📁 Advanced Programming Concepts/
│   ├── 20_exception_handling.ipynb   # Error handling, custom exceptions
│   ├── 21_Recursion.ipynb            # Recursive algorithms, optimization
│   ├── 22_namespaces_decorators.ipynb # Scope, decorators, metaprogramming
│   ├── 23_Iterators.ipynb            # Iterator protocol, custom iterators
│   └── 24_generators.ipynb           # Generator functions, yield keyword
│
├── 📁 File Operations & I/O/
│   └── 19_FileHandling/
│       ├── fileHandling_1.ipynb      # File I/O, JSON, pickle operations
│       ├── demo.json                 # Sample JSON data
│       ├── person.pkl                # Serialized Python objects
│       └── sample.txt                # Text file examples
│
├── 📁 Real-World Projects/
│   └── 25_NLP_APP/                   # Complete NLP GUI Application
│       ├── app.py                    # Main application interface
│       ├── my_api.py                 # Gemini API integration
│       ├── mydb.py                   # Database operations
│       ├── requirements.txt          # Project dependencies
│       └── resources/                # Application assets
│
├── 📁 Interview & Assessment/
│   ├── 17_interview_questions.ipynb  # Technical interview questions
│   ├── 18_Interview_Questions.ipynb  # Advanced interview topics
│   ├── 26_interview_questions.ipynb  # Module system, imports
│   ├── 27_Task 10.ipynb             # Practice exercises
│   ├── 28_Task 11 FREE.ipynb        # Advanced practice problems
│   ├── 29_Task 12 FREE.ipynb        # Comprehensive assessment
│   └── 30_Practice Problem Solutions FREE.ipynb  # Solutions guide
│
├── 📁 Python Modules/
│   ├── P26module1.py                 # Custom module example
│   ├── P26module2.py                 # Module importing demonstration
│   └── __pycache__/                  # Compiled Python modules
│
└── 📁 Data & Resources/
    ├── sample.txt                    # Text processing examples
    ├── word_count.pkl                # Serialized data structures
    └── README.md                     # This comprehensive documentation
```

## 🐍 Core Python Concepts

### 1. Python Basics (`1_basicPython.ipynb` - `3_basicPython.ipynb`)

#### Variables and Data Types
Python supports various data types: integers, floats, strings, and booleans. These are dynamically typed, meaning you don't need to declare the type when creating variables.

**From the notebooks:**
```python
# Working with different data types
p = int(input("Enter amount: "))        # Integer
r = float(input("Enter rate: "))        # Float
name = "Python"                         # String
is_valid = True                         # Boolean
```

#### Input/Output Operations
Python provides built-in functions for input and output operations. The `print()` function has powerful formatting capabilities through separators and end parameters.

**From `1_basicPython.ipynb`:**
```python
# Using separator and end parameters in print()
print("Data", "Science", "Mentorship", "Program", sep='-', end='started')
print("By", "CampusX", sep='-')
# Output: Data-Science-Mentorship-Program-startedBy-CampusX
```

#### Basic Operations and Arithmetic
Python supports standard arithmetic operations and can be used for mathematical calculations.

**From `1_basicPython.ipynb`:**
```python
# Temperature conversion example
celcius = float(input("Enter temp in celcius: "))
fahrenheit = celcius * (9/5) + 32
print(fahrenheit)

# Simple interest calculation
p = int(input("Enter amount: "))
t = int(input("Enter time: "))
r = float(input("Enter rate: "))
interest = (p * t * r) / 100
print("The interest is: ", interest)
```

#### Control Structures and Conditionals
Python uses indentation to define code blocks in control structures.

**From `2_basicPython.ipynb`:**
```python
# Tax calculation based on salary slabs
if ctc < 5_00_000:
    tax_rate = 0
elif ctc <= 10_00_000:
    tax_rate = 0.10
elif ctc <= 20_00_000:
    tax_rate = 0.20
else:
    tax_rate = 0.30
```

#### Menu-Driven Programs
Python can create interactive programs that respond to user input.

**From `2_basicPython.ipynb`:**
```python
# Menu-driven unit conversion program
while True:
    print("\nMenu:")
    print("1. Convert cm to ft")
    print("2. Convert km to miles")
    print("3. Convert USD to INR")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        cm = float(input("Enter length in cm: "))
        print(f"{cm} cm is {cm_to_ft(cm):.2f} ft")
    elif choice == '2':
        km = float(input("Enter distance in km: "))
        print(f"{km} km is {km_to_miles(km):.2f} miles")
    # ...other options and logic...
```

#### Algorithm Implementation
Solving mathematical problems using Python.

**From `1_basicPython.ipynb`:**
```python
# Number swapping without temporary variable
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print(f"Value of num1 and num2 before swap-> num1={a}, num2={b}")
a = a + b
b = a - b
a = a - b
print(f"Value of Num1: {a}")
print(f"Value of num2: {b}")

# Calculate Euclidean distance
px1 = int(input("Enter x cood of 1st point: "))
py1 = int(input("Enter y cood of 1st point: "))
px2 = int(input("Enter x cood of 2nd point: "))
py2 = int(input("Enter y cood of 2nd point: "))
distance = ((px2 - px1) ** 2 + (py2 - py1) ** 2) ** 0.5
print(round(distance, 2))
```

#### Pattern Problems and Series
Python can efficiently implement mathematical sequences and patterns.

**From `2_basicPython.ipynb`:**
```python
# Fibonacci sequence implementation
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter a number: "))
fibonacci(n)
# Output for n=10: 0 1 1 2 3 5 8 13 21 34
```

### 2. Data Structures (`4_PythonList.ipynb` - `7_python_tuple_sets_dictionary.ipynb`)

#### Lists
Lists are ordered, mutable collections that can store multiple data types. They are one of the most versatile data structures in Python.

**From `4_PythonList.ipynb`:**
```python
# Creating different types of lists
L1 = []                      # Empty list
L2 = [1, 2, 3, 4, 5]         # Homogeneous list (all integers)
L3 = [1, 2.5, True, "hello"] # Heterogeneous list (mixed types)

# List manipulation methods
# Appending a single element
L = [1, 2, 3, 4, 5]
L.append(True)
print(L)  # Output: [1, 2, 3, 4, 5, True]

# Extending with multiple elements
L = [1, 2, 3, 4, 5]
L.extend([6, 7, 8])
print(L)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Inserting at specific position
L = [1, 2, 3, 4, 5]
L.insert(1, 100)
print(L)  # Output: [1, 100, 2, 3, 4, 5]

# Removing elements
L = [1, 2, 3, 4, 5]
L.remove(5)    # Remove by value
print(L)       # Output: [1, 2, 3, 4]

L = [1, 2, 3, 4, 5]
L.pop()        # Remove last item and return it
print(L)       # Output: [1, 2, 3, 4]
```

#### List Operations and Comprehensions
Python lists support arithmetic operations and powerful comprehension syntax for efficient list creation.

**From the notebooks:**
```python
# List arithmetic operations
L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]

# Concatenation
print(L1 + L2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Repetition
print(L1 * 3)   # Output: [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

# List comprehension examples
squares = [i**2 for i in range(1, 11)]
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

filtered_squares = [i**2 for i in range(1, 11) if i > 5]
# Output: [36, 49, 64, 81, 100]
```

#### Tuples
Tuples are immutable ordered sequences, offering better performance and security compared to lists.

**From `6_python_tuple_sets_dictionary.ipynb`:**
```python
# Creating tuples
t1 = ()                      # Empty tuple
t2 = ('hello',)              # Single-item tuple (note the comma)
t3 = (1, 2, 3, 4)            # Multiple items
t4 = (1, 2.5, True, [1, 2])  # Heterogeneous tuple
t5 = tuple('hello')          # Converting other types to tuple
print(t5)                    # Output: ('h', 'e', 'l', 'l', 'o')

# Tuple benefits (from performance tests)
import time, sys

L = list(range(1000))
T = tuple(range(1000))

print('List size', sys.getsizeof(L))   # Larger memory footprint
print('Tuple size', sys.getsizeof(T))  # Smaller memory footprint

# Special tuple operations
# Tuple unpacking
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3

# Extended unpacking with asterisk
a, b, *others = (1, 2, 3, 4)
print(a, b)      # Output: 1 2
print(others)    # Output: [3, 4]

# Swapping variables
a, b = 1, 2
a, b = b, a      # Tuple packing and unpacking
print(a, b)      # Output: 2 1
```

#### Sets
Sets are unordered collections of unique elements, perfect for membership testing and removing duplicates.

**From `6_python_tuple_sets_dictionary.ipynb`:**
```python
# Creating sets
s1 = set()                   # Empty set (not {} - that's an empty dict)
s2 = {1, 2, 3, 4, 5}         # Set with values
s3 = set([1, 2, 2, 3, 4])    # Creating from list, duplicates removed
print(s3)                    # Output: {1, 2, 3, 4}

# Set operations
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# Union (all elements from both sets)
print(s1 | s2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (elements common to both sets)
print(s1 & s2)  # Output: {4, 5}

# Difference (elements in s1 but not in s2)
print(s1 - s2)  # Output: {1, 2, 3}

# Symmetric difference (elements in either set but not in both)
print(s1 ^ s2)  # Output: {1, 2, 3, 6, 7, 8}

# Set comprehensions
squares_set = {i**2 for i in range(1, 11) if i > 5}
# Output: {36, 49, 64, 81, 100}
```

#### Dictionaries
Dictionaries are key-value mappings allowing fast lookups and complex data organization.

**From `6_python_tuple_sets_dictionary.ipynb`:**
```python
# Creating dictionaries
d1 = {}                                  # Empty dictionary
d2 = {'name': 'nitish', 'gender': 'male'} # Simple key-value pairs
d3 = {(1, 2, 3): 1, 'hello': 'world'}    # Mixed key types

# Nested dictionaries (JSON-like structure)
student = {
    'name': 'nitish',
    'college': 'bit',
    'sem': 4,
    'subjects': {
        'dsa': 50,
        'maths': 67,
        'english': 34
    }
}

# Dictionary from sequence
d4 = dict([('name', 'nitish'), ('age', 32), (3, 3)])

# Accessing dictionary elements
print(student['name'])        # Direct access
print(student.get('address')) # Safe access with get() - returns None if key doesn't exist
print(student.get('address', 'Not Found')) # With default value

# Dictionary operations and methods
keys = student.keys()       # Get all keys
values = student.values()   # Get all values
items = student.items()     # Get all (key, value) pairs

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 3. Functions (`8_functions.ipynb` - `9_taskOfFunction.ipynb`)

#### Function Definition and Documentation
Functions in Python are defined using the `def` keyword, and can include docstrings for documentation.

**From `8_functions.ipynb`:**
```python
def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 16th Nov 2022
  """
  if type(num) == int:
    if num % 2 == 0:
      return 'even'
    else:
      return 'odd'
  else:
    return 'pagal hai kya?'
    
# Using the function
for i in range(1, 11):
  x = is_even(i)
  print(x)
```

#### Types of Arguments
Python supports various argument types for flexible function definitions.

**From `8_functions.ipynb`:**
```python
# Default arguments
def power(a=1, b=1):
  return a**b
  
power()               # Uses defaults: a=1, b=1, returns 1
power(2, 3)           # Positional arguments: a=2, b=3, returns 8
power(b=3, a=2)       # Keyword arguments: a=2, b=3, returns 8

# Variable-length arguments (*args)
def multiply(*kwargs):
  product = 1
  for i in kwargs:
    product = product * i
  return product

multiply(1, 2, 3, 4, 5)  # Can take any number of arguments
# Output: 120

# Keyword variable-length arguments (**kwargs)
def display(**salman):
  for (key, value) in salman.items():
    print(key, '->', value)

display(india='delhi', srilanka='colombo', nepal='kathmandu')
# Output: 
# india -> delhi
# srilanka -> colombo
# nepal -> kathmandu
```

#### Variable Scope and Namespaces
Python functions create their own scope for variables, following LEGB (Local, Enclosing, Global, Built-in) rule.

**From `8_functions.ipynb`:**
```python
# Accessing global variables inside functions
def g(y):
    print(x)      # Accesses global x
    print(x + 1)  # Uses global x in calculation
x = 5
g(x)
print(x)  # Output: 5, 6, 5

# Local variables don't affect global scope
def f(y):
    x = 1        # Creates local x, doesn't affect global x
    x += 1
    print(x)     # Prints local x
x = 5
f(x)
print(x)  # Output: 2, 5
```

#### Function Return Values
Functions can return single values, multiple values, or no explicit value (returns `None`).

**Examples from the notebooks:**
```python
# Function returning multiple values
def count_case(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower  # Returns a tuple that can be unpacked
    
s = 'CampusX is an Online Mentorship Program'
upper_count, lower_count = count_case(s)
```

#### Practical Function Examples
Real-world examples of Python functions solving various problems.

**From `9_taskOfFunction.ipynb`:**
```python
# Function to return unique elements from a list
def unique(L):
    res = []
    for i in L:
        if i not in res:
            res.append(i)
    return res

L = [1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
print(unique(L))  # Output: [1, 2, 3, 4, 5, 6]

# Function to sort hyphen-separated words
def sort_sequence(seq):
    L = []
    for i in sorted(seq.split('-')):
        L.append(i)
    return "-".join(L)
    
s = "green-red-yellow-black-white"
print(sort_sequence(s))  # Output: black-green-red-white-yellow

# Function to merge multiple dictionaries
def merge_dict(*kwargs):
    d = {}
    for i in kwargs:
        d.update(i)
    return d
    
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
print(merge_dict(d1, d2, d3))
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
```

## 🏛️ Object-Oriented Programming (`10_OOP1.ipynb` - `16_OOP6.ipynb`)

### 1. Classes and Objects
Classes are blueprints for creating objects with specific attributes and behaviors.

**From `10_OOP1.ipynb`:**
```python
class Atm:
  # Constructor - automatically called when object is created
  def __init__(self):
    self.pin = ''
    self.balance = 0
    self.menu()

  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit
    """)

    if user_input == '1':
      self.create_pin()
    elif user_input == '2':
      self.change_pin()
    # other menu options...

  def create_pin(self):
    user_pin = input('enter your pin')
    self.pin = user_pin
    user_balance = int(input('enter balance'))
    self.balance = user_balance
    print('pin created successfully')
    self.menu()

  def check_balance(self):
    user_pin = input('enter your pin')
    if user_pin == self.pin:
      print('your balance is ', self.balance)
    else:
      print('chal nikal yahan se')
```

### 2. Object Attributes and References
Objects in Python are mutable by default, and reference variables point to objects in memory.

**From `12_OOP3.ipynb`:**
```python
# Reference variables and object mutability
class Person:
  def __init__(self, name, gender):
    self.name = name
    self.gender = gender

# Multiple references to the same object
p = Person('nitish', 'male')
q = p  # q now references the same object as p

print(p.name)  # Output: nitish
print(q.name)  # Output: nitish

# Changing attribute through one reference affects all references
q.name = 'ankit'
print(q.name)  # Output: ankit
print(p.name)  # Output: ankit - also changed!

# Pass by reference in functions
def greet(person):
  print(id(person))  # Same ID as the original object
  person.name = 'changed name'
  print(person.name)

p = Person('nitish', 'male')
print(id(p))
greet(p)
print(p.name)  # Output: changed name - the original object was modified
```

### 3. Class Design and Practical Applications
Python OOP enables creating complex systems with well-defined interfaces.

**From `12_OOP3.ipynb`:**
```python
class Point:
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod, self.y_cod)
    
    def euclidean_distance(self, other):
        return ((self.x_cod - other.x_cod)**2 + 
                (self.y_cod - other.y_cod)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0, 0))
    
class Line:    
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)
    
    def point_on_line(self, point):
        if self.A*point.x_cod + self.B*point.y_cod + self.C == 0:
            return 'lies on the line'
        else:
            return 'does not lie on the line'  

    def shortest_distance(self, point):
        return abs(self.A*point.x_cod + self.B*point.y_cod + self.C) / \
               ((self.A**2 + self.B**2)**0.5)
```

### 4. Static Class Variables and Methods
Python classes can have variables and methods that are shared across all instances.

**From `13_OOP4.ipynb`:**
```python
class Car:
    # Static class variable shared by all instances
    __counter = 0

    def __init__(self):
        Car.__counter += 1  # Increment counter with each new instance
        
    @staticmethod
    def get_counter():  # Static method to access the counter
        return Car.__counter
    
o1 = Car()
o2 = Car()
o3 = Car()
print(Car.get_counter())  # Output: 3
```

### 5. Class Relationships: Aggregation and Inheritance

#### Aggregation (Has-A Relationship)
When one class contains objects of another class as attributes.

**From `14_OOP5.ipynb`:**
```python
class Address:
    def __init__(self, city, pin, state):
        self.__city = city  # Private attribute
        self.pin = pin
        self.state = state
        
    def get_city(self):
        return self.__city
        
    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address  # Address object
    
    def print_address(self):
        print(f"City: {self.address.get_city()}")
        print(f"Pin: {self.address.pin}")
        print(f"State: {self.address.state}")

    def edit_profile(self, new_city, new_pin, new_state):
        self.address.edit_address(new_city, new_pin, new_state)
        print("Profile updated successfully")

# Usage
address_1 = Address("Delhi", "110001", "Delhi")
customer_1 = Customer("John", "Male", address_1)
customer_1.print_address()
```

#### Inheritance (Is-A Relationship)
When a class inherits attributes and methods from another class.

**From `14_OOP5.ipynb`:**
```python
# Parent class
class User:
    def __init__(self):
        self.name = 'Souvik'
        self.gender = 'male'

    def login(self):
        print('login')

# Child class
class Student(User):
    def enroll(self):
        print('enroll into the course')

# Usage
u = User()
s = Student()

print(s.name)  # Inherited from User class
s.login()      # Method inherited from User
s.enroll()     # Method specific to Student
```

### 6. Polymorphism and Method Overriding
Ability of objects to take different forms depending on context.

**From `15_OOP6.ipynb`:**
```python
class Vehicle:
    def __init__(self, type, capacity):
        self.type = type
        self.capacity = capacity

class Bus(Vehicle):
    def fare(self):
        # Calculate fare with maintenance charge
        base_fare = super().fare()
        bus_fare = base_fare + 0.1 * base_fare
        return bus_fare

# Polygon abstract class example
from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def get_data(self):
        pass
    
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def get_data(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b
    
class Triangle(Polygon):
    def get_data(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h

# Usage
rect = Rectangle()
rect.get_data(10, 5)
print(f"Rectangle area: {rect.area()}")  # Output: Rectangle area: 50
```

## 🚀 Advanced Topics

### 1. Exception Handling (`20_exception_handling.ipynb`)
Exception handling allows your code to gracefully handle errors during execution.

**From `20_exception_handling.ipynb`:**
```python
# Basic try-except block
try:
    with open('sample1.txt', 'r') as f:
        print(f.read())
except:
    print("File not found")

# Catching specific exceptions
try:
    m = 10
    f = open('sample1.txt', 'r')
    print(f.read())
    print(m)
    print(5/0)  # Will raise ZeroDivisionError
    L = [1, 2, 3]
    L[100]      # Will raise IndexError
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Division by zero")
except NameError:
    print('Variable is not defined')
except Exception as e:
    print("An error occurred:", e)
```

**Common Python Exceptions:**
```python
# IndexError - accessing an invalid index
L = [1, 2, 3, 4, 5]
# L[100]  # IndexError: list index out of range

# KeyError - accessing a non-existent key in dictionary
d = {'name': "Souvik"}
# d['age']  # KeyError: 'age'

# TypeError - operation between incompatible types
# 1 + 'a'  # TypeError: unsupported operand type(s)

# ValueError - inappropriate value for function argument
# int('a')  # ValueError: invalid literal for int()

# AttributeError - accessing non-existent attribute
L = [1, 2, 3]
# L.upper()  # AttributeError: 'list' object has no attribute 'upper'
```

### 2. Recursion (`21_Recursion.ipynb`)
Recursion is when a function calls itself to solve smaller instances of the same problem.

**From `21_Recursion.ipynb`:**
```python
# Recursive multiplication
def mul_rec(a, b):
    if b == 1:  # Base case
        return a
    return a + mul_rec(a, b-1)  # Recursive case

print(mul_rec(4, 5))  # Output: 20
# Execution: 4 + (4 + (4 + (4 + 4)))

# Factorial implementation
def factorial(n):
    if n == 0:  # Base case
        return 1
    return n * factorial(n-1)  # Recursive case

print(factorial(5))  # Output: 120
# 5! = 5 * 4 * 3 * 2 * 1 = 120

# Fibonacci sequence
def fibo(n):
    if n == 1 or n == 0:  # Base case
        return n
    return fibo(n-1) + fibo(n-2)  # Recursive case

print(fibo(5))  # Output: 5
# Sequence: 0, 1, 1, 2, 3, 5

# Palindrome check using recursion
def palindrome(s):
    if len(s) <= 1:  # Base case: empty string or single character
        print("Palindrome")
    else:
        if s[0] == s[-1]:  # Check first and last characters
            return palindrome(s[1:-1])  # Recursively check inner string
        else:
            print("Not a Palindrome")

palindrome("madam")  # Output: Palindrome

# Power set generation using recursion
def power_set(s, index=0, current=""):
    if index == len(s):  # Base case: reached end of string
        print(f'[{current}]', end='')
        return
    power_set(s, index+1, current)  # Exclude current character
    power_set(s, index+1, current+s[index])  # Include current character

power_set("123")  # Output: [][1][2][12][3][13][23][123]
```

### 3. Namespaces and Decorators (`22_namespaces_decorators.ipynb`)
Namespaces organize variables, while decorators modify function behavior.

**From `22_namespaces_decorators.ipynb`:**
```python
# Variable scopes
a = 2  # Global variable

def temp():
    # Local variable
    a = 3  # Different from global 'a'
    print(a)  # Accesses local 'a'

temp()  # Output: 3
print(a)  # Output: 2 (global 'a' unchanged)

# Accessing global variables
a = 2

def temp():
    global a  # Declare that we want to use global 'a'
    a += 1    # Modify global 'a'
    print(a)

temp()  # Output: 3
print(a)  # Output: 3 (global 'a' was changed)
```

### 4. Iterators and Generators
Iterators allow custom iteration logic, while generators provide memory-efficient iteration.

**From `24_generators.ipynb`:**
```python
# Creating a simple generator function
def gen_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"

# Using the generator
gen = gen_demo()
for i in gen:
    print(i)

# Generator vs return statement
def fun(n):
    for i in range(n):
        return i  # Function exits after first iteration

# Generator version
def fun_gen(n):
    for i in range(n):
        yield i  # Pauses function and returns value

# Memory efficiency demonstration
import sys

L = [x for x in range(1000)]  # List comprehension
G = (x for x in range(1000))  # Generator expression

print('List size', sys.getsizeof(L))   # Much larger memory usage
print('Generator size', sys.getsizeof(G))  # Very small memory usage
```

### 5. File Handling (`19_FileHandling/fileHandling_1.ipynb`)
Python provides versatile tools for reading, writing, and manipulating files.

**From `19_FileHandling/fileHandling_1.ipynb`:**
```python
# Basic file writing
f = open('sample.txt', 'w')
f.write("Hello Python\nHello World")
f.close()

# Reading from files
f = open('sample.txt', 'r')
content = f.read()
print(content)
f.close()

# Using context managers (with statement)
with open('sample1.txt', 'w') as f:
    f.write('I love BMW')

# Reading chunks from large files
with open('big.txt', 'r') as f:
    chunk_size = 10
    while True:
        data = f.read(chunk_size)
        if not data:
            break
        print(data, end="")

# File positioning with seek() and tell()
with open('sample1.txt', 'r') as f:
    f.seek(7)  # Move to the 8th byte position
    print(f.read())  # Read from that position
    print(f.tell())  # Current position in file

# JSON serialization
import json

# Dictionary to JSON
d1 = {
    'student': 'Souvik',
    'marks': [15, 20, 60, 89, 56]
}

with open('demo.json', 'w') as f:
    json.dump(d1, f)

# Reading JSON back
with open('demo.json', 'r') as f:
    data = json.load(f)
    print(data)

# Custom object serialization
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person('souvik', 21, 'male')

def serialize_person(person):
    if isinstance(person, Person):
        return {
            "name": person.name,
            "age": person.age,
            "gender": person.gender
        }

with open('demo2.json', 'w') as f:
    json.dump(person, f, default=serialize_person)
```

## 💼 Projects

### 1. NLP Toolkit Application (`25_NLP_APP/`)
A complete GUI application built with Tkinter for natural language processing tasks using Google's Gemini API.

#### Architecture Overview
The application is built with a clean MVC-like architecture:
- `app.py`: Main application UI and controller logic
- `my_api.py`: API integration with Gemini
- `mydb.py`: Database operations for user management

**From `25_NLP_APP/app.py`:**
```python
class NLPApp:
    def __init__(self):
        self.dbo = Database()
        
        # Load API key from environment variable
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            messagebox.showerror("❌ Configuration Error", 
                               "API key not found. Please set GEMINI_API_KEY in your .env file")
            return
        
        self.nlp = GeminiNLP(api_key)

        # Initialize UI components
        self.root = Tk()
        self.root.title("✨ NLP Toolkit")
        self.root.geometry("420x620")
        self.root.configure(bg="#1E1E2F")
        self.root.resizable(False, False)
        self.root.iconbitmap("resources/python.ico")

        self.font_heading = ("Segoe UI", 20, "bold")
        self.font_label = ("Segoe UI", 12)
        self.font_btn = ("Segoe UI", 10, "bold")

        self.login_gui()
        self.root.mainloop()
        
    # UI helper methods
    def styled_button(self, text, command, bg="#6A5ACD"):
        Button(self.root, text=text, bg=bg, fg="white", activebackground="#5A4BCF",
               activeforeground="white", font=self.font_btn, relief=FLAT,
               bd=0, width=25, height=2, command=command).pack(pady=10)
               
    # Core functionality
    def perform_sentiment_analysis(self):
        text = self.sentiment_input.get()
        result = self.nlp.analyze_sentiment(text)
        emoji = {"Positive": "😊", "Negative": "😞", "Neutral": "😐"}
        self.sentiment_result.config(text=f"{result} {emoji.get(result, '')}")
```

#### API Integration
The application uses Google's Gemini API for natural language processing tasks.

**From `25_NLP_APP/my_api.py`:**
```python
class GeminiNLP:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"
        self.headers = {
            "Content-Type": "application/json"
        }

    def analyze_sentiment(self, text):
        prompt = f"""
        You are a sentiment analysis tool. Analyze the sentiment of the following text and respond with only one word: 
        Positive, Negative, or Neutral.\n\nText: {text}
        """
        return self.call_api(prompt)

    def analyze_ner(self, text):
        prompt = f"""
        You are an NLP tool. Extract all named entities from the following text and list them with their type (e.g., PERSON, LOCATION, ORGANIZATION).
        Return the result in this format: Entity - Type.\n\nText: {text}
        """
        return self.call_api(prompt)

    def analyze_emotion(self, text):
        prompt = f"""
        You are an emotion detection tool. Identify the main emotion in the following text and return one word: Joy, Sadness, Anger, Fear, Surprise, or Disgust.
        \n\nText: {text}
        """
        return self.call_api(prompt)
```

#### Data Persistence
The application uses JSON for simple data storage and user authentication.

**From `25_NLP_APP/mydb.py`:**
```python
class Database:
    def add_data(self, name, email, password):
        with open('db.json', 'r') as rf:
            data = json.load(rf)

        if email in data:
            return 0
        else:
            data[email] = [name, password]
            with open('db.json', 'w') as wf:
                json.dump(data, wf)
            return 1
            
    def search(self, email, password):
        with open('db.json', 'r') as rf:
            database = json.load(rf)
        if email in database:
            if database[email][1] == password:
                return 1
            else:
                return 0
        else:
            return 0
```

#### Features
- **User Authentication**: Registration and login system
- **Sentiment Analysis**: Detects positive, negative, or neutral sentiment
- **Named Entity Recognition**: Identifies entities like people, places, and organizations
- **Emotion Detection**: Identifies primary emotions in text
- **Modern UI**: Responsive interface with custom styling

#### Setup Instructions
```bash
# Install dependencies
pip install -r requirements.txt

# Create .env file with your API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run the application
python app.py
```

## 🎯 Interview Preparation (`17_interview_questions.ipynb`, `18_Interview_Questions.ipynb`)

### Common Python Interview Topics:
1. **OOP Concepts**: Inheritance, polymorphism, encapsulation
2. **Data Structures**: Time complexity, use cases
3. **Memory Management**: Garbage collection, reference counting
4. **Decorators and Generators**: Advanced Python features
5. **Exception Handling**: Best practices and patterns

### Sample Interview Questions:
```python
# Q: Explain the difference between __str__ and __repr__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Q: What is multiple inheritance and MRO?
class Father:
    def show(self):
        print("Father Class Method")

class Mother:
    def show(self):
        print("Mother Class Method")

class Son(Father, Mother):  # MRO: Son -> Father -> Mother
    pass
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Git (for cloning the repository)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/iamsouvik007/PyPlayground.git
cd PyPlayground
```

2. **Create a virtual environment:**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt  # For NLP application
pip install jupyter numpy pandas matplotlib  # For notebooks
```

4. **Start Jupyter Notebook:**
```bash
jupyter notebook
```

### Environment Setup

For the NLP application, you'll need to set up the environment variables:

```bash
# Create a .env file in the 25_NLP_APP directory
cd 25_NLP_APP
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Get your API key from: https://ai.google.dev/
```

### Recommended Learning Path

Follow this structured learning path to maximize your learning experience:

#### 1. Python Fundamentals (Week 1)
- **Start with**: `1_basicPython.ipynb` to `3_basicPython.ipynb`
- **Key concepts**: Variables, data types, operators, control flow
- **Practice with**: Basic mathematical calculations and string operations
- **Example from notebooks**:
  ```python
  # Temperature converter from notebook 1
  celsius = float(input("Enter temperature in celsius: "))
  fahrenheit = celsius * (9/5) + 32
  print(f"{celsius}°C is {fahrenheit}°F")
  ```

#### 2. Data Structures (Week 2)
- **Start with**: `4_PythonList.ipynb` to `7_python_tuple_sets_dictionary.ipynb`
- **Key concepts**: Lists, tuples, sets, dictionaries, operations
- **Practice with**: Data manipulation exercises
- **Example from notebooks**:
  ```python
  # List operations
  L = [1, 2, 3, 4, 5]
  L.append(6)      # Add element
  L.extend([7, 8]) # Add multiple elements
  L.pop(2)         # Remove element at index 2
  ```

#### 3. Functional Programming (Week 3)
- **Start with**: `8_functions.ipynb` and `9_taskOfFunction.ipynb`
- **Key concepts**: Function definition, arguments, return values
- **Practice with**: Custom function implementations
- **Example from notebooks**:
  ```python
  # Function to find unique elements
  def unique(L):
      res = []
      for i in L:
          if i not in res:
              res.append(i)
      return res
  ```

#### 4. Object-Oriented Programming (Week 4-5)
- **Start with**: `10_OOP1.ipynb` to `16_OOP_Project1.ipynb`
- **Key concepts**: Classes, objects, inheritance, polymorphism
- **Practice with**: Design patterns and OOP projects
- **Example from notebooks**:
  ```python
  # Class to handle geometry
  class Point:
      def __init__(self, x, y):
          self.x_cod = x
          self.y_cod = y
          
      def distance_from_origin(self):
          return (self.x_cod**2 + self.y_cod**2)**0.5
  ```

#### 5. Advanced Python Concepts (Week 6)
- **Start with**: `20_exception_handling.ipynb` to `24_generators.ipynb`
- **Key concepts**: Exception handling, recursion, decorators, generators
- **Practice with**: Error handling and advanced function concepts
- **Example from notebooks**:
  ```python
  # Generator for Fibonacci numbers
  def fibo_generator(n):
      a, b = 0, 1
      count = 0
      while count < n:
          yield a
          a, b = b, a + b
          count += 1
  ```

#### 6. File Operations & I/O (Week 7)
- **Start with**: `19_FileHandling/fileHandling_1.ipynb`
- **Key concepts**: File operations, JSON, serialization
- **Practice with**: Data persistence exercises
- **Example from notebooks**:
  ```python
  # JSON serialization
  import json
  student_data = {'name': 'Souvik', 'marks': [85, 90, 78]}
  with open('student.json', 'w') as f:
      json.dump(student_data, f)
  ```

#### 7. Real-World Project (Week 8)
- **Start with**: `25_NLP_APP/`
- **Key concepts**: Full application development, API integration
- **Practice with**: Enhancing the NLP application

#### 8. Interview Preparation (Week 9)
- **Start with**: `17_interview_questions.ipynb`, `18_Interview_Questions.ipynb`, etc.
- **Key concepts**: Common interview problems and solutions
- **Practice with**: Coding challenges and algorithmic problems

## 📊 Key Learning Outcomes

By completing this repository, you will:

- ✅ **Master Python fundamentals**: Variables, data types, control structures
- ✅ **Understand object-oriented programming**: Classes, inheritance, encapsulation
- ✅ **Handle data structures efficiently**: Lists, dictionaries, sets
- ✅ **Apply advanced programming techniques**: Recursion, decorators, generators
- ✅ **Implement error handling**: Try-except blocks, custom exceptions
- ✅ **Manage file operations**: Reading, writing, JSON serialization
- ✅ **Build complete applications**: GUI interfaces, API integration
- ✅ **Solve complex problems**: Algorithmic thinking, optimization
- ✅ **Prepare for technical interviews**: Common questions and solutions

## 📚 Additional Resources

- [Official Python Documentation](https://docs.python.org/3/) - Comprehensive language reference
- [Real Python](https://realpython.com/) - In-depth tutorials on Python topics
- [Python Standard Library](https://docs.python.org/3/library/) - Built-in modules and functions
- [PEP 8](https://peps.python.org/pep-0008/) - Python style guide for clean code

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### How to Contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **CampusX**: For providing comprehensive Python training materials
- **Python Community**: For excellent documentation and resources
- **Contributors**: Thanks to all contributors who helped improve this repository

## 📞 Contact

- **Author**: Souvik
- **GitHub**: [@iamsouvik007](https://github.com/iamsouvik007)
- **Repository**: [PyPlayground](https://github.com/iamsouvik007/PyPlayground)

---

**Happy Learning! 🐍✨**

*This repository is continuously updated with new content and improvements. Star ⭐ the repository to stay updated with the latest changes!*
