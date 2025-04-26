import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r'Sale.csv')

df['Purchase'] = df['Quantity Ordered'] * df['Price Each']

df['Order Date'] = pd.to_datetime(df['Order Date'])

df['month'] = df['Order Date'].dt.month
df['month name'] = df['Order Date'].dt.month_name()

# df.to_csv('Sale.csv',index=False)