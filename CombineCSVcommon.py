import pandas as pd
import os

def find_common_columns(folder_path):
    common_columns = None
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            if common_columns is None:
                common_columns = set(df.columns)
            else:
                common_columns = common_columns.intersection(df.columns)
    return common_columns

def combine_csv_files_common_columns(folder_path, common_columns):
    combined_data = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_csv(file_path)
            common_columns_data = df[list(common_columns)]
            combined_data.append(common_columns_data)
    combined_df = pd.concat(combined_data, axis=0, ignore_index=True)
    
    combined_df = combined_df[['Study.Group', 'Age Group'] + [col for col in combined_df.columns if col not in ['Study.Group', 'Age Group']]]
    return combined_df


folder_path = '/home/group16/MLBIO/COdes for cleaning/AJ ka kam/Unprocessed train'


common_columns = find_common_columns(folder_path)
print("Common Columns:", common_columns)


combined_df = combine_csv_files_common_columns(folder_path, common_columns)


output_file_path = os.path.join('/home/group16/MLBIO/COdes for cleaning/AJ ka kam/', 'Unprocessesed_Train_OnlyCommon.csv')

combined_df.to_csv(output_file_path, index=False)

print(f"Combined CSV file with common columns saved at: {output_file_path}")
