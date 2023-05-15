import pandas as pd

df = pd.read_excel('./email.xlsx')

# Convert each row to a string
row_strings = df.apply(lambda row: row.astype(str).str.cat(sep=', '), axis=1)

# Print the row strings that end with '@bauer.uh.edu'
for row_string in row_strings:
    if not row_string.endswith('@bauer.uh.edu'):
        print(row_string)