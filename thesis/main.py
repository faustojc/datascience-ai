import re
import pandas as pd

df = pd.read_csv('data/Thesis Data.csv', skiprows=1, encoding='latin-1')

df['STREET NAME/SUBD/CONDO'] = df['STREET NAME/SUBD/CONDO'].ffill()
df['VICINITY'] = df['VICINITY'].ffill()


