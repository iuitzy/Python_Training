import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler
 
 
#load the dataset
df=pd.read_csv(r'C:\Users\bhavithar\OneDrive - Maveric Systems Limited\Desktop\py_Basic\Python_Training\random_forest_algo\smartphone_data.csv')
print(df.head())    
 
#checking missing values
print(df.isnull().sum())    
 
#fill missing values for categorical columns using mode
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])
 
#fill missing values for numerical columns using median
df.fillna(df.select_dtypes(include='number').median(),inplace=True)
 
#remove duplicates
df.drop_duplicates(inplace=True)
 
#visualize outliers using box plot
sns.boxplot(data=df)
plt.show()
 
#apply one-hot encoding for categorical cols
df=pd.get_dummies(df, columns=['Brand','processor'], drop_first=True)
 
#scaling
scaler = StandardScaler()
x=df.drop('Price(USD)',axis=1)
y=df['Price(USD)']
x_scaled = scaler.fit_transform(x)
 
#split the dataset
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
   
#tune and train the model
model = RandomForestRegressor(n_estimators=200, max_depth=10, random_state=42)
model.fit(x_train, y_train)
 
#evaluate the model
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred) #actual and predicted values
r2 = r2_score(y_test, y_pred)  
print("Mean Squared Error:",mse)
print("R2 Score:",r2)
 
#Identify important features
feature_importances = pd.series(model.feature_importances_, index=x.columns).sort_values(ascending=False)
print('feature_importances:',feature_importances)  