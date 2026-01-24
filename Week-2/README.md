# Variables
- variables are the container that is used to store data temporarily.
- Variables is a symbolic name that refers to data.it can hold manay values
  but at a time it can hold only one value. 
- Data store in memory (memory means RAM).
# Example of variable code
## Creating Veriable As String

```
Name="Atta Ur Rehman"
print(Name)
```
## Type of given data
```
type(Name)
```
## Finding Id or Address of storing data
```
id(Name)
```
## Creating Veriable As number/Integer

```
Num= 20
print(Num)
```
## Type of given data
```
type(Num)
```
## Finding Id or Address of storing data
```
id(Num)
```

## Creating Veriable As Float
```
Weight= 20.2
print(Weight)
```
## Type of given data
```
type(Weight)
```
## Finding Id or Address of storing data
```
id(Weight)
```
- [Practice Exercise For Variable](http://www.ASmarterWayToLearn.com/python/2.html) 


# Datatypes
 Datatype specify the value of data that variable hold.That is use to perform operation

- Integers -->  ````Numbers```` eg. 23
- Decimal --> ````Float```` eg. 12.4
- Character --> ````string```` eg. "Atta"
- Binary 0/1 OR True/False --> ````Boolean```` eg. True/False 

### Apply all these steps/Rules on diffferen data types ( string, integer, float, bool)

- creating a variable eg: variable_name = variable_value 
- printing that variable eg: print(variable_name) 
- check the type of variable eg: type(variable_name) 
- check the address of the variable eg: id(variable_name)

## Creating Veriable As Boolean
```
boolean_var=True
print(boolean_var)
```
## Type of given data
```
type(boolean_var)
```
## Finding Id or Address of storing data
```
id(boolean_var)
```
## Creating Veriable As Boolean
```
boolean_var=False
print(boolean_var)
```
## Type of given data
```
type(boolean_var)
```
## Finding Id or Address of storing data
```
id(boolean_var)
```
- [Practice Exercise for Var Rules](http://www.ASmarterWayToLearn.com/python/5.html  )

# Operators

- ````Addition```` +
```
2+5
```
- ````Subtraction```` -
```
5-3
```
- ````Multiplication```` *
```
3*3
```
- ````Divide```` /
```
20/5 
- Note it down that divide give result in FLOAT
```
- ````Power```` **
```
2**3 # 2*2*2
```
```
4**5 # 4*4*4*4*4
````

- [Practice Exercise for Operators](http://www.ASmarterWayToLearn.com/python/4.html)


# Unfamiliar Operator
- Reminder/Modulus % (it will give remainder )
- Floor // (it will give 1 value that would be display before point)

```
20/4
```
```
20 % 3    (Give Remainder)
- 3*6 = 18
- 3*7 = 21
```

```
13//4
- 13/4 => 3.25
```

```
20//3
- 20/3 = 6.66
```

```
26//5
```
# Expressions (BODMAS)

```
((5*4) + (4-2))-5

- = ((5*4) + (4-2))-5
- = (20 + 2) - 5
- = 22 - 5
- = 17
```
```
((((4*2)+2)/5)*3) +1
```
# Naming Convention and Reserve Keywords

- id
- type
- print
- if, else, elif

# Rules

- Don't have number in start
- Naming can't ahve spaces (tip: use underscore)
- Can't use reserve keywords

# Tips

- Always keep the name meanining full and consice
     - name = "Atta" --> Good
     - city = "Atta" --> wrong
     - My_name_is = "Atta Ur Rehman"

- [Reserve Kerwords](image.png)
# Conditional Statement
- if internert_available --> Class will be conducted.
- if no internet_available --> There will be no class.
# if-else
 ```
 internet = True
 if internet:
    print("Class will be Conducted")
    print("Goto to Institute")
    print("Attended the calss")
else:
    print("There will be no class")
```
### Q: Write a python code that check the age. If age is greater then 18 then eligible for CNIC else not elibigle

```
age= int(input("Enter your age:"))

if age > 18:
    print("You're eligible for CNIC")
else:
    print("Sorry, You're not Eligible")

```
# Conditional Operators

- ````Greater then```` >
- ````Less then```` <
- ````Not equal```` to !=
- ````Greater then```` and ````Equal to```` >=
- ````Less then```` and ````Equal to```` <=
- ````equals to```` ==

```
5 > 2
```
```
3 < 7
```
```
5 != 6
```
```
5 == 5
```

```
40 >= 41
```
```
40 <= 41
```
