import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Customer_Churn.csv')
print("shape(rows and columns), (customers,features)=", df.shape)

print("Numerical columns:", df.select_dtypes(include='number').columns.tolist())
print("Categorical columns:", df.select_dtypes(include='object').columns.tolist())


# #(df.info()) shows the datatype of each column  df.dtypes also shows data type of columns 

# #task 6
# print(df['OnlineSecurity'].unique())
# print(df['TechSupport'].unique())
# print(df['PaymentMethod'].unique())


# #task 7
# # 1. Standard NaN values count and  percentage
# null_counts = df.isnull().sum()
# null_percents = (df.isnull().mean()) * 100

# # summary table 

# missing_summary = pd.DataFrame({'Missing Count': null_counts, 'Percentage (%)': null_percents})
# print("=== Standard Missing Values (NaN) ===")
# print(missing_summary)


# total_charges_numeric = pd.to_numeric(df['TotalCharges'], errors='coerce')
# hidden_missing_count = total_charges_numeric.isnull().sum()
# hidden_missing_percent = (hidden_missing_count / len(df)) * 100

# print("\n=== Hidden Missing Values in TotalCharges ===")
# print(f"Count of blank spaces: {hidden_missing_count}")
# print(f"Percentage: {hidden_missing_percent:.3f}%")



# #task 8 
# print ("full row duplicate count :", df.duplicated().sum())
# print("id_duplicates count: ", df['customerID'].duplicated().sum())



#task 11
clean_df=df.copy()
clean_df['TotalCharges'] = pd.to_numeric(
    clean_df['TotalCharges'],
    errors='coerce'
)

print(clean_df['TotalCharges'].dtype)


print(clean_df.isnull().sum())


print(clean_df.duplicated().sum())

print(clean_df['customerID'].duplicated().sum())


#task 12 


# plt.figure(figsize=(8,5))
# plt.hist(df['tenure'], bins=20)
# plt.xlabel('Tenure')
# plt.ylabel('No of customers')
# plt.title('Distribution of customer tenure')
# plt.show()



# plt.figure(figsize=(8,5))

# plt.hist(df['MonthlyCharges'], bins=20)

# plt.xlabel('MonthlyCharges')
# plt.ylabel('Number of Customers')
# plt.title('Distribution of monthly charges ')

# plt.show()




# plt.figure(figsize=(8,5))

# df['Contract'].value_counts().plot(kind='bar')

# plt.xlabel('Contract Type')
# plt.ylabel('Number of Customers')
# plt.title('Distribution of Contract Types')

# plt.xticks(rotation=30, ha='right')

# plt.show()


# plt.figure(figsize=(10,5))

# df['PaymentMethod'].value_counts().plot(kind='bar')

# plt.xlabel('Payment Method')
# plt.ylabel('Number of Customers')
# plt.title('Distribution of Payment Methods')

# plt.xticks(rotation=20, ha='right')

# plt.show()




#task 13 
plt.figure(figsize=(8,5))
clean_df.boxplot(column='tenure')
plt.title('Box Plot of Tenure')
plt.ylabel('Tenure (Months)')

plt.show()



plt.figure(figsize=(8,5))
clean_df.boxplot(column='MonthlyCharges')
plt.title('Box Plot of Monthly charges')
plt.ylabel('monthly charges')

plt.show()



plt.figure(figsize=(8,5))

clean_df.boxplot(column='TotalCharges')

plt.title('Box Plot of Total Charges')
plt.ylabel('Total Charges')

plt.show()