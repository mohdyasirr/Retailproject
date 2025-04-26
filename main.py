import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

## Merging files in one file ----->

# Method 1:
filenames = os.listdir('SalesData')
edf = pd.DataFrame()

for filename in filenames:
    df = pd.read_csv(f'SalesData/{filename}')
    edf = pd.concat([edf,df])

edf.to_csv('Sale.csv',index=False)

# Method 2:
# filenames = os.listdir('SalesData')
# edf = pd.DataFrame()
# for filename in filenames:
#     file_path = os.path.join('SalesData', filename)
#     df = pd.read_csv(file_path)  # Read each CSV file into a DataFrame
#     print(df)

