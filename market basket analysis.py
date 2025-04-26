import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv(r'Sale.csv')

df = df.loc[df['Order ID'].duplicated(keep=False)]
df = df[['Order ID','Product']]

df.to_csv('Duplicated.csv',index=False)