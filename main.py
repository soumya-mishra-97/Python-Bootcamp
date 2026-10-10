## Crash course: https://python.datalumina.com/getting-started
## Python latest version: 3.14.4
## This file is created to demonstrate the basic concepts of Python programming language.
# This is Python code
name = "Sarah"
age = 25
print(f"Hello, my name is {name} and I am {age} years old")
name = "Alice"
age = 25
is_student = True
print(f"Hello, my name is {name} and I am {age} years old. Am I a student? {is_student}")

name = "Bob"
print(f"Hello, my name is {name}!")

user_name = "Dave"      # lowercase with underscores (Python style)
userName = "Dave"       # camelCase (works but not Python style)
age2 = 30              # numbers are OK (not at start)
_private = "secret"    # underscore at start is OK

# Good Python style
first_name = "Alice"
user_age = 25
is_logged_in = True
shopping_cart_total = 49.99

# Avoid camelCase (this is for other languages)
firstName = "Alice"  # Works, but not Python style
userAge = 25
isLoggedIn = True

# Start with one value
score = 0
print(score)  # Shows: 0
# Change it
score = 10
print(score)  # Shows: 10
# Change it again
score = score + 5
print(score)  # Shows: 15
subtotal = 100.0
# Good: Explains why
# Using 1.0625 because sales tax in CA is 6.25%
total = subtotal * 1.0625

# Bad: States the obvious
# Multiply subtotal by 1.0625
total = subtotal * 1.0625

print("Starting process...")
# print("Debug info")  # Uncomment for debugging
def new_method():
    print("This is a new method.")
new_method()
# old_method()  # Keeping for reference

# Addition and subtraction
total = 10 + 5     # 15
change = 20 - 7    # 13
# Multiplication and division
area = 6 * 4       # 24
half = 10 / 2      # 5.0 (always returns float)
# Powers
squared = 5 ** 2   # 25
cubed = 2 ** 3     # 8
# Regular division (always float)
result = 10 / 3    # 3.333...
# Integer division (rounds down)
result = 10 // 3   # 3
# Single quotes
first = 'Python'
# Double quotes  
second = "Python"
# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""
print(first, second, paragraph)
first_name = "John"
last_name = "Doe"
# Concatenation
full_name = first_name + " " + last_name
print(full_name)  # John Doe
# Repetition
stars = "*" * 5
print(stars)  # *****

message = "Hello"
print(len(message))  # 5
empty = ""
print(len(empty))    # 0

age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old

# Or use f-strings (we'll learn more later)
message = f"I am {age} years old"
print(message)  # I am 25 years old

age = 25
# Equality
print(age == 25)     # True - equals
print(age != 30)     # True - not equals
# Greater/Less than
print(age > 20)      # True - greater than
print(age < 30)      # True - less than
print(age >= 25)     # True - greater or equal
print(age <= 25)     # True - less or equal

# Basic math
print(10 + 3)   # 13 - Addition
print(10 - 3)   # 7  - Subtraction
print(10 * 3)   # 30 - Multiplication
print(10 / 3)   # 3.333... - Division (always gives float)
# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)   # 1  - Modulo (remainder)
print(10 ** 3)  # 1000 - Exponent (power)

result = 2 + 3 * 4      # 14 (not 20!)
result = (2 + 3) * 4    # 20 (parentheses first)

age = 25
has_license = True
not has_license # False
# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

# AND: Both must be True
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False
# OR: At least one must be True  
print(True or False)    # True
print(False or False)   # False
# NOT: Flips the value
print(not True)         # False
print(not False)        # True

# Instead of:
score = score + 10
# Write:
score += 10
# Works with all operators
x = 10
x += 5    # x is now 15
x *= 2    # x is now 30

first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

text = "Python Programming"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
print(text.title())      # "Python Programming"

messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True
# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

new_message = message.replace("I", "We")
print(new_message)  # "We love Python programming with Python"

