import pandas as pd

# Load the dataset (change the path to the location of your dataset)
try:
    df = pd.read_csv('your_dataset.csv')  # Replace with your dataset file path
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: The file was not found. Please check the file path.")
    exit()

# Display first few rows to inspect data
print("First few rows of the dataset:")
print(df.head())

# Check data types and missing values
print("\nData Types and Missing Values:")
print(df.info())

# Clean the dataset by filling or dropping missing values
# Here, we are filling missing values with the mean (you can customize this based on the dataset)
df.fillna(df.mean(), inplace=True)

# Verify if missing values are handled
print("\nAfter cleaning missing values:")
print(df.isnull().sum())
