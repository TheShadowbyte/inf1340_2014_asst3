__author__ = 'Curtis and Dimitar and Shawn'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

#!/usr/bin/env python

"""
Creates a line graph out of .json stock histories and marks the six best and six worst months
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import mining
import datetime

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

# gets the lists from mining's StockMiner class and makes them into lists
best_months = mining.StockMiner('GOOG', 'data/GOOG.json').six_best_months()
worst_months = mining.StockMiner('GOOG', 'data/GOOG.json').six_worst_months()
monthly_averages_list = mining .StockMiner('GOOG', 'data/GOOG.json').get_monthly_averages_list()

# Some empty lists for storage
best_stock_prices = []
best_stock_dates = []
worst_stock_prices = []
worst_stock_dates = []
monthly_prices = []
monthly_dates = []
datetime_list = []


def sort_stock_results(best_months_list, worst_months_list, monthly_list):
    """
    Takes the results of StockMiner's lists and organizes the contents into variables for graphing
    :param best_months_list: the return of mining.best_six_months, tuples of the best performing stock dates/prices
    :param worst_months_list: the return of mining.worst_six_months, tuples of the worst performing stock dates/prices
    :param monthly_list: the return of mining.monthly_averages, tuples of the entire historical data set
    :return: returns a whole bunch of lists of semi-organized data
    """
    for datum in best_months:
        best_stock_dates.append(datum[0])
        best_stock_prices.append(datum[1])

    for datum in worst_months:
        worst_stock_dates.append(datum[0])
        worst_stock_prices.append(datum[1])

    for datum in monthly_averages_list:
        monthly_dates.append(datum[0])
        monthly_prices.append(datum[1])

#runs the functions to get the proper lists
sort_stock_results(best_months, worst_months, monthly_averages_list)


def format_dates(dates_str_list):
    """
    Takes the date strs and creates them as datetime objects
    :param dates_str_list: a list of strs representing
    :return:  datetime_list: a list of datetime objects
    """
    for date in dates_str_list:
        datetime_list.append(datetime.datetime.strptime(date, "%Y/%m").date())

format_dates(monthly_dates)

# sets the parametres of the graph to be plotted
fig, ax = plt.subplots()
x_len = len(monthly_prices)
index = np.arange(x_len)

# Plots the actual graph out of the above lists
stock_line = plt.plot(datetime_list, monthly_prices, color='#33CCFF', linewidth=3.0, linestyle='-')
# Demarcates the fields of best and worst performing months
plt.axhspan(ymin=min(best_stock_prices), ymax=max(best_stock_prices), xmin=0, xmax=1, color='#99CC00')
green_best = mpatches.Patch(color='#99CC00')
plt.axhspan(ymin=min(worst_stock_prices), ymax=max(worst_stock_prices), xmin=0, xmax=1, color='#FF0066')
red_worst = mpatches.Patch(color='#FF0066')


# all the labelling, ticks based on dates, and some style stuff
ax.set_title("stock_name" + '\nHistorical Monthly Prices')
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_ylabel("$\$$ USD")
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)
# makes sure the x axis is is as long as the data
datemin = min(datetime_list)
datemax = max(datetime_list)
ax.set_xlim(datemin, datemax)


box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

# Put a legend below current axis
# ax.legend([stock_line, green_best, red_worst], ['Stock Price', 'Best Months', 'Worst Months'],
#           bbox_to_anchor=(0., 1.02, 1., .102), loc=8,
#            ncol=3, mode="expand", borderaxespad=0.)
#           #   loc='upper center', bbox_to_anchor=(0.5, -0.05),
#           # fancybox=True, shadow=False, ncol=3)


# sets the display parametres for mouseover (x = time, y = price)
def price(x): return '$%1.2f'%x
ax.format_xdata = mdates.DateFormatter('%Y/%m')
ax.format_ydata = price

ax.grid(True)

fig.autofmt_xdate()
fig.savefig('stock_line.png', transparent=True)
plt.show()
