# Import libraries.
import pandas as pd
import numpy as np

# Step 1: Create a sample dataset with a Python dictionary (Datasets are available for free through some websites).
data = {
    'Hours_Studied': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
    'Test_Score': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25]
}

# Step 2: Convert the dictionary to a DataFrame.
df = pd.DataFrame(data)
print("Initial DataFrame: ")
print(df)
print("\nFirst few rows of the DataFrame: ")
print(df.head())

# Step 3: Get basic statistics of the DataFrame.
print("\nBasic statistics of the DataFrame (using Pandas): ")
print(df.describe())

hours_array = np.array(df['Hours_Studied'])
mean_hours = np.mean(hours_array)
std_hours = np.std(hours_array)

print("\nNumPy Calculations:")
print(f"Mean of Hours Studied: {mean_hours:.2f}") #.2f is string formatting to control the number of decimal places displayed.
print(f"Standard Deviation of Hours Studied: {std_hours:.2f}")

# Step 4: Get the shape of the DataFrame.
print("\nShape of the DataFrame: ")
print(df.shape)

# Step 5: Get the column names of the DataFrame.
print("\nColumn names of the DataFrame: ")
print(df.columns)

# Step 6: Get the data types of the columns in the DataFrame.
print("\nData types of the columns in the DataFrame: ")
print(df.dtypes)

# Step 7: Add a new column to the DataFrame.
df['Grade'] = ['F', 'F', 'F', 'C', 'F', 'F', 'B+', 'B', 'A', 'F']
print("\nDataFrame after adding a new column 'Grades': ")

# Step 8: Handle missing values (if applicable).
df.loc[5, 'Test_Score'] = np.nan # Introducing a missing value.
print("\N DataFrame with a missing value:")
print(df)

# Step 9: Fill missing values with the median using NumPy.
median_score = np.nanmedian(df['Test_Score'])
df['Test_Score'].fillna(median_score, inplace=True)
print("\nDataFrame after filling missing values with the median:")
print(df)

# Step 10: Filter & sort data.
print("\nStudents who scored above 50:")
high_scorers = df[np.array(df['Test_Score'] > 50)]
print(high_scorers)

print("\nStudents who studied more than 5 hours:")
filtered_df = df[df['Hours_Studied'] > 5]
print(filtered_df)

# Step 11: Save the DataFrame to a CSV file.
df.to_csv('student_data.csv', index=False)
print("\nDataFrame saved to 'student_data.csv' file.")