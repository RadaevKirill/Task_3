import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_csv('./data/train/train.csv')

X_train = df.drop('Temperature', axis=1)
y_train = df['Temperature']

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, './data/trained_model.sav')
