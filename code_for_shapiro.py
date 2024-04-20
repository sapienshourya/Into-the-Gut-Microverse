import pandas as pd
from scipy.stats import shapiro

data = pd.read_csv("/home/group16/MLBIO/Shourya doing work/normalized_data_yachida.csv")

healthy_group = data[data['Study.Group'] == 'Healthy']
gastrectomy_group = data[data['Study.Group'] == 'Cancer']

total_columns = len(data.columns) - 1  
non_normal_columns_count = {'Healthy': 0, 'Cancer': 0}

for column in data.columns:
    if column != 'Study.Group': 
        healthy_abundance = pd.to_numeric(healthy_group[column], errors='coerce').dropna()
        if len(healthy_abundance) >= 3: 
            stat_h, p_value_h = shapiro(healthy_abundance)
            if p_value_h < 0.05:
                non_normal_columns_count['Healthy'] += 1
        gastrectomy_abundance = pd.to_numeric(gastrectomy_group[column], errors='coerce').dropna()
        if len(gastrectomy_abundance) >= 3:  
            stat_g, p_value_g = shapiro(gastrectomy_abundance)
            if p_value_g < 0.05:
                non_normal_columns_count['Cancer'] += 1

non_normal_percentage = {group: (count / total_columns) * 100 for group, count in non_normal_columns_count.items()}

print("Percentage of non-normal columns for Healthy group:", non_normal_percentage['Healthy'], "%")
print("Percentage of non-normal columns for Cancer group:", non_normal_percentage['Cancer'], "%")