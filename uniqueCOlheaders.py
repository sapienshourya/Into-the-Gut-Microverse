import os
import pandas as pd

def count_unique_column_headers(folder_path):
    
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    
    
    unique_headers = set()

    
    for file in csv_files:
        
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)

        
        standardized_headers = [header.strip().lower() for header in df.columns]

        
        unique_headers.update(standardized_headers)
    
    
    print("Total number of unique column headers:", len(unique_headers))
    print("Unique column headers:", unique_headers)



count_unique_column_headers('/home/group16/MLBIO/COdes for cleaning/AgeAdded')
