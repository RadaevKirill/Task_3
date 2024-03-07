﻿from sklearn.preprocessing import StandardScaler, OneHotEncoder
import os
import pandas as pd


class PrcoessModel:
  def __init__(self):
    self.scaler = StandardScaler()
    self.encoder = OneHotEncoder()

  def load_data(self, path):
    data = pd.concat([pd.read_csv(os.path.join(path, file)) for file in os.listdir(path) if file.endswith(".csv")], ignore_index=True)
    return data
  
  def process_data(self,folder_path):
        raw_data = self.load_data(folder_path)

        numerical_data = raw_data.select_dtypes(include=['number'])
        categorical_data = raw_data.select_dtypes(exclude=['number'])

        scaled_numerical_data = self.scaler.fit_transform(numerical_data)
        encoded_categorical_data = self.encoder.fit_transform(categorical_data)

        processed_numerical = pd.DataFrame(scaled_numerical_data, columns=numerical_data.columns)
        processed_categorical = pd.DataFrame(encoded_categorical_data.toarray(), columns=self.encoder.get_feature_names_out(categorical_data.columns))

        return pd.concat([processed_numerical, processed_categorical], axis=1)
  