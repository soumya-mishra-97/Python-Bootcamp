## Advanced Python Code
'''
What are packages?
Packages are collections of Python code that solve specific problems:
- requests - Download web pages and data
- pandas - Work with spreadsheets and data
- numpy - Fast mathematical operations
- openai - Connect to AI models
- beautifulsoup4 - Extract data from websites
Each package is like a toolbox with specialized tools for a specific job.
'''

'''
pip (Pip Installs Packages) is Python’s package manager. It:
Downloads packages from the internet
Installs them in your environment
Manages versions and dependencies
'''

'''
Anaconda: it's another tool that manages Python environments and packages. 
It's popular in the data science world because it comes pre-loaded with many data science packages.
if someone else asking to use anaconda environment, you can use virtual enviroment insetad of anaconda. (Recommended)
'''

import requests
import matplotlib.pyplot as plt

#Download a web page
url = "https://www.example.com"
response = requests.get(url)
print('Status code:', response.status_code)

#Define plot data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#Create the line plot
plt.plot(x, y, 
         label = 'Line Plot', 
         color = 'red', 
         marker = 'o', 
         linestyle = '--')

# Add title and labels
plt.title('Sample Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the chart
plt.show()

# Define a function to plot a bar chart
def plot_bar_chart(data, title, xlabel, ylabel):
    plt.bar(data.keys(), data.values(), color='blue')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    
bar_data = {'A': 10, 'B': 15, 'C': 7, 'D': 12}
plot_bar_chart(bar_data, 'Sample Bar Chart', 'Categories', 'Values')


# Highest_frequency_char
''' Input: Programming
Output: g
g appears twice, which is the highest frequency in this example. Other characters with the same frequency can also exist.

Explanation
1. Create a dictionary to store each character's frequency.
2. Loop through the string and increment the count for each character.
3. Use max(frequency, key=frequency.get) to return the character with the highest count.
'''

# Find max_freq character
'''
arr = ['a', 'd', 'f', 'd', 'a', 'h', 'd']
find max_freq character
Output: d

How it works
1. Create a dictionary to count each character.
2. Loop through the list and increment each character's count.
3. Use max(freq, key=freq.get) to find the character with the highest frequency.
4. Return that character.

For this input, d appears 3 times, which is the highest frequency.
- Time complexity: \(O(n)\)
- Space complexity: \(O(k)\), where \(k\) is the number of distinct characters.
'''

# Replace 'd' with 'h' in string 's= 'abcde'
'''s= 'abcde'
s[3] = h ## Type Error

Replace 'd' with 'h' in  string
- Convert the string into a list
- using replace()
- using slicing
'''
# Convert the string into a list
s = 'abcde'
list_s = list(s) #['a', 'b', 'c', 'd', 'e']
print(list_s)
list_s[3] = 'h'
print(list_s) #['a', 'b', 'c', 'h', 'e']
s = ''.join(list_s)
print(s) #abche

# Replace
s= 'abcde'
s= s.replace('d', 'h')
print(s) #abche

# Slicing
s = "abcde"
#      01234
#      -5-4-3-2-1
s = s[:3] + "h" + s[4:]
print(s) #abche
