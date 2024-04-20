import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(input_file, output_train_file, output_test_file, test_size=0.2, random_state=42):
    
    data = pd.read_csv(input_file)
    
    
    X = data.drop(columns=['Study.Group'])  
    y = data['Study.Group']  
    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    
    train_data = pd.concat([y_train, X_train], axis=1)
    test_data = pd.concat([y_test, X_test], axis=1)
    
    
    train_data.to_csv(output_train_file, index=False)
    test_data.to_csv(output_test_file, index=False)


input_file = "/home/group16/MLBIO/COdes for cleaning/combined_output.csv"
output_train_file = "/home/group16/MLBIO/COdes for cleaning/combined_train_output.csv"
output_test_file = "/home/group16/MLBIO/COdes for cleaning/combined_test_output.csv"
split_data(input_file, output_train_file, output_test_file, test_size=0.2, random_state=42)

