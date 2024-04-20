from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
import pandas as pd

df = pd.read_csv("/home/group16/MLBIO/Shourya doing work/MArs_significant_data_mannwhitneyu.csv")
X = df.drop(['Study.Group', 'Age Group'], axis=1)
y = df['Study.Group']

estimator = RandomForestClassifier(n_estimators=100, random_state=42)
selector = RFECV(estimator, step=1, cv=StratifiedKFold(5), scoring='accuracy')
selector = selector.fit(X, y)

X_reduced = X.iloc[:, selector.support_]

reduced_df = pd.concat([df[['Study.Group', 'Age Group']], X_reduced], axis=1)

reduced_df.to_csv("Mars_RFECV.csv", index=False)

