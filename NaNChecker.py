import pandas as pd


data = pd.read_csv('/home/group16/MLBIO/COdes for cleaning/164normal_Yachida.csv')


nan_values = data.isna().sum()


missing_values = data.isnull().values.any()

if missing_values:
    print("There are missing values in the DataFrame.")
    print("Number of NaN values in each column:")
    print(nan_values)
else:
    print("There are no missing values in the DataFrame.")
