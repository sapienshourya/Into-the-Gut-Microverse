import pandas as pd

# Read data from a TSV file
file_path = '/home/group16/MLBIO/microbiome-metabolome-curated-data/data/processed_data/ERAWIJANTARI_GASTRIC_CANCER_2020/genera.tsv'  # Replace 'your_file.tsv' with the path to your TSV file
data = pd.read_csv(file_path, sep='\t')

# Check for missing values
missing_values_column = data.isnull().sum()
missing_values_row = data.isnull().sum(axis=1)

# Calculate percentage of missing values
total_rows = len(data)
total_columns = len(data.columns)
percentage_missing_column = (missing_values_column / total_rows) * 100
percentage_missing_row = (missing_values_row / total_columns) * 100

# Print missing values counts and percentages
print("Missing Values Counts - Columns:")
print(missing_values_column)
print("\nMissing Values Counts - Rows:")
print(missing_values_row)

print("\nPercentage of Missing Values - Columns:")
print(percentage_missing_column)
print("\nPercentage of Missing Values - Rows:")
print(percentage_missing_row)
