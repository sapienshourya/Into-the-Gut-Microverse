

import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('/home/group16/MLBIO/COdes for cleaning/Microbiome data/Trials/REFKimAdenomas.csv')


X = data.iloc[:, 1:]  
y = data.iloc[:, 0]   


label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)


dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)


params = {
    'objective': 'multi:softmax',    
    'num_class': len(np.unique(y_train)),  
    'eval_metric': 'merror'          
}


num_rounds = 100  
model = xgb.train(params, dtrain, num_rounds)


y_pred = model.predict(dtest)


y_pred_decoded = label_encoder.inverse_transform(y_pred.astype(int))


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
