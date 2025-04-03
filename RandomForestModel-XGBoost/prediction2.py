import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # Use GUI backend for debugging
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
import joblib

# Load the dataset
df = pd.read_csv('smartphone_data.csv')
print("First 5 rows of data:\n", df.head())

# Data Cleaning and Preprocessing
df.fillna(df.median(numeric_only=True), inplace=True)  
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])
df.drop_duplicates(inplace=True)

# Feature Engineering
df['Battery_per_Inch'] = df['Battery (mAh)'] / df['Display Size (Inches)']
df['Camera_per_RAM'] = np.where(df['RAM (GB)'] == 0, 0, df['Camera (MP)'] / df['RAM (GB)'])
df['Storage_per_RAM'] = np.where(df['RAM (GB)'] == 0, 0, df['Storage (GB)'] / df['RAM (GB)'])
df['Battery_x_RAM'] = df['Battery (mAh)'] * df['RAM (GB)']
df['Camera_x_Storage'] = df['Camera (MP)'] * df['Storage (GB)']

# One-Hot Encoding
df = pd.get_dummies(df, columns=['Brand', 'Processor'], drop_first=True)

# Define Features and Target
X = df.drop('Price (USD)', axis=1) 
y = df['Price (USD)']

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split with K-Fold Cross Validation
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# XGBoost Model with Improved Hyperparameter Tuning and K-Fold CV
xgb_model = XGBRegressor(random_state=42)

param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [5, 6],
    'learning_rate': [0.05, 0.1],
    'min_child_weight': [1, 2],
    'subsample': [0.8, 0.9],
    'colsample_bytree': [0.8, 0.9],
    'gamma': [0, 0.1],
    'reg_alpha': [0, 0.1],
    'reg_lambda': [1, 1.5]
}

kf = KFold(n_splits=5, shuffle=True, random_state=42)
grid_search = GridSearchCV(estimator=xgb_model, param_grid=param_grid, cv=kf, n_jobs=-1, scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)

# Evaluation
print("Best Parameters:", grid_search.best_params_)
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', rmse)
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('R2 Score:', r2_score(y_test, y_pred))

joblib.dump(best_model, 'best_xgboost_model.pkl')
print("Model saved as best_xgboost_model.pkl")

# Results and Plot
results_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print(results_df.head())

plt.figure(figsize=(8, 6))
sns.scatterplot(x='Actual', y='Predicted', data=results_df)
plt.plot([results_df['Actual'].min(), results_df['Actual'].max()], [results_df['Actual'].min(), results_df['Actual'].max()], color='red')
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.savefig('actual_vs_predicted.png')
plt.show()
plt.close()
