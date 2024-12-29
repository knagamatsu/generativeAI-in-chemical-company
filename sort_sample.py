import pandas as pd

df = pd.read_csv('./case..csv')
df_sorted = df.sort_values('date', ascending=False)
df_sorted.to_csv('./case_sorted.csv', index=False)