import pandas as pd
from scipy.stats import kruskal
from statsmodels.stats.multitest import multipletests

df = pd.read_csv("/home/group16/MLBIO/shourya doing experiment/normalized_data_franzosa.csv")

groups = ['CD', 'UC', 'Healthy']

features = df.columns.drop(['Study.Group', 'Age Group'])

p_values = {}

for feature in features:
    data_groups = [df[df['Study.Group'] == group][feature] for group in groups]
    
    stat, p = kruskal(*data_groups)
    p_values[feature] = p

p_adjusted = multipletests(list(p_values.values()), method='fdr_bh')[1]

adjusted_p_values = dict(zip(p_values.keys(), p_adjusted))

significant_features = {feature: p for feature, p in adjusted_p_values.items() if p < 0.05}

significant_df = df[['Study.Group', 'Age Group'] + list(significant_features.keys())]

significant_df.to_csv("significant_features_FRANZOSA.csv", index=False)

print("CSV file containing significant features, 'Study.Group', and 'Age Group' saved successfully.")
