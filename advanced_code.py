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

#Download a web page
url = "https://www.example.com"
response = requests.get(url)
print('Status code:', response.status_code)