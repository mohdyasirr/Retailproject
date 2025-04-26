import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r'Sale.csv')

ndf = df.groupby(['month','month name']).agg(
    total_sale = ('Purchase','sum')
)
ndf = ndf.reset_index()
# ndf.to_csv('Monthly Sales.csv',index=False)

plt.plot(ndf['month name'],ndf['total_sale'],marker='o')
plt.xlabel('month')
plt.ylabel('Sale in ten laks')
plt.xticks(rotation=45)
plt.grid()
for x,y in zip(ndf['month name'],ndf['total_sale']):
    plt.text(x,y,y,va='bottom',ha='right',color='red',fontsize=5)
plt.show()

