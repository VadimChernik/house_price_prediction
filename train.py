import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor

OUTPUT_FILE = 'model.bin'
SEED = 42

df = pd.read_csv('data/train.csv')

df.columns = df.columns.str.lower().str.replace(' ', '_')

del df['id']

df['garageyrblt'] = df['garageyrblt'].fillna(value=df['garageyrblt'].median())
df['masvnrarea'] = df['masvnrarea'].fillna(value=df['masvnrarea'].median())

# df.dropna(inplace=True)

df['age'] = 2025 - df['yearbuilt'].astype(int)
df['totalsf'] = df['totalbsmtsf'] + df['1stflrsf'] + df['2ndflrsf']

numerical = ['lotarea', 'masvnrarea', 'bsmtfinsf1', 'bsmtunfsf', 'totalbsmtsf', 
             '1stflrsf', '2ndflrsf', 'grlivarea', 'bsmtfullbath', 'fullbath', 
             'halfbath', 'bedroomabvgr', 'totrmsabvgrd', 'fireplaces', 'garagecars'
             , 'garagearea', 'wooddecksf', 'openporchsf', 'age', 'totalsf']

categorical = ['mszoning', 'lotshape', 'landcontour', 'lotconfig', 'neighborhood', 
               'condition1', 'bldgtype', 'housestyle', 'overallqual', 'overallcond', 
               'yearbuilt', 'yearremodadd', 'roofstyle', 'exterior1st', 'exterior2nd', 
               'exterqual', 'extercond', 'foundation', 'bsmtqual', 'bsmtcond', 'bsmtexposure', 
               'bsmtfintype1', 'bsmtfintype2', 'heatingqc', 'electrical', 'kitchenqual', 
               'functional', 'garagetype', 'garageyrblt', 'garagefinish', 'garagequal', 
               'paveddrive', 'mosold', 'yrsold', 'saletype', 'salecondition']

for col in categorical:
  df[col] = df[col].astype(str)

df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=SEED)
df_train, df_val = train_test_split(df_train_full, test_size=len(df_test), random_state=SEED)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train["saleprice"]
y_val = df_val["saleprice"]
y_test = df_test["saleprice"]

df_train = df_train[numerical + categorical]
df_val = df_val[numerical + categorical]
df_test = df_test[numerical + categorical]

y_train = np.log1p(y_train.values)
y_val = np.log1p(y_val.values)
y_test = np.log1p(y_test.values)

def train(df_train, y_train):
    dicts = df_train[numerical + categorical].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = RandomForestRegressor(n_estimators=60, max_features=28, min_samples_leaf=1, random_state=SEED)
    model.fit(X_train, y_train)

    return dv, model

def predict(df, dv, model):
    dicts = df[numerical + categorical].to_dict(orient='records')
    X = dv.transform(dicts)
    y_pred = model.predict(X)

    return y_pred

dv, model = train(df_train, y_train)

y_pred = predict(df_test, dv, model)

with open(OUTPUT_FILE, "wb") as f_out:
    pickle.dump((dv, model), f_out)
