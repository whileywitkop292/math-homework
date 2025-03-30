import numpy as np
import pandas as pd

# Example: Create a DataFrame with some data
data = {
    'column1': [1, 2, 3],
    'column2': ['a', 'b', 'c']
}
df = pd.DataFrame(data)

# Calculate the mean of column 'column1'
mean_col_1 = df['column1'].mean()

print(mean_col_1)
