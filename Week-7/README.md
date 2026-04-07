# *args 
`*args` allows a function to take multiple positional arguments (values without names).

- Non-keyword / Positional Arguments
- It stores data as a tuple.
# syntax
```
def function_name(*args):
    # use args
```
# Example
```
def numbers(*args):
    print(args)

numbers(1, 2, 3, 4)
```
# Example 2
```
def add(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

add(5, 10, 15)
```
# **kwargs 
`**kwargs` allows a function to take multiple keyword arguments (key = value pairs).

- Keyword Arguments
- It stores data as a dictionary.
# Syntax
```
def function_name(**kwargs):
    # use kwargs
```
# Example
```
def student(**kwargs):
    print(kwargs)

student(name="Ali", age=20)
```
# Example 2
```
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, "=", value)

student(name="Ali", age=20)
```