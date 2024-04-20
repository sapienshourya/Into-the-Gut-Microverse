import os
import pandas as pd

def process_files(input_folder, output_folder, reference_file):
    os.makedirs(output_folder, exist_ok=True)

    reference_df = pd.read_csv(reference_file)
    reference_columns = reference_df.columns

    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            df = pd.read_csv(file_path)

            common_columns = set(df.columns).intersection(reference_columns)
            df_filtered = df[common_columns]

            df_reordered = df_filtered[reference_columns]

            output_path = os.path.join(output_folder, filename)
            df_reordered.to_csv(output_path, index=False)

input_folder = "/home/group16/MLBIO/COdes for cleaning/AJ ka kam/unprocessed test"
output_folder = "/home/group16/MLBIO/COdes for cleaning/AJ ka kam/unprocessed test only common"
reference_file = "/home/group16/MLBIO/COdes for cleaning/AJ ka kam/Unprocessesed_Train_OnlyCommon.csv"

process_files(input_folder, output_folder, reference_file)
