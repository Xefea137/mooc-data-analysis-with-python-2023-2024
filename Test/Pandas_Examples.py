import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
print(df)
#       Name  Age         City
# 0    Alice   25     New York
# 1      Bob   30  Los Angeles
# 2  Charlie   35      Chicago
# 3    David   40      Houston
print()


# Accessing columns
# To access a single column, you can use square brackets and the column name
# Alternatively, you can also use dot notation if the column name is a valid Python variable name
name_column = df['Name']    # name_column = df.Name
print("Name column:")
print(name_column)
# 0      Alice
# 1        Bob
# 2    Charlie
# 3      David
# Name: Name, dtype: object
print()

age_column = df['Age']      # age_column = df.Age
print("Age column:")
print(age_column)
# 0    25
# 1    30
# 2    35
# 3    40
# Name: Age, dtype: int64
print()

city_column = df['City']    # city_column = df.City
print("City column:")
print(city_column)
# 0       New York
# 1    Los Angeles
# 2        Chicago
# 3        Houston
# Name: City, dtype: object
print()


# Accessing rows
# You can access rows using the .loc or .iloc accessor
# .loc is label-based, which means you provide the index label or the row label
# .iloc is integer-based, which means you provide the integer position of the row

# Accessing a single row by label
row_alice = df.loc[0]
print("Row for Alice:")
print(row_alice)
# Name       Alice
# Age           25
# City    New York
# Name: 0, dtype: object
print()

# Accessing a single row by integer position
row_bob = df.iloc[1]
print("Row for Bob:")
print(row_bob)
# Name            Bob
# Age              30
# City    Los Angeles
# Name: 1, dtype: object
print()

# Accessing multiple rows by label
multiple_rows = df.loc[[0, 2]]
print("Multiple rows:")
print(multiple_rows)
#       Name  Age      City
# 0    Alice   25  New York
# 2  Charlie   35   Chicago
print()

# Accessing multiple rows by integer position
multiple_rows_iloc = df.iloc[[0, 2]]
print("Multiple rows using iloc:")
print(multiple_rows_iloc)
#       Name  Age      City
# 0    Alice   25  New York
# 2  Charlie   35   Chicago
print()


# Accessing a single cell value
cell_value = df.at[0, 'Name']  # This will give you the value at row 0, column 'Name'
print("Cell value:", cell_value)
# Cell value: Alice
print()

# Accessing a single cell value by integer position
cell_value_iloc = df.iat[0, 0]  # This will give you the value at row 0, column 0
print("Cell value using iloc:", cell_value_iloc)
# Cell value using iloc: Alice