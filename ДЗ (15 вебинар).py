import pandas as pd
df = pd.read_csv('/content/Customers.csv')
df[['CustomerID', 'Gender', 'Age', 'Income', 'Spending Score (1-100)', 'Profession', 'Work Experience', 'Family Size']] = df['CustomerID;Gender;Age;Income;Spending Score (1-100);Profession;Work Experience;Family Size'].str.split(';', expand=True)
new_df = df.drop('CustomerID;Gender;Age;Income;Spending Score (1-100);Profession;Work Experience;Family Size', axis=1, inplace=False)
new_df[['Age', 'Income', 'Work Experience']] = df[['Age', 'Income', 'Work Experience']].astype(int)
new_df.isnull().sum()
grouped_df = new_df.groupby('Profession')['Income'].agg('mean')
print(grouped_df)