import pandas as pd
import os
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

def train_and_save_model():
    # Load dataset
    df = pd.read_csv("data/loan_data.csv")

    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))

    # Remove duplicates
    df = df.drop_duplicates()

    # Define features and target
    X = df[['Age', 'MonthlySalary', 'NumberOfYearsStudied', 'FScore']]
    y = df['LoanAmountApproved']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train model
    model = LinearRegression()
    model.fit(X_scaled, y)

    # Save model and scaler
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")

if __name__ == "__main__":
    train_and_save_model()
