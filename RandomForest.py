import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

def train_and_evaluate(train_folder, test_folder):
    results = []
    
    for train_file, test_file in zip(sorted(os.listdir(train_folder)), sorted(os.listdir(test_folder))):
        train_data = pd.read_csv(os.path.join(train_folder, train_file))
        X_train = train_data.drop(columns=['Study.Group'])#,'Age Group'])
        y_train = train_data['Study.Group']
        
        test_data = pd.read_csv(os.path.join(test_folder, test_file))
        X_test = test_data.drop(columns=['Study.Group'])#,'Age Group'])
        y_test = test_data['Study.Group']
        
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_classifier.fit(X_train, y_train)
        
        y_pred = rf_classifier.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='weighted')
        results.append((train_file, test_file, accuracy, f1))
    
    return results

train_folder = "/home/group16/MLBIO/Shourya doing work/AAJ_KA_KAAM/Processed_data/Processed_output_train_folder"
test_folder = "/home/group16/MLBIO/Shourya doing work/AAJ_KA_KAAM/Processed_data/Processed_output_test_folder"

results = train_and_evaluate(train_folder, test_folder)

for i, (train_file, test_file, accuracy, f1) in enumerate(results, 1):
    print(f"File {i}: Train: {train_file}, Test: {test_file}, Accuracy: {accuracy}, F1 Score: {f1}")
