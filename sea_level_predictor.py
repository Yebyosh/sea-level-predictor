import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot - Use matplotlib to create scatter plot using Year column as x-axis and CSIRO Adjusted Sea Level column as y-axis.
    # plt.scatter(x,y,s=area,c=colors, alpha=0.5)
    plt_x = df['Year']
    plt_y = df['CSIRO Adjusted Sea Level']
    plt.scatter(plt_x, plt_y)

    # Create first line of best fit - Use linregress function from scipy.stats to get slope and y-intercept of line of best fit. Plot line over top of scatter plot. Make line go through year 2050 to predict sea level rise in 2050.
    # slope, intercept, r, p, se = linregress(x, y)
    # result = linregress(x, y) <- result is an obj with slope, intercept, rvalue, pvalue and stderr as attributes
    res1 = linregress(plt_x, plt_y)
    #print(f'{res1.slope}, {res1.intercept}, {res1.rvalue}, {res1.pvalue}, {res1.stderr}')
    x_res1 = np.arange(1880, 2051)
    y_res1 = x_res1 * res1.slope + res1.intercept
    plt.plot(x_res1, y_res1, color='r', label='Best Fit 1')

    # Create second line of best fit - Plot new line of best fit just using data from year 2000 through most recent year in dataset. Make line also go through year 2050 to predict sea level rise in 2050 if the rate of rise continues as it has since year 2000.
    src_new_x = df.loc[df['Year'] >= 2000, 'Year']
    src_new_y = df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level']
    res2 = linregress(src_new_x, src_new_y)
    x_res2 = np.arange(2000, 2051)
    y_res2 = x_res2 * res2.slope + res2.intercept
    plt.plot(x_res2, y_res2, color='g', label='Best Fit 2')

    # Add labels and title - x label should be Year, y label should be Sea Level (inches), and title should be Rise in Sea Level
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    #plt.legend() - somehow legend is spammed 5 times

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
