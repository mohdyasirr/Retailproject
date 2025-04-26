import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv(r'Sale.csv')
df = df.loc[df['Order ID'] != 'Order ID']  # Filter out irregular value
# print(df.isnull().sum())  # Check how many values are missing in dataset
df = df.dropna(how='all')  # Delete missing value where all values missing

# df.to_csv('Sale.csv',index=False)

print(df.info())