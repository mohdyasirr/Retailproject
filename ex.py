from itertools import combinations    # Find the combinations
from collections import Counter
import pandas as pd


df = pd.read_csv(r'ddf.csv')
df['Product'] = df['Product'].str.split(',')

total_purchases = list(df['Product'])


count = Counter()  # Counter is class, iske ander count krne ke functions hote h

for single_purchase in total_purchases:
    count.update(Counter(combinations(single_purchase,2)))

#task --> Convert into excel

print('Excel file created successfully')

comb_df = pd.DataFrame(count.items(), columns=['Product_Pair', 'Count'])

comb_df.to_excel('product_combinations.xlsx', index=False)