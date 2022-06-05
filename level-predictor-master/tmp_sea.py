import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')
# print(df.columns)
# print(df.head(-5))
fig, ax = plt.subplots()  # Create a figure containing a single axes.
# plt.rcParams["figure.figsize"] = (25, 12)
ax.set_title("Rise in Sea Level")
ax.set_xlabel('Year')
ax.set_ylabel('Sea Level (inches)')

x = df['Year'].values
y = df['CSIRO Adjusted Sea Level'].values
ax.scatter(x=x, y=y)

m = linregress(x, y)
# df.insert(len(df.columns), 'trend', t)
year1 = int(df.loc[df['Year'].idxmin()].Year)

year_extended = [_ for _ in range(year1, 2050, 1)]
t = [m.slope * i + m.intercept for i in year_extended]
ax.plot(year_extended, t, 'r')

x = df[df['Year'] >= 2000]['Year'].values
y = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'].values
m = linregress(x, y)
year_extended_2000 = [_ for _ in range(2000, 2050, 1)]
t_2000 = [m.slope * i + m.intercept for i in year_extended_2000]
ax.plot(year_extended_2000, t_2000, 'r')
plt.savefig('sea_level_plot.png')
