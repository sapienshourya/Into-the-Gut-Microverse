 import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('/home/group16/MLBIO/COdes for cleaning/Uncommon/modified_SINHA_combined_filtered.csv')


features = data.drop('Study.Group', axis=1)
labels = data['Study.Group']


for column in features.columns:
    if features[column].dtype == 'object':
        encoder = LabelEncoder()
        features[column] = encoder.fit_transform(features[column])


X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)


rf = RandomForestClassifier()


rf.fit(X_train, y_train)


accuracy = rf.score(X_test, y_test)
print("Accuracy:", accuracy)