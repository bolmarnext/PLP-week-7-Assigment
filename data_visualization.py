import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming df is already loaded from load_and_explore.py or another script

# Line Chart (e.g., sales trend over time)
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='date_column', y='sales_column')
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()

# Bar Chart (e.g., comparison of numerical value across categories)
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='category_column', y='numerical_column')
plt.title('Comparison of Numerical Value Across Categories')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# Histogram (e.g., distribution of a numerical column)
plt.figure(figsize=(10, 6))
sns.histplot(df['numerical_column'], kde=True, bins=30)
plt.title('Distribution of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot (e.g., relationship between two numerical columns)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='numerical_column_1', y='numerical_column_2')
plt.title('Relationship Between Two Numerical Columns')
plt.xlabel('Numerical Column 1')
plt.ylabel('Numerical Column 2')
plt.show()