# Making a simple decision
if age >= 18:
    print("I can vote!")
else:
    print("I'm too young to vote")

print("Hey, Kevin!\nWelcome to Python programming.")
print("Hello", "Kevin", 5, sep=" , ", end=".\n")
print("Hello, Python Learner\nI am \"good\" at Python programming.")
print('''Hey, Kevin!
Welcome to Python programming.''')
print("This is a tab in here ->\t<-")

a = 5 #Integer
print("The value of a is:", a)
if a >= 3:
    print("a is greater than or equal to 3")
    print("Statement 1 is inside the if block")
else:
    print("a is less than 3")
    print("Statement 2 is inside the else block")
    
name = "Kevin" #String
print("Hello, ", name + "!")

cgpa = 3.5 #Float
print("The CGPA is:", cgpa)

isCompleted = True #Boolean
print("Is the task completed?", isCompleted)

isAgeValid = False #Boolean 
print("Is the age valid?", isAgeValid)

pi = 3.14159 #Float
str_pi = int(pi) #Convert float to integer
print("The value of pi is: ", str_pi)

age = int(input("Enter your age: "))
if age > 18:
    print("You are eligible to vote.")
elif age == 18:
    print("You are eligible to vote, but you need to register first.")
else:
    print("You are not eligible to vote.")

marks = int(input("Enter your marks: "))
match marks:
    case m if m>=90 and m<=100:
        print("You got an A grade.")
    case m if m>=80 and m<=89:
        print("You got a B grade.")
    case m if m>=70 and m<=79:
        print("You got a C grade.")
    case m if m>=60 and m<=69:
        print("You got a D grade.")
    case _:
        print("You got an F grade.")
        
## Approcahes -1
# num1 = input("Enter a number: ")
# print("You entered:", num1)
# num1 = int(num1) #Convert num1 to integer
# num2 = num1 + 3
# print("The num2 value is:", num2)

## Approcahes -2
num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))
num5 = num3 + num4
print("The sum of num3 and num4 is:", num5)

# print a square and cube of a number
num6 = int(input("Enter a number: "))
square = num6 ** 2
cube = num6 ** 3
print("The square of", num6, "is:", square)
print("The cube of", num6, "is:", cube)

# Range function demonstration from i to i-1
for i in range(1, 6):
    print("The value of i is:", i)

for i in range( 1, 11):
    print("5 *", i, "=", 5*i)

from itertools import repeat
  
for _ in repeat(None, 10):
    print("This is a repeated message.")

# Count from 1 to 5
for i in range(1, 6):
    print(i) # Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i) # Output: 0, 2, 4, 6, 8

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")
# Output:
# I like red
# I like blue
# I like green

# While loops
i = 1
while i<= 5:
    print(f"Count is {i}")
    i+=1
# Output:
# Count is 1
# Count is 2
# Count is 3
# Count is 4
# Count is 5

# Lists: order listed; collection of items
# Dictionaries: Key value pairs; collection of items
# Tuples: When data shouldn’t change (like coordinates), fixed values; collection of items
# Sets: Unique values, unordered; collection of items

fruits = ["apple", "banana", "orange"]
mixed = ["hello", 42, True, 3.14]  # Different types OK!
print(fruits)  # Output: ['apple', 'banana', 'orange']
print(mixed)  # Output: ['hello', 42, True, 3.14]

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)
print(fruits[-3])   # "apple" (third to last)
# print(fruits[-4])   # IndexError: list index out of range (there are only 3 items)

# Change an item
fruits[0] = "mango"
print(fruits)  # Output: ['mango', 'banana', 'orange']
# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position
print(fruits)  # Output: ['mango', 'kiwi', 'banana', 'orange', 'grape']

