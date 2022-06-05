import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
mask = (df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))
df = df[mask]
fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=30)
ax.set_ylabel('Page Views', fontsize=20)
ax.set_xlabel('Date', fontsize=20)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
ax.plot(df, 'r', linewidth=3)
# Save image and return fig (don't change this part)
fig.savefig('line_plot.png')

df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(32, 11), dpi=100)
# left chart
sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
ax1.set_title('Year-wise Box Plot (Trend)', fontsize=24)
ax1.set_xticklabels(ax1.get_xticklabels(), fontsize=16)
ax1.set_xlabel('Years', fontsize=20)
ax1.set_ylabel('Page Views', fontsize=20)
# right chart
order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=order)
ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=24)
ax2.set_xticklabels(ax2.get_xticklabels(), fontsize=16)
ax2.set_xlabel('Months', fontsize=16)
ax2.set_ylabel('Page Views', fontsize=20)

fig.savefig('box_plot.png')

# order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
#          'December']
# label = {'01': 'January',
#          '02': 'February',
#          '03': 'March',
#          '04': 'April',
#          '05': 'May',
#          '06': 'June',
#          '07': 'July',
#          '08': 'August',
#          '09': 'September',
#          '10': 'October',
#          '11': 'November',
#          '12': 'December'
#          }
