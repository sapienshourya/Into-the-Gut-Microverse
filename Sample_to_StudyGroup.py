import pandas as pd
import os

def remove_columns_by_label(csv_files, columns_to_remove, output_folder):
    for csv_file in csv_files:
        
        data = pd.read_csv(csv_file)

        
        data.drop(columns=columns_to_remove, inplace=True, errors='ignore')

        
        output_csv = os.path.join(output_folder, f"modified_{os.path.basename(csv_file)}")

        
        data.to_csv(output_csv, index=False)
        print(f"Modified CSV file saved: {output_csv}")


csv_files = ["/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/ERAWINJINTARI_combined.csv", "/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/FRANZOSA_combined.csv",'/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/iHMP_combined.csv','/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/KIM ADENOMAS_combined.csv','/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/MARS_combined.csv','/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/SINHA_combined.csv','/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/COmbined/YACHIDA_combined.csv']  
columns_to_remove = ['Dataset', 'Age Group']  
output_folder = "/home/group16/MLBIO/COdes for cleaning/Microbiome data/SampleToStudyNumber"  

remove_columns_by_label(csv_files, columns_to_remove, output_folder)




