import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
# plt.figure(figsize=(8,5))
# clean_df.boxplot(column='tenure')
# plt.title('Box Plot of Tenure')
# plt.ylabel('Tenure (Months)')

# plt.show()



# plt.figure(figsize=(8,5))
# clean_df.boxplot(column='MonthlyCharges')
# plt.title('Box Plot of Monthly charges')
# plt.ylabel('monthly charges')

# plt.show()



# plt.figure(figsize=(8,5))

# clean_df.boxplot(column='TotalCharges')

# plt.title('Box Plot of Total Charges')
# plt.ylabel('Total Charges')

# plt.show()


#task 14 
churn_count=clean_df['Churn'].value_counts()
churn_percentage=clean_df['Churn'].value_counts(normalize=True)*100


print("churn count : ", churn_count)
print("churn percentage :", churn_percentage)


#task 16
internet_churn=pd.crosstab(clean_df['InternetService'],clean_df['Churn'],normalize='index')*100
contract_churn=pd.crosstab(clean_df['Contract'],clean_df['Churn'], normalize='index')*100


print("relation btw internet service and churn:\n",internet_churn)
print("relation btw contact and churn\n",contract_churn)

#task 17
# plt.figure(figsize=(8,5))
# sns.boxplot(x='Churn', y='tenure', data=clean_df)
# plt.title('Tenure vs Churn')
# plt.xlabel('Churn')
# plt.ylabel('Tenure (Months)')

# plt.show()

# plt.figure(figsize=(8,5))

# sns.boxplot(x='Churn', y='MonthlyCharges', data=clean_df)

# plt.title('Monthly Charges vs Churn')
# plt.xlabel('Churn')
# plt.ylabel('Monthly Charges')

# plt.show()



#task 18
corr_matrix=clean_df.corr(numeric_only=True)
print(corr_matrix)
plt.figure(figsize=(8,5))

sns.heatmap(corr_matrix,annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation of numerical features')
plt.show()



#task 23 
# task 23: Build the final clean_df

# Start again from the raw data so this cell is safe to re-run
clean_df = df.copy()

# 1. Fix data type: TotalCharges object -> float (blank strings become NaN)
clean_df['TotalCharges'] = pd.to_numeric(clean_df['TotalCharges'], errors='coerce')

# 2. Confirm the missing TotalCharges rows are exactly the new customers (tenure == 0)
missing_tc = clean_df[clean_df['TotalCharges'].isnull()]
print("Rows with missing TotalCharges:", len(missing_tc))
print("Of these, rows with tenure == 0:", (missing_tc['tenure'] == 0).sum())

# 3. Handle missing values: these customers have not been billed yet, so total = 0
clean_df['TotalCharges'] = clean_df['TotalCharges'].fillna(0)

# 4. Handle duplicates BEFORE dropping the ID column
print("Duplicate rows before:", clean_df.duplicated().sum())
print("Duplicate customerIDs:", clean_df['customerID'].duplicated().sum())
clean_df = clean_df.drop_duplicates()

# 5. Remove the identifier column
clean_df = clean_df.drop(columns=['customerID'])

# 6. Save for Lab 3
clean_df.to_csv('clean_churn.csv', index=False)
print("Saved clean_churn.csv with shape:", clean_df.shape)


#task 24
print(clean_df.info())