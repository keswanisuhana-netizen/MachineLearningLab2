import pandas as pd
import numpy as np
df=pd.read_csv('Customer_Churn.csv')
print("shape(rows and columns), (customers,features)=", df.shape)

print("Numerical columns:", df.select_dtypes(include='number').columns.tolist())
print("Categorical columns:", df.select_dtypes(include='str').columns.tolist())


print(df['OnlineSecurity'].unique())
print(df['TechSupport'].unique())
print(df['PaymentMethod'].unique())