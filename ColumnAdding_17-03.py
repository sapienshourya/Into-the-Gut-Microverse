import pandas as pd

def insert_column(source_csv, dest_csv, column_header, insert_column_index):
    
    source_df = pd.read_csv(source_csv)
    
    
    selected_column = source_df[column_header]
    
    
    dest_df = pd.read_csv(dest_csv)
    
    
    dest_df.insert(insert_column_index, column_header, selected_column)
    
    
    dest_df.to_csv("output.csv", index=False)


source_csv = "/home/group16/MLBIO/COdes for cleaning/Microbiome data/Column and COmbined data/4 column metadata/ERAWIJINTARI_4_col_age_range.csv"  
dest_csv = "/home/group16/MLBIO/COdes for cleaning/Microbiome data/Only labels and features/modified_ERAWINJINTARI_combined_modified.csv"  
column_header = "Age Group"  
insert_column_index = 1  

insert_column(source_csv, dest_csv, column_header, insert_column_index)