# Remove items
fruits.remove("banana")     # Remove by value
print(fruits)  # Output: ['mango', 'kiwi', 'orange', 'grape']
# Slicing
print(fruits[0:2])  # ['mango', 'kiwi']
print(fruits[1:4])  # ['kiwi', 'orange', 'grape']
print(fruits[:2])   # ['mango', 'kiwi']
print(fruits[-2:])  # ['orange', 'grape']

last = fruits.pop()        # Remove and return last
print(last)      # Output: 'grape'
del fruits[0]              # Remove by index
print(fruits)  # Output: ['kiwi', 'orange']
    
has_license = False
my_list = [1, "Soumya", 24, True, has_license]
print(my_list)  # Output: [1, 'Soumya', 24, True, False]

name = my_list[1]  # Accessing the second item in the list
print(name)  # Output: 'Soumya'

age = my_list[2]  # Accessing the third item in the list
print(age)  # Output: 24

is_student = my_list[-2]  # Accessing the fourth item in the list
print(is_student)  # Output: True

has_license = my_list[-1]  # Accessing the fifth item in the list
print(has_license)  # Output: False

number = [3, 1, 4, 1, 5, 9]
print(len(number))  # Output: 6
print(number.count(1))  # Output: 2
print(number.index(4))  # Output: 2
number.sort()
print(number)  # Output: [1, 1, 3, 4, 5, 9]
number.reverse()
print(number)  # Output: [9, 5, 4, 3, 1, 1]
# Copy
new_list = number.copy()   # Create a copy
print(new_list)  # Output: [9, 5, 4, 3, 1, 1]

fruits = ["apple", "banana", "orange"]

# Check if item exists
if "banana" in fruits:
    print("Found banana!")
else:
    print("List is empty")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")
    
# Wrong - both variables point to same list
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4] - changed!

# Right - make a copy
list1 = [1, 2, 3]
list2 = list1.copy()
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged
print(list2)  # [1, 2, 3, 4] - new list

# Dictionaries: Key-value pairs
persons = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
print(persons)  # Output: {'name': 'Alice', 'age': 30, 'is_student': False}
print(persons["name"])  # Output: Alice
persons["name"] = "Bob"  # Change value
print(persons)  # Output: {'name': 'Bob', 'age': 30, 'is_student': False}
print(persons["age"])   # Output: 30
print(persons["is_student"])  # Output: False
print(persons.get("age"))  # Output: 30

# Safer with get()
print(persons.get("job"))    # None (no error)
print(persons.get("job", "Unknown"))  # "Unknown" (default)
# Add or update
persons["email"] = "alice@email.com"  # Add new
print(persons)  # Output: {'name': 'Bob', 'age': 30, 'is_student': False, 'email': 'alice@email.com'}

# Remove items
del persons["email"]              # Remove by key
print(persons)  # Output: {'name': 'Bob', 'age': 30, 'is_student': False}
age = persons.pop("age")          # Remove and return
print(persons)  # Output: {'name': 'Bob', 'is_student': False}
persons.clear()                   # Remove all items
print(persons)  # Output: {}
persons = {
    "name": "Alice",
    "age": 30,
    "is_student": False
}
# Get all keys, values, or items
print(persons.keys())    # dict_keys(['name', 'age', 'city'])
print(persons.values())  # dict_values(['Alice', 30, 'New York'])
print(persons.items())   # dict_items([('name', 'Alice'), ...])

# Right - use get()
print(persons.get("id", 40))  # Returns 40 if missing

# Check if key exists
if "name" in persons:
    print("Name found!")

# Update multiple values
persons.update({"age": 31, "job": "Engineer"})

students = {
    "kevin": {"age": 20, "major": "Computer Science"},
    "sarah": {"age": 22, "major": "Mathematics"},
    "alice": {"age": 21, "major": "Physics"}
}
print(students)
print(students["sarah"])  # Output: {'age': 22, 'major': 'Mathematics'}
print(students["kevin"]["major"])  # Output: Computer Science
print(students["alice"]["age"])  # Output: 21

