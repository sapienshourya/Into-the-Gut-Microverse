from scipy.stats import ttest_ind
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/home/group16/MLBIO/Shourya doing work/Final file/Mars_RFECV.csv")

healthy_group = data[data['Study.Group'] == 'Healthy']
IBS_group = data[data['Study.Group'] == 'IBS']


p_values = {}
for column in data.columns:
    if column != 'Study.Group':  # Skip the 'Study.Group' column
        healthy_abundance = pd.to_numeric(healthy_group[column], errors='coerce')
        IBS_abundance = pd.to_numeric(IBS_group[column], errors='coerce')
        healthy_abundance = healthy_abundance.dropna()
        IBS_abundance = IBS_abundance.dropna()
        t_statistic, p_value = ttest_ind(healthy_abundance, IBS_abundance)
        p_values[column] = p_value

for column, p_value in p_values.items():
    print(f"Column: {column}, P-value: {p_value}")

import numpy as np

significance_threshold = 0.05

significant_features = []
non_significant_features = []

for feature, p_value in p_values.items():
    if np.isnan(p_value):
        print(f"Column: {feature}, P-value: NaN")
    elif p_value < significance_threshold:
        significant_features.append(feature)
        print(f"Column: {feature}, P-value: {p_value}, Significant")
    else:
        non_significant_features.append(feature)
        print(f"Column: {feature}, P-value: {p_value}, Not Significant")

print(f"Number of significant features: {len(significant_features)}")
print(f"Number of non-significant features: {len(non_significant_features)}")

for feature in significant_features:
    data.boxplot(column=feature, by='Study.Group', figsize=(8, 6))
    plt.title(f'Box plot for {feature}')
    plt.ylabel('Abundance')
    plt.xlabel('Study Group')
    plt.show()
