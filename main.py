import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = 'Online Retail.xlsx'  # Replace with your file path
data = pd.read_excel(file_path)

# Display the first few rows of the data
print(data.head())

# Basic information about the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Summary statistics
print(data.describe())

# Data Visualization
# Histograms for numerical features
num_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[num_columns].hist(bins=15, figsize=(15, 6), layout=(2, 4))

# Box plots for numerical features
plt.figure(figsize=(15, 10))
for i, col in enumerate(num_columns):
    plt.subplot(2, 4, i + 1)
    sns.boxplot(y = data[col])
    plt.title(f'Box plot of {col}')
plt.tight_layout()

# Correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')

plt.show()
