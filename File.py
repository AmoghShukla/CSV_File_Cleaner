import pandas as pd

# This function reads a CSV file, removes duplicates and NaN values, and saves the cleaned data to a new CSV file.
def CSVfine(input_file, Output_file):

    # We read the CSV file and store it in a DataFrame
    df = pd.read_csv(input_file)

    # We remove duplicates and NaN values
    df = df.drop_duplicates()

    # After removing duplicates, we also remove any rows with NaN values
    df = df.dropna()

    # Here we save the cleaned DataFrame to a new CSV file
    df.to_csv(Output_file, index=False)

# Example usage of the CSVfine function
input_file = 'input.csv'
Output_file = 'output.csv'
CSVfine(input_file, Output_file)