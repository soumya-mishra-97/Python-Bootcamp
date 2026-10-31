import os
import pandas as pd
import json
from pathlib import Path

print(f'Get current directory: {os.getcwd}')

data_path = 'data/sales.csv'

if os.path.exists(data_path):
    print(f"Found the path {data_path}")
else:
    print("can not find the path")
    print("Make sure path should be exist in sales-analysis folder")
    
## One folder level up then go with ../data; 
# if you wnat to go two level up then ../../data
## you are abale to access the outside of data folder

data_path1 = "../data/paris_weather.csv"
if os.path.exists(data_path1):
    print(f"Found the path {data_path1}")
else:
    print("can not find the path")
    print("Make sure path should be exist in sales-analysis folder")
    
## --------
'''
# Read CSV file
data_path = Path(__file__).resolve().parent / "data" / "sales.csv"
df  = pd.read_csv(data_path)
# Read JSON file
data_path = Path(__file__).resolve().parent / "data" / "sales.json"
df  = pd.read_json(data_path)
# Read Excel file
data_path = Path(__file__).resolve().parent / "output" / "sales_data.xlsx"
df  = pd.read_excel(data_path)
'''
df  = pd.read_csv("data/sales.csv") # Read csv file
df = pd.read_json("data/sales.json")  # Read json file
df = pd.read_excel("output/sales_data.xlsx")  # Read excel file
print(df)
print(f"Shape {df.shape[0]} rows and {df.shape[1]} columns")

# Calculation operation
total_price = df['quantity'] * df['price']
print(f"Total Price: {total_price}")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save the file as different formats
df.to_json('output/sales_data.json', orient='records',  indent=2)
df.to_excel('output/sales_data.xlsx', index=False)
df.to_csv('output/sales_data.csv', index=False)

print("Data saved")

with open('data/sales.json', 'r') as f:
    data = json.load(f)
    print(data)

with open('output/sales_data.xlsx', 'rb') as f:
    data = pd.read_excel(f)
print(data)