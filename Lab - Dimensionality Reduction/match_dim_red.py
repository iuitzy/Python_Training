import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D

# 1️⃣ Load Dataset
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\Lab - Dimensionality Reduction\match_info_data.csv')

# 2️⃣ Convert 'season' column to numeric (Fix '2020/21' issue)
df['season'] = df['season'].astype(str).str[:4].astype(int)

# 3️⃣ Select Only Numeric Columns for PCA
numeric_columns = ['season', 'win_by_runs', 'win_by_wickets', 'dl_applied']
df_numeric = df[numeric_columns].copy()

# 4️⃣ Handle Missing Values Properly
df_numeric = df_numeric.dropna()  # OR df_numeric.fillna(df_numeric.mean(), inplace=True)

# 5️⃣ Standardizing the Data
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

# 6️⃣ Apply PCA (Reducing to 3 Components)
pca = PCA(n_components=3)
pca_result = pca.fit_transform(df_scaled)

# 7️⃣ Create a New DataFrame with PCA Results
df_pca = pd.DataFrame(pca_result, columns=['PC1', 'PC2', 'PC3'])
df_pca['ID'] = df.loc[df_numeric.index, 'id']  # Preserve Match ID

# 8️⃣ 3D Visualization After PCA
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(df_pca['PC1'], df_pca['PC2'], df_pca['PC3'], c=df_pca['PC1'], cmap='viridis')

ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_zlabel("Principal Component 3")
ax.set_title("After PCA: 3D Feature Space")
plt.colorbar(scatter)
plt.show()

# 9️⃣ Feature Contributions to Principal Components
feature_contributions = pd.DataFrame(pca.components_, columns=numeric_columns, index=['PC1', 'PC2', 'PC3'])

print("\n🔍 Feature Contributions to Principal Components:\n")
print(feature_contributions.T)
