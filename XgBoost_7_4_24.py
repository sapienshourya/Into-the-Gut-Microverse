import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('/home/group16/MLBIO/COdes for cleaning/AgeAdded/combinedAll.csv')  


label_column = 'Study.Group'  


X = data.drop(label_column, axis=1)
y = data[label_column]

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)


X = pd.get_dummies(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = xgb.XGBClassifier()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)