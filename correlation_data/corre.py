import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt


df=pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\correlation_data\sample_data.csv')

#print(df.head())

print("Missing values before cleaning:")
print(df.isnull().sum())

df['Income'].fillna(df['Income'].median())
df['SpendingScore'].fillna(df['SpendingScore'].median())

print("Missing Values After Cleaning:")
print(df.isnull().sum())

df['Gender']=df['Gender'].map({'Male':1,'Female':0})

print("Data after Transformation:")
print(df.head())

#Univariate Analysis

fig, ax = plt.subplots(2, 2, figsize=(12,10))
sns.histplot(df['Age'], ax=ax[0,0], kde=True, color='red')
ax[0,0].set_title('Age Distribution')

sns.histplot(df['Income'], ax=ax[0,1], kde=True, color='blue')
ax[0,1].set_title('Income Distribution')

sns.histplot(df['SpendingScore'], ax=ax[1,0], kde=True, color='green')
ax[1,0].set_title('Spending Score Distribution')

sns.countplot(x='EducationYears', data=df, ax=ax[1,1])
ax[1,1].set_title('Education Years Count')

plt.tight_layout()
plt.show(block=False)

#Bivariate Analysis
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Income',y='SpendingScore',hue='Gender',data=df)
plt.title  ("Income vs Spending Score")
plt.show(block=False)

#correlation matrix
correlation_matrix=df.corr()
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show(block=False)

#only female trend analysis 
df_female = df[df['Gender'] == 0]
education_spending = df_female.groupby('EducationYears')['SpendingScore'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='EducationYears', y='SpendingScore', data=education_spending, palette='viridis')
plt.title("Average Spending Score by Years of Study (Women)")
plt.xlabel("Years of Study (EducationYears)")
plt.ylabel("Average Spending Score")
plt.xticks(rotation=45)
plt.show(block=False)

#only men 
df_male = df[df['Gender'] == 1]
education_spending_men = df_male.groupby('EducationYears', as_index=False)['SpendingScore'].mean()
plt.figure(figsize=(8, 5))
sns.barplot(x='EducationYears', y='SpendingScore', data=education_spending_men, palette='Blues')
plt.title("Average Spending Score by Years of Study (Men)")
plt.xlabel("Years of Study (EducationYears)")
plt.ylabel("Average Spending Score")
plt.xticks(rotation=45)
plt.show(block=True)