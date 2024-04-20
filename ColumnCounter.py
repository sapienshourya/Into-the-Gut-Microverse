import csv

def count_columns(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        first_row = next(reader)
        num_columns = len(first_row)
        return num_columns


csv_file = '/home/group16/MLBIO/COdes for cleaning/AJ ka kam/processed_all_combined.csv'
num_columns = count_columns(csv_file)
print(f"The CSV file has {num_columns} columns.")

