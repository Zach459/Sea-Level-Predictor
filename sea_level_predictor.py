import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", index_col = 0 )
    

    # Create scatter plot
    
    plt.scatter(df.index, df["CSIRO Adjusted Sea Level"])
    

    # Create first line of best fit
    
    
    res1 = linregress(df.index, df["CSIRO Adjusted Sea Level"])
    year_extended = np.arange(df.index[0], 2051, 1)
    predict1 = year_extended*res1.slope + res1.intercept
    plt.plot(year_extended, predict1)
    # Create second line of best fit
    
    res2 = linregress(df.index[df.index >= 2000], df["CSIRO Adjusted Sea Level"][df.index >= 2000])

    year_extended2 = np.arange(2000, 2051, 1)
    predict2 = year_extended2*res2.slope + res2.intercept
    plt.plot(year_extended2, predict2)
    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()