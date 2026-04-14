# Classes
A class in Python is a blueprint for creating objects.It is used to define attributes (data) and methods (functions) that describe the behavior of an object.

# Syntax
```
class ClassName:
    def __init__(self, parameters):
        self.variable = parameters

    def method_name(self):
        # code here
```
# Inheritence
Inheritance in Python is an Object-Oriented Programming (OOP) concept in which a new class (child/derived class) acquires the properties (variables) and behaviors (methods) of an existing class (parent/base class).
It promotes code reusability, modularity, and helps in building a hierarchical relationship between classes.

# Key Points
- Parent Class / Base Class: Jis class se properties inherit hoti hain
- Child Class / Derived Class: Jo class inherit karti hai

# Syntax
```
class ParentClass:
    body of parent class  # attributes and methods
class ChildClass(ParentClass):
    body of child class   # additional attributes and methods
```
# Single inheritance class
Single inheritance means one child class inherits from only one parent class
```
class Parent:
    # Parent class code
    def parent_method(self):
        pass

class Child(Parent):   # Inheriting from one parent
    # Child class code
    def child_method(self):
        pass
```
# Multiple Inhertance
Multiple inheritance means one child class inherits from more than one parent class.

# syntax
```
class Parent1:
    def method1(self):
        pass

class Parent2:
    def method2(self):
        pass

class Child(Parent1, Parent2):   # Inheriting from multiple parents
    def method3(self):
        pass
```
# Multilevel inheritance
Multilevel inheritance means a class inherits from a class, which itself inherits from another class.

### Simple chain:
Grandparent → Parent → Child
### Example
Grandfather → Father → Son
(Son indirectly inherits from Grandfather too)

# Syntax
```
class Grandparent:
    def method1(self):
        pass

class Parent(Grandparent):   # Inheriting Grandparent
    def method2(self):
        pass

class Child(Parent):        # Inheriting Parent
    def method3(self):
        pass
```
# Access Specifires/Modifires

Access specifiers are rules that control who can use the data (variables) and functions (methods) of a class.

# 1. Public
A public member is open to everyone. It can be accessed from inside the class and outside the class.
# Syntax
```
class MyClass:
    def __init__(self):
        self.name = "Ali"   # Public variable
```
### Key Point
- No underscore is used
- Fully accessible
# 2. Private

A private member is restricted to the same class only and should not be accessed from outside.
# Syntax 
```
class MyClass:
    def __init__(self):
        self.__name = "Ali"   # Private variable
```
### Key Point
- Uses double underscore (__name)
- Cannot be accessed directly outside the class
### Name mangling
Name mangling is a technique in Python where private variables are internally renamed to avoid direct access from outside the class.

# 2. Protected

A protected member is meant to be used inside the class and by its child (derived) classes.

