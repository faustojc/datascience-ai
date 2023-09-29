import pandas as pd

print('pandas version: ', pd.__version__)

df = pd.read_csv('data/Cost of living index by country 2020.csv')

df.head()
df.tail()
df.sample(10)
df.columns
df.info()
df.describe()
df[['Cost of Living Index']].describe()
df.shape
df[['Cost of Living Index', 'Rent Index', 'Cost of Living Plus Rent Index']]
df[df.columns[-5:]]
df.select_dtypes('float64')
df['Local Purchasing Power Index'].value_counts()
df['Local Purchasing Power Index'].unique()
df['Local Purchasing Power Index'].min()
df['Local Purchasing Power Index'].max()
df['Local Purchasing Power Index'].sum()
df['Local Purchasing Power Index'].mean()
df['Local Purchasing Power Index'].std()
df['Local Purchasing Power Index'].quantile([0.25, 0.5, 0.75])
df[['Cost of Living Index', 'Rent Index', 'Cost of Living Plus Rent Index']].agg(['mean', 'std', 'min', 'max'])