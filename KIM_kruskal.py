import pandas as pd
from scipy.stats import kruskal
import numpy as np

df = pd.read_csv("/home/group16/MLBIO/COdes for cleaning/Microbiome data/Normal/normal_KIM.csv")

groups = df['Study.Group'].unique()
features = df.columns.difference(['Study.Group', 'Age Group'])

p_values = {}

for feature in features:
    data_groups = [df[df['Study.Group'] == group][feature].dropna() for group in groups]

    uniform_or_empty = any(len(data) == 0 or np.unique(data).size == 1 for data in data_groups)
    if uniform_or_empty:
        print(f'Skipping {feature} because it is uniform or one or more groups are empty.')
        continue

    try:
        stat, p = kruskal(*data_groups)
        p_values[feature] = p
    except ValueError as e:
        print(f"Error processing feature {feature}: {e}")

significance_threshold = 0.05

significant_features = [feature for feature, p_value in p_values.items() if p_value < significance_threshold]

significant_data = df[['Study.Group', 'Age Group'] + significant_features]

output_csv_file = "significant_features_data_KIM_kruskal.csv"
significant_data.to_csv(output_csv_file, index=False)

print(f"CSV file containing significant features data saved to '{output_csv_file}'")

