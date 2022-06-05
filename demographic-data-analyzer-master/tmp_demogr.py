import pandas as pd

# Read data from file
df = pd.read_csv("adult.data.csv")
print(df.columns)

# Identify the most popular occupation for those who earn >50K in India.

mask = (df.salary == '>50K') & (df['native-country'] == 'India')
top_IN_occupation = df[mask].occupation.value_counts().idxmax()
print(top_IN_occupation)



