## Python latest version: 3.14.4
## This file is created to demonstrate the basic concepts of Python programming language.
# This is Python code
name = "Sarah"
age = 25
print(f"Hello, my name is {name} and I am {age} years old")

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

