import os
import pandas as pd
from sklearn.model_selection import train_test_split

input_directory = "/home/group16/MLBIO/Shourya doing work/Final file" 
output_train_directory = "Processed_output_train_folder"  
output_test_directory = "Processed_output_test_folder"  

os.makedirs(output_train_directory, exist_ok=True)
os.makedirs(output_test_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_directory, filename)
        data = pd.read_csv(file_path)
        X = data.drop(columns=['target_column'])  
        y = data['target_column']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        train_data = pd.concat([X_train, y_train], axis=1)
        test_data = pd.concat([X_test, y_test], axis=1)
        train_output_path = os.path.join(output_train_directory, f"train_{filename}")
        test_output_path = os.path.join(output_test_directory, f"test_{filename}")

        train_data.to_csv(train_output_path, index=False)
        test_data.to_csv(test_output_path, index=False)

        print(f"Training and testing datasets saved successfully for {filename}.")
