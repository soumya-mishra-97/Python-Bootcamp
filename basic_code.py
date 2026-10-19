## Basic Python Code
## Functions:
# Avoid to import evrerything from a module using *
# from math import *
# import math
from math import sqrt, pi
from datetime import datetime, timezone, timedelta
import os
import pandas as pd

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

def isTemperature_high(temp):
    value = 30
    if temp > value:
        print("Temperature is high")
    else:
        print("Temperature is normal")

isTemperature_high(35)  # Output: Temperature is high

def calculate_tax(amount, tax_rate, discount=0):
    tax = amount * tax_rate
    total = amount + tax - discount
    return total

tax_amount = calculate_tax(100, 0.1, 5)
print(tax_amount)  # Output: 105.0

def calculate_total_ctc(price):
    tax_rate = 0.02
    discount = 10
    tax = price * tax_rate
    finalPrice = price + tax - discount 
    print(f"Total CTC in LPA: {finalPrice} lpa")

calculate_total_ctc(1400000)

def simple_numbers() -> int:
    numbers = [1, 2, 3, 4, 5]
    first_num = numbers[0]
    last_num = numbers[-1]
    return first_num + last_num

simple_numbers()

## Reverse String using higher-order function and without higher-order function
# Higher-order function approach:
def reverse_string(value: str) -> str:
    return ''.join(reversed(value))
print("Reversed string approach1:", reverse_string("Hello, World!"))

# Without higher-order function:
'''
How range() works
For: Hello, World! : there are 13 characters.

The indexes are:
H e l l o ,   W o r l d !
0 1 2 3 4 5 6 7 8 9 10 11 12

This: range(len(value) - 1, -1, -1)
becomes: range(12, -1, -1)
So the indexes are: 12 → 11 → 10 → 9 → ... → 0
Characters are therefore read as: ! → d → l → r → o → W → , →   → o → l → l → e → H
Then join() creates: !dlroW ,olleH
'''
def reverse_string_manual(value: str) -> str:
    characters = []
    for index in range(len(value) -1, -1, -1):
        characters.append(value[index])
    return ''.join(characters)
print("Reversed string approach2:", reverse_string_manual("Hello, World!"))

## Reverse Word using higher-order function and without higher-order function
# Higher-order function approach:
def reverse_word(value: str) -> str:
    return ' '.join(reversed(value.split()))
print("Reversed word approach1:", reverse_word("Hello, My name is Kevin!"))

#without higher-order function:
def reverse_word_manual(value: str) -> str:
    words = value.split()
    reversedwords = []
    for index in range(len(words) -1, -1, -1):
        reversedwords.append(words[index])
    return ' '.join(reversedwords)
print("Reversed word approach2:", reverse_word_manual("Hello, My name is Kevin!"))

result = sqrt(64)
print(result)
radius = 5
circle_area = pi * radius ** 2
print(circle_area)
now = datetime.now()
print(now)
today = datetime.today().date()
print(today)
utc_time = datetime.now(timezone.utc)
print(utc_time)
current_directory = os.getcwd()
print(current_directory)
data = {
    'Name': 'Alice',
    'Age': 30,
    'City': 'New York'
}
print(data)
data_frame = pd.DataFrame([data])
print(data_frame)

# How do you convert a list of characters into a string?
characters = ['A', 'I']
result = ''.join(characters)
print(result)