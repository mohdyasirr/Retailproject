import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# What City sold the most product --->

df = pd.read_csv(r'Sale.csv')

df['City'] = df['Purchase Address'].str.split(',',expand=True)[1]

ndf = df.groupby('City').agg(
    orders = ('Quantity Ordered','sum')
)
ndf = ndf.sort_values('orders',ascending=False)
ndf = ndf.reset_index()
print(ndf)
# ndf.to_csv('Number of orders City Wise.csv')