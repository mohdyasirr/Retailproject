import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r'Duplicated.csv')
df['Product'] = df['Product'] +','
ndf = df.groupby('Order ID').agg(
    Product = ('Product','sum')
)
ndf['Product'] = ndf['Product'].str.strip(',')

# ndf.to_csv('ddf.csv',index=False)