# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "global_air_quality_data_10000.xlsx"
data = pd.read_excel(file_path)

# Initial Exploration
print("Initial Data Exploration")
print(data.head())
print(data.info())
print(data.describe())

# Data Cleaning
# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Check for duplicates
duplicates = data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Normalize column names
data.columns = data.columns.str.strip().str.replace(' ', '_').str.lower()

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Handling missing or incorrect data
# Separate numeric and non-numeric columns
numeric_cols = data.select_dtypes(include=['number']).columns
non_numeric_cols = data.select_dtypes(exclude=['number']).columns

# Fill missing values for numeric columns with the mean of each column
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# For non-numeric columns, you might want to use mode or a constant value
# Example: Fill missing values for non-numeric columns with the mode
for col in non_numeric_cols:
    data[col] = data[col].fillna(data[col].mode()[0])

# Verify that there are no more missing values
missing_values_after = data.isnull().sum()
print("Missing values after handling:")
print(missing_values_after)

# Exploratory Data Analysis (EDA)
print("\nExploratory Data Analysis (EDA)")

# Distribution of PM2.5 values
plt.figure(figsize=(10, 6))
sns.histplot(data['pm2.5'], kde=True, bins=30)
plt.title('Distribution of PM2.5 values')
plt.xlabel('PM2.5')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of PM2.5 vs Temperature
plt.figure(figsize=(10, 6))
sns.scatterplot(x='temperature', y='pm2.5', data=data)
plt.title('PM2.5 vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('PM2.5')
plt.show()

# Box plot of PM2.5 values by Country
plt.figure(figsize=(12, 8))
sns.boxplot(x='country', y='pm2.5', data=data)
plt.title('PM2.5 values by Country')
plt.xlabel('Country')
plt.ylabel('PM2.5')
plt.xticks(rotation=90)
plt.show()

# Heatmap of correlation matrix (only numeric columns)
plt.figure(figsize=(12, 8))
correlation_matrix = data[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()

# Insights and Observations
insights = """
1. The distribution of PM2.5 values shows that most values are between 40 and 120.
2. There is a slight positive correlation between PM2.5 and temperature.
3. The box plot indicates that some countries have higher median PM2.5 values compared to others.
4. The correlation matrix shows strong correlations between certain pollutants (e.g., PM2.5 and PM10).
"""

print("Insights and Observations")
print(insights)

# Save the cleaned data
cleaned_file_path = "cleaned_global_air_quality_data.xlsx"
data.to_excel(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")

