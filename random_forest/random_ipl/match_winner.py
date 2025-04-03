import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset (replace with actual file path)
df = pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\random_forest\random_ipl\match_info_data.csv')

### **1. Data Cleaning** ###
# Drop unwanted columns
df.drop(columns=['id', 'date', 'dl_applied', 'player_of_match', 'umpire1', 'umpire2', 'umpire3'], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.dropna(inplace=True)

# Remove outliers (win_by_runs & win_by_wickets)
df = df[(df['win_by_runs'] < df['win_by_runs'].quantile(0.95)) & 
        (df['win_by_wickets'] < df['win_by_wickets'].quantile(0.95))]

### **2. Feature Encoding** ###
# Encode categorical variables
encoders = {}
for col in ['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'result', 'winner']:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col])

# Define features and target
X = df[['team1', 'team2', 'toss_winner', 'toss_decision', 'venue', 'result']]
y = df['winner']  # Winner as encoded values

### **3. Train-Test Split** ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### **4. Train Random Forest Model** ###
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluate Model
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

### **5. Predict on a Single Match with Team Names** ###
def predict_winner(team1, team2, toss_winner, toss_decision, venue, result):
    # Convert input values to encoded form
    new_match = pd.DataFrame([[team1, team2, toss_winner, toss_decision, venue, result]], columns=X.columns)
    
    for col in new_match.columns:
        new_match[col] = encoders[col].transform(new_match[col])
    
    # Make prediction
    winner_encoded = rf.predict(new_match)[0]
    
    # Convert back to team name
    winner_team = encoders['winner'].inverse_transform([winner_encoded])[0]
    
    return winner_team

### **6. Example Prediction** ###
match_winner = predict_winner(
    team1="Gujarat Titans", 
    team2="Chennai Super Kings", 
    toss_winner="Chennai Super Kings", 
    toss_decision="field", 
    venue="Narendra Modi Stadium, Ahmedabad", 
    result="D/L"
)
print(f"Predicted Winner: {match_winner}")
