from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\match_info_data.csv')  # Update with actual dataset file

### Step 1: Drop unwanted columns
columns_to_drop = ['id', 'date', 'player_of_match', 'venue', 'umpire1', 'umpire2', 'umpire3','city']
df.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Boxplot before removing outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['win_by_runs', 'win_by_wickets']])
plt.title("Box Plot Before Removing Outliers")
plt.show()

### Step 2: Handle missing values
# Fill numerical missing values with median
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())

# Fill categorical missing values with mode
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

### Step 3: Handle Outliers using IQR
Q1 = df[num_cols].quantile(0.25)
Q3 = df[num_cols].quantile(0.75)
IQR = Q3 - Q1

# Define outlier range
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
for col in num_cols:
    df = df[(df[col] >= lower_bound[col]) & (df[col] <= upper_bound[col])]

# Boxplot after removing outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['win_by_runs', 'win_by_wickets']])
plt.title("Box Plot After Removing Outliers")
plt.show()


### Step 4: Create margin_of_victory column
df['margin_of_victory'] = np.where(df['win_by_runs'] > 0, df['win_by_runs'], df['win_by_wickets'])

# Convert to CSV
df.to_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\less.csv', index=False)

# Drop original target columns
df.drop(columns=['win_by_runs', 'win_by_wickets'], inplace=True)

### Step 5: Encode categorical variables
df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

### Step 6: Define features (X) and target variable (y)
X = df.drop(columns=['margin_of_victory'])
y = df['margin_of_victory']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### Step 7: Scale numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

### Step 8: Train the RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100,max_depth=10, random_state=42)
model.fit(X_train_scaled, y_train)

### Step 9: Make predictions
y_pred = model.predict(X_test_scaled)

### Step 10: Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# Feature importance
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print('Feature Importances:')
print(feature_importances)

#print the model actual and predict value 
print(y_test,y_pred)

input_data = {
    'season': 2023,
    'team1': 'Royal Challengers Bangalore',
    'team2': 'Lucknow Super Giants',
    'toss_winner': 'Lucknow Super Giants',
    'toss_decision': 'field',
    'result': 'normal',
    'dl_applied': 0,
    'winner': 'Lucknow Super Giants',
    'team1_wins': 0,
    'team2_wins': 1,
    'previous_encounters': 1
}

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

# Encode categorical variables (same as training)
input_df = pd.get_dummies(input_df, columns=cat_cols, drop_first=True)

# Ensure all features match the training data
missing_cols = set(X.columns) - set(input_df.columns)
for col in missing_cols:
    input_df[col] = 0

# Reorder columns to match training set
input_df = input_df[X.columns]

# Scale numerical features
input_scaled = scaler.transform(input_df)

# Predict using the trained model
predicted_margin = model.predict(input_scaled)

# Print the predicted margin of victory
print(f"Predicted Margin of Victory: {predicted_margin[0]:.2f}")












#import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# # Load the dataset
# df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\match_info_data.csv')  # Update with actual dataset file

# date_columns = ['date']  
# df.drop(columns=date_columns, errors='ignore', inplace=True)

# # Create margin_of_victory column
# df['margin_of_victory'] = np.where(df['win_by_runs'] > 0, df['win_by_runs'], df['win_by_wickets'])

# # Drop the original columns (optional)
# df.drop(columns=['win_by_runs', 'win_by_wickets'], inplace=True)

# # Identify categorical columns
# categorical_cols = df.select_dtypes(include=['object']).columns

# # One-hot encode categorical columns
# df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# # Define features (X) and target variable (y)
# X = df.drop(columns=['margin_of_victory'])  # Features
# y = df['margin_of_victory']  # Target

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Standardize the features
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Train the RandomForestRegressor model
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train_scaled, y_train)

# # Make predictions
# y_pred = model.predict(X_test_scaled)

# # Evaluate the model
# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)

# # Print evaluation metrics
# print(f"Mean Absolute Error (MAE): {mae}")
# print(f"Mean Squared Error (MSE): {mse}")
# print(f"R-squared (R²): {r2}")
