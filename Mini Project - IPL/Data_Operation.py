import pandas as pd

df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\Mini Project - IPL\match_data.csv')

# finding missing values in the data
def missing_values(df):
    print("Missing values before cleaning:")
    print(df.isnull().sum())