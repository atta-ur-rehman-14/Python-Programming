# File Handling
File handling means creating, reading, writing, and updating files using Python. It helps you store data permanently (unlike variables which disappear after program ends).

Python provides a built-in function: `open()`
# syntax

```
file = open("example.txt", "mode")
```

```
with open(<file_name>, <mode>) as <alias>:
    <alias>.write("")
```
# Common modes:
- "r" → Read (default)
- "w" → Write (creates new / overwrites)
- "a" → Append (adds data at end)
- "x" → Create (fails if file exists)
- "r+" → Read + Write
# Functions 
open() → start working with file
read() → get data
write() → overwrite data
append() → add data
with → safest way (auto close file)
# Modules
A module in Python is a file that contains Python code (functions, variables, or classes) which you can reuse in other programs.
OR,
A module is a ready-made toolbox that helps you avoid writing the same code again and again.
# CSV File Handling
A CSV (Comma-Separated Values) file is used to store tabular data (like Excel), where values are separated by commas.
# Important 
- Always use newline="" while writing CSV files
- Use with open() (best practice)
- CSV stores data as strings

# JSON File Handling 
JSON (JavaScript Object Notation) is a format used to store and exchange data.
It looks like a Python dictionary (key-value pairs).
# Important
- `json.load()` → read from file
- `json.dump()` → write to file
- `json.loads()` → string to Python
- `json.dumps()` → Python to string