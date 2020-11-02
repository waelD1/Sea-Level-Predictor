import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err= linregress(x, y)

    plt.scatter(x,intercept + slope*x)

    x1 = pd.Series(range(1880,2050))
    y1 = pd.Series(intercept + slope*x1)
    plt.plot(x1, y1)
    

    # Create second line of best fit
    x2 = df[df['Year']>=2000]['Year']
    y2 = df[df['Year']>=2000]['CSIRO Adjusted Sea Level']

    slope_new, intercept_new, r_value_new, p_value_new, std_err_new= linregress(x2, y2)

    x3 = pd.Series(range(2000,2050))
    y3 = pd.Series(intercept_new + slope_new*x3)
    plt.plot(x3,y3)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level') 
    
    # Save plot and return data for testing 
    plt.savefig('sea_level_plot.png')
