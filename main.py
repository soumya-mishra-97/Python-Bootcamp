print("Hello, World!")

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

'''
print("What does the Visualize button do?")
Write a code to call LLM model gpt 4o deployed in azure  
https://abc.openai.com/deployments/gpt4o/chat/completions
'''
