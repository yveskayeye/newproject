import pandas as pd # to put data into dataframes
import numpy as np #  for making arrays
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split # allows us to split data into Train and Test Data
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv("app/add/Maternal Health Risk Data Set.csv")

dataset2 = dataset.drop_duplicates()

X=dataset.drop(['RiskLevel'], axis=1)
y=dataset['RiskLevel']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1,
                                                    random_state =2)

models = RandomForestClassifier(max_features= 5, n_estimators=250, max_depth=15, random_state=1)
b = models.fit(X_train, y_train)

def get_prediction(record):
    y_pred1 = b.predict([record])
    prediction = y_pred1[0]
    return prediction