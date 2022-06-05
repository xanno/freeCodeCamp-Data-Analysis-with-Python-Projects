import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)
# Clean data
mask = (df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))
df = df[mask]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10), dpi=100)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=30)
    ax.set_ylabel('Page Views', fontsize=20)
    ax.set_xlabel('Date', fontsize=20)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    ax.plot(df, 'r', linewidth=3)
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df_bar.groupby(pd.Grouper(freq="M")).mean().round().astype(int)
    df_bar['Years'] = df_bar.index.year
    df_bar['Months'] = df_bar.index.month_name()

    df_bar.reset_index(inplace=True)
    df_bar = df_bar.drop('date', axis=1)

    missing_data = {
        'value': [0, 0, 0, 0],
        'Years': [2016, 2016, 2016, 2016],
        'Months': ['January', 'February', 'March', 'April'],
    }
    df_missing = pd.DataFrame(missing_data)
    df_bar = pd.concat([df_missing, df_bar])
    print(df_bar)

    fig, ax = plt.subplots(figsize=(15, 13), dpi=150)
    sns.barplot(x="Years", y="value", hue="Months", data=df_bar, palette="tab10")
    plt.xticks(rotation=90, fontsize=16)
    plt.xticks(fontsize=16)
    plt.xlabel('Years', fontsize=20)
    plt.ylabel('Average Page Views', fontsize=20)
    # plt.setp(ax.get_legend().get_texts(), fontsize=20)  # for legend text
    # plt.setp(ax.get_legend().get_title(), fontsize='20') # for legend title
    plt.legend(title='Months', fontsize=20, title_fontsize=20)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    # Draw box plots (using Seaborn)
    # left chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(32, 11), dpi=100)
    sns.boxplot(x="year", y="value", data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=24)
    ax1.set_xticklabels(ax1.get_xticklabels(), fontsize=16)
    ax1.set_xlabel('Year', fontsize=20)
    ax1.set_ylabel('Page Views', fontsize=20)
    # right chart
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x="month", y="value", data=df_box, ax=ax2, order=order)
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=24)
    ax2.set_xticklabels(ax2.get_xticklabels(), fontsize=16)
    ax2.set_xlabel('Month', fontsize=16)
    ax2.set_ylabel('Page Views', fontsize=20)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
