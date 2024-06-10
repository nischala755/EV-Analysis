import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data/Electric_Vehicle_Population_Data.csv')

# Display the first 5 rows of the dataframe
print(df.head(5))

# Display the column names
print(df.columns)

# Display the last 5 rows of the dataframe
print(df.tail())

# Display information about the dataframe
print(df.info())

# Display the count of missing values in each column
print(df.isnull().sum())

# Fill missing values
median_year = df['Model Year'].median()
df['Model Year'].fillna(median_year, inplace=True)
df['Make'].fillna('Unknown', inplace=True)
df['Model'].fillna('Unknown', inplace=True)
median_range = df['Electric Range'].median()
df['Electric Range'].fillna(median_range, inplace=True)
median_msrp = df['Base MSRP'].median()
df['Base MSRP'].fillna(median_msrp, inplace=True)
df.dropna(subset=['State'], inplace=True)

# Scatter plot of Electric Vehicle Population by Model Year
plt.figure(figsize=(12, 8))
plt.scatter(df['Model Year'], df['Electric Vehicle Type'], color='blue', alpha=0.5)
plt.title('Electric Vehicle Population by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Vehicle Type')
plt.grid(True)
plt.show()

# Scatter plot using Seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Model Year', y='Electric Vehicle Type', alpha=0.5)
plt.title('Electric Vehicle Population by Model Year')
plt.xlabel('Model Year')
plt.ylabel('Electric Vehicle Type')
plt.grid(True)
plt.show()

# Bar plot of Electric Vehicle Population by Manufacturer
make_counts = df['Make'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(make_counts.index, make_counts.values, color='skyblue')
plt.xlabel('Electric Vehicle Manufacturer')
plt.ylabel('Number of Electric Vehicles')
plt.title('Electric Vehicle Population by Manufacturer')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Histogram of Electric Vehicle Range
data = df['Electric Range']
plt.hist(data, bins=20, color='green', edgecolor='black')
plt.xlabel('Electric Range')
plt.ylabel('Frequency')
plt.title('Electric Vehicle Range Histogram')
plt.show()
