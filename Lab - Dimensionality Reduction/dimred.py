import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1️⃣ Load Wine Dataset from CSV
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\Lab - Dimensionality Reduction\wine_dataset.csv')

# 2️⃣ Handle Missing Values (Choose ONE method)

# Method 1: Drop rows with NaN
df.dropna(inplace=True)

# OR Method 2: Fill NaN with column mean
# df.fillna(df.mean(), inplace=True)

# 3️⃣ Standardizing the Data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df.iloc[:, 1:])  # Ignore first column (Wine_ID)

# 4️⃣ Apply PCA (Reducing to 2 Components)
pca = PCA(n_components=2)
pca_result = pca.fit_transform(df_scaled)

# 5️⃣ Create a New DataFrame with PCA Results
df_pca = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
df_pca['Wine_ID'] = df['Wine_ID']  # Preserve original IDs

# 6️⃣ Feature Contribution (PCA Components)
feature_contributions = pd.DataFrame(pca.components_, columns=df.columns[1:], index=['PC1', 'PC2'])

# 7️⃣ Visualize Before PCA
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df.iloc[:, 1], y=df.iloc[:, 2], palette='viridis')
plt.xlabel(df.columns[1])
plt.ylabel(df.columns[2])
plt.title("Before PCA: Feature Space Visualization")
plt.show()

# 8️⃣ Visualize After PCA
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df_pca['PC1'], y=df_pca['PC2'], palette='viridis')
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("After PCA: Reduced Feature Space")
plt.show()

# 9️⃣ Display Feature Contributions
print("\n🔍 Feature Contributions to Principal Components:\n")
print(feature_contributions.T)
