import pandas as pd

data_csv1 = pd.read_csv('c:/Users/bhavithar/OneDrive - Maveric Systems Limited/Desktop/py_Basic/Python_Training/pandas_tesla_data/Merge_data.csv')
mydf = pd.DataFrame(data_csv1)

# drop multiple columns 

# deleted_df= mydf.drop(columns=['Succesfull','Stalls'])
# print(deleted_df)
# deleted_df.to_csv('deleted.csv', index=True)

#column wise information like avg, mean, max, min
# print(mydf['Stalls'].mean())
# print(mydf['Stalls'].max())             
# print(mydf['Stalls'].min())

#write to csv --> if we want
mydf['NewColumn'] = 'DefaultValue'  # Replace 'DefaultValue' with your desired default

mydf.to_csv('write.csv', index=True)

#filter csv code 
# query_df =mydf.query('Stalls > 6 and Succesfull == 1') 
# print(query_df)
# query_df.to_csv('filtered.csv', index=True)

'''renaming column 
split it into 3 -->60:20:20
combine/merge
filter
remove multiple selected colmns
colum wise information like avg, mean, max, min
write to csv --> if we want '''

#Renaming Stalls column to outlets 
#df = pd.read_excel("Tesla EV Charging Dataset.xlsx", engine="openpyxl")
# df.rename(columns={"Stalls": "Outlets"}, inplace=True)

# df.to_excel("Updated_Tesla_EV_Charging_Dataset.xlsx", index=False, engine="openpyxl")

#Splitting the data into 3 parts of (60:20:20)

# df = pd.read_excel("Tesla EV Charging Dataset.xlsx", engine="openpyxl")


# df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# df_60 = df.sample(frac=0.6, random_state=42)
# df_remaining = df.drop(df_60.index)

# df_20_1 = df_remaining.sample(frac=0.5, random_state=42)
# df_20_2 = df_remaining.drop(df_20_1.index)

# df_60.to_excel("Tesla_EV_Charging_60.xlsx", index=False)
# df_20_1.to_excel("Tesla_EV_Charging_20_1.xlsx", index=False)
# df_20_2.to_excel("Tesla_EV_Charging_20_2.xlsx", index=False)

# df = pd.read_excel("Tesla_EV_Charging_Dataset.xlsx", engine="openpyxl")

# # Shuffle the dataset to randomize the order
# df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# # Define split indices
# n = len(df)
# split_60 = int(n * 0.6)  # First 60%
# split_80 = int(n * 0.8)  # First 60% + Next 20%

# # Split the dataset using iloc
# df_60 = df.iloc[:split_60]  # First 60%
# df_20_1 = df.iloc[split_60:split_80]  # Next 20%
# df_20_2 = df.iloc[split_80:]  # Remaining 20%

# combine or merge 

# data_20_1 = pd.read_excel("Tesla_EV_Charging_20_1.xlsx", engine="openpyxl")
# data_20_2 = pd.read_excel("Tesla_EV_Charging_20_2.xlsx", engine="openpyxl")

# df= pd.DataFrame(data_20_1)
# df1=pd.DataFrame(data_20_2)

# frames = [df,df1]

# result = pd.concat(frames)

# result.to_excel("Merge_data.xlsx", index=False, engine="openpyxl")

# filter the data from the exce sheets 



# df = pd.read_excel("Merge_data.xlsx", engine="openpyxl")












#print(df.head())

# Basic Data exploration 

#df.info()
#print(df.head(2))

#print(df.tail(2))

#print(df.shape)
#print(df.columns)
#print(df.dtypes)

#print(df.isnull().sum())  

#print(df.to_string())

#print(df)

#print(df.dropna())
#print(df.isnull().sum())
#print(pd.options.display.max_rows)



