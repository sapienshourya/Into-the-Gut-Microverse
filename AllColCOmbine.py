import os
import pandas as pd


def combine_csv_files(folder_path, output_file):
    
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
   
    
    unique_columns = set()
   
    
    for file in csv_files:
        
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
       
        
        unique_columns.update(df.columns)
   
    
    unique_columns = list(unique_columns)
   
    
    if 'Study.Group' in unique_columns:
        unique_columns.remove('Study.Group')
    if 'Age Group' in unique_columns:
        unique_columns.remove('Age Group')
    unique_columns = ['Study.Group', 'Age Group'] + unique_columns
   
    
    combined_data = pd.DataFrame(columns=unique_columns)
   
    
    for file in csv_files:
        
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
       
        
        df = df.reindex(columns=unique_columns, fill_value=0)
       
        
        combined_data = pd.concat([combined_data, df], ignore_index=True)
   
    
    combined_data.to_csv(output_file, index=False)
    print(f"Combined CSV file saved to: {output_file}")



combine_csv_files('/home/group16/MLBIO/Shourya doing work/Final file', '/home/group16/MLBIO/COdes for cleaning/AJ ka kam/processed_all_combined.csv')