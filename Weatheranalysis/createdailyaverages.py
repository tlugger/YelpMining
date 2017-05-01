import csv
import pandas as pd

df = pd.read_csv("avgthis.csv")
dailyavgweather=df.groupby(pd.DatetimeIndex(df['DATE']).normalize())['DAILYSunset'].mean()
dailyavgweather.to_csv('avgdailyweather.csv', sep=',')
