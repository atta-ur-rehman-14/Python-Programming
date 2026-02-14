# Logical Operatore
- AND 
```
True and True = True
True and False = False
False and True = False
False and False = False

```
- OR 
```
True and True = True
True and False = True
False and True = True
False and False = True

```


# conditional statements
- if internet avaliable --> Class will be held
- if internet not avaliable --> Class will not be conducted

# Syntax
```
if<condition>:
    <body of if>
else:
    <body of else>
```
# List 
- Collection of Items
- Ordered Items
- Mutable (Means Changeable) 
List is a built in data type that store the multiple values in one variable.
It is a container that store multiple values
- 
## key point
- use [] sqayre brackets to make list
- Collection of Items
- Store multiple data types
# Syntax
```
list_name = [element1, element2, element3]
```
# Indexing
indexing means accessing element of sequence (like a list, string, or tuple) using thier position number
- Always start with [0]
# Reason of indexing why start woth zero
Python uses 0-based indexing because the index represents the offset from the starting memory address, and the first element is at offset 0.
This makes memory calculations simpler and faster in low-level implementation.
# Syntax
```
list_name[index]
```


### Negative-Indexing
- Right to left
- Negative indexing starts from -1 (last element).
- Accessing an index out of range gives IndexError.

# Append 
The `append()` method is used to add an element to the end of a list.
# Syntax
```
list_name.append(value)
```
### Important Points:
- It adds only one element at a time.
- It always adds the element to the end of the list.
- It modifies the original list (lists are mutable).

# POP
The `pop()` method removes and returns an element from a list.
- remove element by using index

### Syntax

```
list_name.pop(index)
```
- index is optional.
- If no index is given, it removes the last element.
# Remove
The remove() method is used to delete the first occurrence of a specified value from a list.
- remove element by using value
### Syntax
```
list_name.remove(value)
```
### Important Points

- `value` → the element you want to remove.

- Only removes the first match.
- Modifies the original list (mutable).
- Raises ValueError if the element is not found.

# Insert
The `insert()` method is used to add an element at a specific index (position) in a list.
# syntax 
```
list_name.insert(index, value)
```
- `index` → position where you want to add the element
- `value` → element to be inserted

# Agregate Function
Aggregate functions are used to perform calculations on a collection of values (like a list) and return a single summarised value.
Some Common aggregate functions include:`sum()`,`min()`,`max()`,`len()`,
`sorted()`.