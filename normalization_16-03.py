import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_csv(input_file, output_file, columns_to_exclude):
    
    df = pd.read_csv(input_file)
    
    
    columns_to_normalize = df.columns.difference(columns_to_exclude)
    
    
    scaler = MinMaxScaler()
    df[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])
    
    
    df.to_csv(output_file, index=False)




input_file = "/home/group16/MLBIO/COdes for cleaning/AgeAdded/modified_SINHA_combined.csv"  
output_file = "/home/group16/MLBIO/Shourya doing work/Final file/normal_sinha.csv"  
columns_to_exclude = ['Study.Group','Age Group']  

normalize_csv(input_file, output_file, columns_to_exclude)
