# What is Python?

- Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

- It is used for:

   - web development (server-side),
   - software development,
   - mathematics,
   - system scripting.

# What can Python do?

- Python can be used on a server to create web applications.
- Python can be used alongside software to create workflows.
- Python can connect to database systems. It can also read and modify files.
- Python can be used to handle big data and perform complex mathematics.

# Why Python?

- Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
- Python has a simple syntax similar to the English language.
- Python has syntax that allows developers to write programs with fewer 
  lines than some other programming languages.
- Python runs on an interpreter system, meaning that code can be executed as
  soon as it is written. This means that prototyping can be very quick.
- Python can be treated in a procedural way, an object-oriented way or a 
  functional way.

# Good to know

- The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
- In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

# Python Syntax compared to other programming languages
Python was designed for readability, and has some similarities to the English language with influence from mathematics.
Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
eg:
## C++ Program
```
#include <iostream>
int main() {
    std::cout << "Hello World!";
    return 0;
}
```
## Python Program
```
print("Hello World!)
```
- Python relies on ````indentation````, using ````whitespace````, to define 
  scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.
eg:

# Python Loop
```
for x in range(6):
  print(x)
```
# Difference Between Compiler and Interpreter

## Compiter
- Translation Process: Translates the entire program into machine code at once before execution.
- Output: Generates an independent executable file (e.g., .exe or .obj).
- Execution Speed: Generally faster because the code is already pre-translated.
- Error Detection: Reports all syntax errors only after scanning the entire program.
- Memory Usage: More memory-efficient during execution as the translator isn't needed once compiled.
- Examples: C, C++, Rust, Go.
## Interpreter
- Translation Process: Translates and executes the program line-by-line during runtime.
- Output: Does not generate an output file; it executes code directly.
- Execution Speed: Slower because translation happens simultaneously with execution.
- Error Detection: Reports errors one by one as it encounters them in a specific line.
- Memory Usage: Higher memory usage because the interpreter must remain in memory during execution.
- Examples: Python, JavaScript, Ruby, PHP.



