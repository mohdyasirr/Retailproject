import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r'Sale.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['time'] = df['Order Date'].dt.hour

ndf = df['time'].value_counts()
ndf = ndf.reset_index()
ndf = ndf.sort_values(['time'])


# df.to_csv('Sale.csv',index=False)


# sns.relplot(x='time',y='count',data=ndf,kind='line')
# plt.grid()
# plt.xticks(np.arange(0,24))
# plt.show()


