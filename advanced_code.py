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