import pandas as pd

def normalize_data_and_save(csv_file_path, output_csv_file):
    df = pd.read_csv("/home/group16/MLBIO/COdes for cleaning/AgeAdded/modified_MARS_combined.csv")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = (df[numeric_columns] - df[numeric_columns].min()) / (df[numeric_columns].max() - df[numeric_columns].min())
    df.to_csv(output_csv_file, index=False)
    print(f"Normalized CSV file saved to '{output_csv_file}'.")

csv_file_path = 'your_data.csv'
output_csv_file = 'normalized_data_MArs.csv'
normalize_data_and_save(csv_file_path, output_csv_file)

