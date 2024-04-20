from scipy.stats import mannwhitneyu
import pandas as pd
data = pd.read_csv("/home/group16/MLBIO/COdes for cleaning/164normal_Yachida.csv")

healthy_group = data[data['Study.Group'] == 'Healthy']
Cancer_group = data[data['Study.Group'] == 'Cancer']

p_values = {}
significant_features = []

for column in data.columns:
    if column != 'Study.Group': 
        healthy_abundance = pd.to_numeric(healthy_group[column], errors='coerce').dropna()
        IBS_abundance = pd.to_numeric(Cancer_group[column], errors='coerce').dropna()
        
        if len(healthy_abundance) > 0 and len(IBS_abundance) > 0:
            statistic, p_value = mannwhitneyu(healthy_abundance, IBS_abundance, alternative='two-sided')
            p_values[column] = p_value
            
            if p_value < 0.05:
                significant_features.append(column)
        else:
            print(f"Warning: '{column}' has no data after dropping NaN values.")

for column, p_value in p_values.items():
    significance = "Significant" if column in significant_features else "Not Significant"
    print(f"Column: {column}, P-value: {p_value}, {significance}")

print(f"Number of significant features: {len(significant_features)}")
print(f"Number of non-significant features: {len(p_values) - len(significant_features)}")

significant_data = data[significant_features]

age_group_column = data['Age Group']

study_group_column = data['Study.Group']

significant_data = pd.concat([study_group_column, age_group_column, significant_data], axis=1)

csv_file_path = '/home/group16/MLBIO/COdes for cleaning/MannWhitneyU_Yachida.csv'

significant_data.to_csv(csv_file_path, index=False)

print(f"CSV file containing significant features, 'Study.Group', and 'Age Group' from the original dataset saved to '{csv_file_path}'.")
