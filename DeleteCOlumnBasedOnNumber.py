import pandas as pd
import os

def remove_columns_and_save(input_folder, output_folder, columns_to_remove):
    
    files = os.listdir(input_folder)
    
    
    for file in files:
        if file.endswith('.csv'):
            file_path = os.path.join(input_folder, file)
            
            
            data = pd.read_csv(file_path)
            
            
            data = data.drop(data.columns[columns_to_remove], axis=1)
            
            
            output_file_path = os.path.join(output_folder, f'modified_{file}')
            
            
            data.to_csv(output_file_path, index=False)
            
            print(f"Modified data saved to '{output_file_path}'.")


input_folder = '/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined'
output_folder = '/home/group16/MLBIO/COdes for cleaning/AgeAdded'


columns_to_remove = [0,1]  


remove_columns_and_save(input_folder, output_folder, columns_to_remove)

