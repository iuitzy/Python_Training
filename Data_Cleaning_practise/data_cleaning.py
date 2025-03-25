import pandas as pd 

from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import MinMaxScaler

import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\Data_Cleaning_practise\transactions.csv')

print("Duplicate rows before removing: ")

print(df[df.duplicated()])

df=df.drop_duplicates()

print("Duplicate rows after removing: ")

print("Missing Values before removing: ")

print(df.isnull().sum())

df['Amount'].fillna(df['Amount'].mean(),inplace=True)

df['Category'].fillna(df['Category'].mode()[0],inplace=True)

print("Data Types:")
print(df.dtypes)

label_encoder = LabelEncoder()
df['Customer']= label_encoder.fit_transform(df['Customer'])
df['Category']= label_encoder.fit_transform(df['Category'])
df['PaymentMethod']= label_encoder.fit_transform(df['PaymentMethod'])

df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])
df['Day']=df['TransactionDate'].dt.day
df['Month']=df['TransactionDate'].dt.month
df['Year']=df['TransactionDate'].dt.year

print("Data after Transformation:")

print(df.head())

scalar= MinMaxScaler()
df['Amount']=scalar.fit_transform(df[['Amount']])
print("Data after Normalization:")
print(df.head())

plt.figure(figsize=(8, 5))
sns.barplot(x=df['Category'], y=df['Amount'], estimator=sum, ci=None)
plt.xticks(rotation=45)
plt.title("Total Transaction Amount by Category")
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.show()


payment_counts = df['PaymentMethod'].value_counts()
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
plt.figure(figsize=(6, 6))  
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title("Distribution of Payment Methods")
plt.show()
