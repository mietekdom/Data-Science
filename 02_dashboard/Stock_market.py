import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% importing data
df = pd.read_csv('./data/ten.csv', index_col=0)

df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']


# %% dzienna procentowa zmiana procentowa w porównaniu z dniem poprzednim

df['Daily_Change'] = df['Close'].pct_change()

# %% zmiana procntowa z okresu 5 dni

df['5_Daily_Change'] = df['Close'].pct_change(periods=5)

# %% zmiana procentowa otwarcia i zmakiecia (sesja giełdowa z dnia)

df['Close_to_Open'] = df[['Open', 'Close']].pct_change(axis=1).drop('Open', axis=1)

# %%

clean_price = df[['Open', 'High', 'Low', 'Close']]

daily_change = clean_price.pct_change()