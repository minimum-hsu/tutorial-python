#!/usr/bin/env python3

# Functional Programming Example with Pandas.

# Functional Programming (FP) is a programming paradigm where functions are treated as first-class citizens. This means that functions can be passed as arguments, returned from other functions, and assigned to variables. The main characteristics of FP are:
# Immutability: Data is not modified directly. Instead of changing existing data, new data is created from the original.
# Pure Functions: Functions always produce the same output for the same input and have no side effects (like modifying global variables or printing to the screen).
# Higher-Order Functions: Functions can accept other functions as arguments or return them as results, making the code more flexible and reusable.
# Function Composition: Small functions are combined to build more complex functions, making the code modular and easier to understand.
# Overall, FP focuses on using functions to transform data and avoid mutable state, leading to cleaner, more predictable code.

from pandas import DataFrame

def create_example() -> DataFrame:
    """
    Create a simple pandas DataFrame as an example.

    Returns:
        DataFrame: A pandas DataFrame with sample data.
    """

    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    return DataFrame(data)

def filter_age(df, min_age) -> DataFrame:
    '''
    Filter rows where Age is greater than min_age.

    Args:
        df (DataFrame): The input DataFrame.
        min_age (int): The minimum age to filter by.

    Returns:
        DataFrame: Filtered DataFrame.
    '''

    return df[df['Age'] > min_age]

def uppercase_city(df) -> DataFrame:
    '''
    Convert the 'City' column to uppercase.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: DataFrame with 'City' column in uppercase.
    '''

    _df = df.copy()
    _df['City'] = _df['City'].apply(lambda city: city.upper())
    return _df

def add_age_flag(df) -> DataFrame:
    '''
    Add a new column 'Age > 30' indicating if Age is greater than 30.

    Args:
        df (DataFrame): The input DataFrame.

    Returns:
        DataFrame: DataFrame with new 'Age > 30' column.
    '''

    _df = df.copy()
    _df['Age > 30'] = _df['Age'].apply(lambda age: age > 30)
    return _df

if __name__ == '__main__':
    df = create_example()

    # Using pipe to chain functions
    result = df.pipe(filter_age, min_age=30) \
               .pipe(uppercase_city) \
               .pipe(add_age_flag)
    print(result)
