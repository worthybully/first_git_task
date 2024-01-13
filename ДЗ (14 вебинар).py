import pandas as pd
df = pd.read_csv("C:\Users\User\Downloads\Customers.csv")
df[['CustomerID', 'Gender', 'Age', 'Income', 'Spending Score (1-100)', 'Profession', 'Work Experience', 'Family Size']] = df['CustomerID;Gender;Age;Income;Spending Score (1-100);Profession;Work Experience;Family Size'].str.split(';', expand=True)
new_df = df.drop('CustomerID;Gender;Age;Income;Spending Score (1-100);Profession;Work Experience;Family Size', axis=1, inplace=False)
new_df[['Age', 'Income', 'Work Experience']] = df[['Age', 'Income', 'Work Experience']].astype(int)
new_df['Profession'].unique()
new_df[(new_df['Age'] > 30) & (new_df['Income'] < 30000)]
new_df[(new_df['Profession'] == 'Lawyer') & (new_df['Work Experience'] > 5)]