import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\match_info_data.csv')

# Convert date column to datetime
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)  # Drop missing dates
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df.drop(columns=['date'], inplace=True)

# Handle missing values
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])
df.fillna(df.select_dtypes(include='number').median(), inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Drop irrelevant columns
df.drop(columns=['id', 'umpire1', 'umpire2', 'umpire3'], inplace=True)

# Remove outliers
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# Apply one-hot encoding AFTER removing outliers
df = pd.get_dummies(df, columns=['season', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'venue'], drop_first=True)

# Define features and target variables
features = df.drop(columns=['win_by_runs', 'win_by_wickets', 'winner', 'player_of_match'])
target_runs = pd.to_numeric(df['win_by_runs'], errors='coerce').fillna(0)

# Ensure all features are numeric
features = features.select_dtypes(include=['number'])

# Scale the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(features)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_scaled, target_runs, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Evaluate and predict
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Identify important features
feature_importances = pd.Series(model.feature_importances_, index=features.columns).sort_values(ascending=False)
print('Feature Importances:', feature_importances)

# Actual vs Predicted values
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print(comparison_df.head(10))


















# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# from sklearn.calibration import LabelEncoder
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error,r2_score
# from sklearn.preprocessing import StandardScaler

# #load the dataset
# df=pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\match_info_data.csv')
# print(df.head())

# #checking missing values
# print(df.isnull().sum())

# #convert date column to datetime
# if 'date' in df.columns:
#     df['date'] = pd.to_datetime(df['date'], errors='coerce')

# #fill missing values for categorical columns using mode
# for col in df.select_dtypes(include='object').columns:
#     df[col] = df[col].fillna(df[col].mode()[0])

# #fill missing values for numerical columns using median
# df.fillna(df.select_dtypes(include='number').median(),inplace=True)

# #remove duplicates
# df.drop_duplicates(inplace=True)    

# #extract useful features from date column
# if 'date' in df.columns:
#     df['year'] = df['date'].dt.year
#     df['month'] = df['date'].dt.month
#     df['day'] = df['date'].dt.day
#     df.drop(columns=['date'], inplace=True)  

# # Drop 'id' as it's not useful for predictions
# df.drop(columns=['id'], inplace=True)

# # Drop 'umpire' columns since they don't impact match outcome
# df.drop(columns=['umpire1', 'umpire2', 'umpire3'], inplace=True)    

# #visualize outliers using box plot
# sns.boxplot(data=df)
# plt.show()

# #removing outliers
# numeric_cols = df.select_dtypes(include=['number']).columns

# for col in numeric_cols:
#     Q1 = df[col].quantile(0.25)
#     Q3 = df[col].quantile(0.75)
#     IQR = Q3 - Q1
#     lower_bound = Q1 - 1.5 * IQR
#     upper_bound = Q3 + 1.5 * IQR

#     # Remove outliers
#     df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

# print("Outliers removed!")

# #apply one-hot encoding for categorical cols
# df = pd.get_dummies(df, columns=['season', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'venue'], drop_first=True)

# #selecting features and target variables 
# features = df.drop(columns=['win_by_runs', 'win_by_wickets', 'winner', 'player_of_match'])
# target_runs = df['win_by_runs']
# target_wickets = df['win_by_wickets']

# # Identify remaining non-numeric columns
# print("Feature column types:\n", features.dtypes)

# # Convert any remaining categorical columns
# categorical_cols = features.select_dtypes(include=['object']).columns
# if len(categorical_cols) > 0:
#     print("Categorical columns found:", categorical_cols)
#     features = pd.get_dummies(features, columns=categorical_cols, drop_first=True)

# # Ensure all features are numeric before scaling
# features = features.select_dtypes(include=['number'])

# #scaling
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(features)

# #split the dataset
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, target_runs, test_size=0.2, random_state=42)

# #tune and train the model
# model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
# model.fit(X_train, y_train)

# # evaluate and predict the model
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# r2 = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R2 Score:", r2)

# #Identify important features
# feature_importances = pd.Series(model.feature_importances_, index=features.columns).sort_values(ascending=False)
# print('feature_importances:', feature_importances)

# #actual and predicted values
# comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
# print(comparison_df.head(10))