# Wrong - lists can't be keys
# bad_dict = {[1, 2]: "value"}  # TypeError!

# Right - use immutable types
stud_id = {(1, 2): "id"}  # Tuple is OK
print(stud_id)  # Output: {(1, 2): 'value'}
print(stud_id[(1, 2)])  # Output: value
stud_roll = {"1,2": "roll number"}   # String is OK
print(stud_roll)  # Output: {'1,2': 'roll number'}
print(stud_roll["1,2"])  # Output: roll number

# Tuples: Immutable ordered collection, 
# it can't be changed after creation
# Fixed values, often used for coordinates or fixed data
pi = 3.14159
print(type(pi))  # Output: <class 'float'>
coordinates = (10.0, 20.0)  # Tuple with two values
print(coordinates)  # Output: (10.0, 20.0)
# Accessing tuple items
print(coordinates[0])  # Output: 10.0
print(coordinates[1])  # Output: 20.0
# Tuples are immutable
# coordinates[0] = 15.0  # TypeError: 'tuple' object
empty_tuple = ()  # Empty tuple
print(empty_tuple)  # Output: ()
single_tuple = (42,)  # Single item tuple (note the comma)
print(single_tuple)  # Output: (42,)
print(type(single_tuple))  # Output: <class 'tuple'>
colors = ("red", "green", "blue")
print(colors)  # Output: ('red', 'green', 'blue')
print(colors[0])  # Output: red
print(colors[-1])  # Output: blue
not_tuple = (42)  # This is just 42 in parentheses
print(not_tuple)  # Output: 42
# Without parentheses (implicit)
coordinates = 10, 20
print(coordinates)  # Output: (10, 20)
# Slicing works too
print(colors[0:2])   # ("red", "green")
# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5
print(x, y)  # Output: 3 5
# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)
print(a, b, c)  # Output: 1 2 3
# Swap variables elegantly
x, y = y, x  # Swaps values!
print(x, y)  # Output: 5 3

# # Wrong - tuples are immutable
point = (3, 5)
# point[0] = 4  # TypeError!

# Right - create a new tuple
point = (4, point[1])
print(point)  # Output: (4, 5)
# Or convert to list, modify, convert back
temp = list(point)
temp[0] = 4
print(temp)  # Output: [4, 5]
print(type(temp))  # Output: <class 'list'>
print(temp[0])  # Output: 4
point = tuple(temp)
print(point)  # Output: (4, 5)

# Sets: Unordered collection of unique items
# Sets are mutable, but the items themselves must be immutable (like numbers, strings, or tuples)
# Sets are collections that only store unique values. 
# They automatically remove duplicates.
empty_set = set()  # Create an empty set
print(empty_set)  # Output: set()
numbers = {3, 1, 4, 1, 5, 9}  # Duplicates are removed
print(numbers)  # Output: {1, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])
print(fruits)  # Output: {'banana', 'orange', 'apple'} (order may vary)
# Add items
fruits.add("kiwi")
print(fruits)  # Output: {'banana', 'orange', 'kiwi', 'apple'}
# Remove items
fruits.remove("banana")  # Raises KeyError if not found
print(fruits)  # Output: {'orange', 'kiwi', 'apple'}
fruits.discard("banana")  # Does not raise error if not found
print(fruits)  # Output: {'orange', 'kiwi', 'apple'}
if "kiwi" in fruits:
    fruits.remove("kiwi")
    print("Kiwi removed")
# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)
print(unique_scores)  # Output: {85, 90, 92}
names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))  # Convert back to list
print(unique_names)  # ['Alice', 'Bob', 'Charlie']
allowed_users = {"alice", "bob", "charlie"}
if "dave" not in allowed_users:
    print("Access denied")
else:
    print("Access granted")

#Sets are unordered, so you can't access items by index
numbers = {3, 1, 4, 1, 5, 9}
print(numbers)  # Output: {1, 3, 4, 5, 9} (order may vary)