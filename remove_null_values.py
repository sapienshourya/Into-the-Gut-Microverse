import pandas as pd

data = pd.read_csv("/home/group16/MLBIO/Shourya doing work/_ERAWA_scaled_data.csv")

threshold = 100 
null_counts = data.isnull().sum()
low_count_features = null_counts[null_counts < threshold]


for feature, count in low_count_features.items():
    if count == 0:
        print(f"No missing values in feature: {feature}")
    else:
        print(f"Missing values in feature {feature}: {count}")

def feature_essential_for_analysis(feature):
    return True  

def impute_missing_values(data, feature):
    pass


for feature, count in low_count_features.items():
    if count == 0:
        continue  
    if feature_essential_for_analysis(feature):
        impute_missing_values(data, feature)
    else:
         data.drop(columns=[feature], inplace=True)

data.to_csv("ERAWA_cleaned_dataset.csv", index=False)