import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi_mask = (df['weight'] / ((df['height'] / 100) ** 2)) > 25
df['overweight'] = 0
df.loc[bmi_mask, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad.
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.gluc = np.where(df.gluc == 1, 0, 1)
df.cholesterol = np.where(df.cholesterol == 1, 0, 1)


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    # using just the values from 'cholesterol', 'gluc', 'gluc', 'alco', 'active', and 'overweight'.

    df_cat = pd.melt(df, id_vars='cardio',
                     value_vars=['cholesterol', 'gluc', 'gluc', 'alco', 'active', 'overweight', 'smoke'])

    # Group and reformat the data to split it by 'cardio'.
    # Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).value_counts()
    df_cat.rename(columns={'count': 'total'}, inplace=True)
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x="variable", y="total", hue="value", kind="bar", data=df_cat, col='cardio').fig
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    mask = (df['ap_lo'] <= df['ap_hi'])
    mask2 = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    mask3 = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[mask & mask2 & mask3]
    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson')
    # print(corr)
    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9), dpi=100)

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, square=True, fmt='.1f', mask=mask, annot=True, linewidths=.5, ax=ax)
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
