import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\Data_Cleaning_practise\transactions.csv')  # Replace with the actual file path

# Display the first few rows
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Fill missing values in 'Amount' with the median
df['Amount'].fillna(df['Amount'].median(), inplace=True)

# Convert TransactionDate to datetime format
df['TransactionDate'] = pd.to_datetime(df['TransactionDate'])

# Convert categorical features to numerical for correlation analysis
df['PaymentMethod'] = df['PaymentMethod'].map({'Credit Card': 1, 'Cash': 2, 'UPI': 3, 'Debit Card': 4})
df['Category'] = df['Category'].astype('category').cat.codes  # Assign numerical codes
df['Customer'] = df['Customer'].astype('category').cat.codes

# Verify data after transformation
print("\nData after transformation:")
print(df.head())

# Compute correlation matrix
correlation_matrix = df.corr()

# Print correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Plot the correlation heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# Univariate Analysis (Distributions)

fig, ax = plt.subplots(2, 2, figsize=(12,10))

sns.histplot(df['Amount'], ax=ax[0,0], kde=True, color='blue')
ax[0,0].set_title('Transaction Amount Distribution')

sns.histplot(df['Charges'], ax=ax[0,1], kde=True, color='red')
ax[0,1].set_title('Transaction Charges Distribution')

sns.countplot(x='Category', data=df, ax=ax[1,0])
ax[1,0].set_title('Transaction Count by Category')
ax[1,0].set_xticklabels(ax[1,0].get_xticklabels(), rotation=45)

sns.countplot(x='PaymentMethod', data=df, ax=ax[1,1])
ax[1,1].set_title('Transaction Count by Payment Method')
ax[1,1].set_xticklabels(['Credit Card', 'Cash', 'UPI', 'Debit Card'])

plt.tight_layout()
plt.show()


# Bivariate Analysis


# Scatter plot for Amount vs Charges
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Amount', y='Charges', hue='PaymentMethod', data=df)
plt.title("Transaction Amount vs Charges")
plt.show()

# Spending trends by category
plt.figure(figsize=(10, 5))
sns.boxplot(x='Category', y='Amount', data=df)
plt.title("Transaction Amount by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.show()

# Payment method trends
plt.figure(figsize=(8, 5))
sns.barplot(x='PaymentMethod', y='Amount', data=df)
plt.title("Average Transaction Amount by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Amount")
plt.xticks(ticks=[0, 1, 2, 3], labels=['Credit Card', 'Cash', 'UPI', 'Debit Card'])
plt.show()

# Customer-wise spending
plt.figure(figsize=(10, 5))
sns.barplot(x='Customer', y='Amount', data=df)
plt.title("Total Spending Per Customer")
plt.xlabel("Customer")
plt.ylabel("Amount")
plt.show()

# Trend Analysis Over Time
df['TransactionMonth'] = df['TransactionDate'].dt.to_period("M").astype(str)

plt.figure(figsize=(12, 5))
sns.lineplot(x='TransactionMonth', y='Amount', data=df, marker="o")
plt.title("Monthly Transaction Amount Trend")
plt.xlabel("Month")
plt.ylabel("Total Transaction Amount")
plt.xticks(rotation=45)
plt.show()
