import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\match_info_data.csv')

### Step 1: Drop Unnecessary Columns
df.drop(columns=['date'], errors='ignore', inplace=True) 

# Debugging Step: Check available columns
print("Columns after dropping 'date':", df.columns)

### Step 2: Handle Missing Values
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

# Fill missing values
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

### Step 3: Handle Outliers
for col in num_cols:
    df[col] = np.where(df[col] > df[col].quantile(0.99), df[col].quantile(0.99), df[col])
    df[col] = np.where(df[col] < df[col].quantile(0.01), df[col].quantile(0.01), df[col])

### Step 4: Feature Engineering - Creating 'margin_of_victory'
if 'win_by_runs' in df.columns and 'win_by_wickets' in df.columns:
    df['margin_of_victory'] = np.where(df['win_by_runs'] > 0, df['win_by_runs'], df['win_by_wickets'])
    df.drop(columns=['win_by_runs', 'win_by_wickets'], inplace=True)
else:
    raise KeyError("Missing columns: 'win_by_runs' or 'win_by_wickets'. Check dataset structure.")

# Debugging Step: Verify 'margin_of_victory' column exists
print("Columns after feature engineering:", df.columns)

### Step 5: Remove Highly Correlated Features
df_numeric = df.select_dtypes(include=[np.number])  # Keep only numeric columns
corr_matrix = df_numeric.corr()  # Compute correlation matrix
high_corr_features = [col for col in corr_matrix.columns if any(corr_matrix[col] > 0.9) and col != 'margin_of_victory']
df.drop(columns=high_corr_features, inplace=True)

### Step 6: Encode Categorical Variables
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

### Step 7: Split Data
if 'margin_of_victory' in df.columns:
    X = df.drop(columns=['margin_of_victory'])
    y = df['margin_of_victory']
else:
    raise KeyError("'margin_of_victory' column is missing after preprocessing.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### Step 8: Train RandomForest with Hyperparameter Tuning
rf = RandomForestRegressor(random_state=42)

# Hyperparameter grid
param_grid = {
    'n_estimators': [100, 300, 500],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search = GridSearchCV(rf, param_grid, cv=3, scoring='r2', n_jobs=-1, verbose=2)
grid_search.fit(X_train, y_train)

# Best Model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

### Step 9: Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"✅ Mean Absolute Error (MAE): {mae:.2f}")
print(f"✅ Mean Squared Error (MSE): {mse:.2f}")
print(f"✅ R-squared (R²): {r2:.2f}")

# Feature Importance
importances = best_model.feature_importances_
feature_names = X.columns
sorted_indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10, 6))
sns.barplot(x=importances[sorted_indices][:10], y=[feature_names[i] for i in sorted_indices[:10]])
plt.title("Top 10 Feature Importance")
plt.show()


