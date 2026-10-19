## 1. Virtual Enviroment:
'''
that allows us to install and manage project-specific dependencies separately from other projects. 
It helps prevent dependency conflicts when different projects require different versions 
of the same package.

Example
Suppose you have two projects:
- Project A: Requires FastAPI version 0.100.
- Project B: Requires FastAPI version 0.115.
Without isolation, managing different package versions can become difficult. 
Virtual environments allow each project to maintain its own dependencies.

Beest way to configure a project environment is to create a virtual environment using venv, 
install the required dependencies using pip, 
and maintain a requirements.txt file to manage package versions.

-- Use a separate .venv for each project.
-- Add .venv/ to .gitignore; don't commit the environment itself.
-- Use requirements.txt or a project dependency manager such as Poetry or uv to manage dependencies.
-- Keep secrets in environment variables or a .env file, and don't commit secrets to Git.
-- In deployment, recreate the environment and install the project's dependencies.
'''

## 2. Class Instance vs Local  vs  Instance Variable
''' 
a. Instance Variable: 
- maintain the object specific data. deifined in 'init()'
- you can access it thorugh the self keyword.
- you can access it through the object even outside of the function.

b. Local Variable:
- Defined inside in the function
- Can't access it outside of the function

c. Class instance Variable:
- Belongs to the class level, it can create inside in the class, shared by default.
- Accessible through the class name
'''
# Code:- 
class Employee:
    comp_name = "Fiserv" # class instance var
    
    def __init__(self, name, salary):
        self.name = name # instance var
        self.salary = salary # instance var
    
    def display(self):
        department = "Software" # local var
        print(self.name ) # accessing the instance var
        print(department)

emp1 = Employee("Kevin", "$10000") 
emp2 = Employee("Alice", "$25000")
# access instance variables through objects
print(f"Employee 1: {emp1.name} -> {emp1.salary}")
print(f"Employee 2: {emp2.name} -> {emp2.salary}")
# acess class instance variable through class name
print(Employee.comp_name)
# access class instance variable through class instance
print(emp1.comp_name)
# access local variable
emp1.display()

## 3. Muatble vs Immutable variable
'''
Mutables objects are chnaged after creation
Immutable objects can't be chnaged after creation
'''
# Imutable code:  str, int, float, tuple
'''
What happens here?
- name = "Smith" → name refers to the string object "Smith".
- name = "Kevin" → name now refers to a different string object, "Kevin".
- The original string "Smith" is not modified in here.
Reassigning a variable is not the same as modifying an object. 
Strings are immutable in Python.
'''
name = "Smith" # refers to one object
name = "Kevin" # refers to other object
print(name) # Kevin

# Mutable code: list, dict, set
'''
names refers to a list object.
append() modifies the existing list.
The same list object now contains an additional element.
'''
names = ["Kevin", "Smith"]
names.append("Alice")
print(names)

## 4. Tuples, is it mutable or imumtable, if i change the tuple value how can i change it
'''
Tuples contains the fixed number of values, 
it contains different data type in to a single compound.
It's like a immutable but if you want to chnage the tuple value like you can alter it
so you convert it to the list after that you modifying it to the tuples
'''
# Code:-
student = (1, "Kevin",  True) # tuples
print(student[1]) # access the tuples value
student_list = list(student) # convert tuple to list
print(student_list)
# modify the list
student_list[1] = "Alice"
student_list.append("Software Dept")
print(student_list)
student = tuple(student_list) #convert the list to tuples
print(student)

## 5. Iterator vs Generator
'''
Iterator: 
it access the elemets at a time using iter() and next()

Generator: it creates the iterator using yeild(), 
it produces the values very lazily and it generates the each of the value when it requested,
when you work on large data sets, impage processing etc... 
used for reduced the memory consumption
yield keyword used when the new requested genrates it resumes where it stops
'''
# Code :-
# Iterator : -
numbers1 = [1,2,3,4]
iterator = iter(numbers1)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # StopIteration Error

# Geneator : -
def generate_nums():
    yield 1
    yield 2
    yield 3
    yield 4
numbers2 = generate_nums()
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
print(next(numbers2))
# print(next(numbers2)) # StopIteration Error

## 6. How to handle the error scenarios in Fast API applications
'''
try, exception, else, finally
Explain the differiencitae between them
- try: performs the execution part like calculations, api call etc..
- exception: handles the failure scenarios
- else: handles the success scenarios
- finally: making it for the cleaup or loging wheater the operation is success or failure
'''
