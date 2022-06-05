import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    ax.scatter(x=x, y=y)
    # Create first line of best fit
    m = linregress(x, y)
    year1 = int(df.loc[df['Year'].idxmin()].Year)
    year_extended = [_ for _ in range(year1, 2051, 1)]
    t = [m.slope * i + m.intercept for i in year_extended]
    ax.plot(year_extended, t, 'r')
    # Create second line of best fit
    x = df[df['Year'] >= 2000]['Year']
    y = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    m = linregress(x, y)
    year_extended_2000 = [_ for _ in range(2000, 2051, 1)]
    t_2000 = [m.slope * i + m.intercept for i in year_extended_2000]
    ax.plot(year_extended_2000, t_2000, 'r')
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
