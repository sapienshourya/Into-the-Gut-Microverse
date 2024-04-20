import pandas as pd

def remove_columns_with_high_zeros_and_save(csv_file_path, output_csv_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv("/home/group16/MLBIO/shourya doing experiment/erawa_selected_columns_mtb_final.csv")

    # Exclude the first column from analysis
    columns_to_check = df.columns[1:]
    
    # Calculate the percentage of zero values in each column
    zero_percentages = (df[columns_to_check] == 0).mean() * 100
    
    # Identify columns with more than 50% zero values
    columns_to_remove = zero_percentages[zero_percentages > 50].index.tolist()
    
    # Remove identified columns
    df_filtered = df.drop(columns=columns_to_remove)
    
    # Save the filtered DataFrame to a new CSV file
    df_filtered.to_csv(output_csv_file, index=False)
    print(f"Filtered CSV file saved to '{output_csv_file}'.")

# Example usage:
# Specify the input CSV file and the desired output CSV file
csv_file_path = 'your_data.csv'  # Replace 'your_data.csv' with the path to your CSV file
output_csv_file = 'filtered_data_erawa.csv'  # Specify the desired output CSV file path

# Call the function to remove columns with more than 50% zeros and save the filtered DataFrame to a new CSV file
remove_columns_with_high_zeros_and_save(csv_file_path, output_csv_file)
