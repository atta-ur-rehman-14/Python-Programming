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