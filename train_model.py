import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load Dataset
df = pd.read_csv("StudentsPerformance.csv")

# Label Encoding
le = LabelEncoder()

df['gender'] = le.fit_transform(df['gender'])
df['race/ethnicity'] = le.fit_transform(df['race/ethnicity'])
df['parental level of education'] = le.fit_transform(df['parental level of education'])
df['lunch'] = le.fit_transform(df['lunch'])
df['test preparation course'] = le.fit_transform(df['test preparation course'])

# Features and Target
X = df.drop('math score', axis=1)
y = df['math score']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Model Training
model = RandomForestRegressor()

model.fit(X_train, y_train)

# Save Model
joblib.dump(model, "model.pkl")

print("Model Saved Successfully")