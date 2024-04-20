from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def train_model(data, features):
    X = data[features]
    y = data['Study.Group']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

original_df = pd.read_csv("/home/group16/MLBIO/Shourya doing work/significant_features_FRANZOSA.csv")
further_reduced_df = pd.read_csv("/home/group16/MLBIO/Shourya doing work/further_reduced_features_FRANZOSA.csv")

original_features = original_df.drop(['Study.Group', 'Age Group'], axis=1).columns
further_reduced_features = further_reduced_df.drop(['Study.Group', 'Age Group'], axis=1).columns

original_accuracy = train_model(original_df, original_features)
reduced_accuracy = train_model(further_reduced_df, further_reduced_features)

print("Accuracy with original significant features:", original_accuracy)
print("Accuracy with further reduced features:", reduced_accuracy)
