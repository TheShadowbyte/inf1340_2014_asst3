"""
                                bonus_02_visual.py

Creates a line graph out of .json stock histories and marks the six best and six worst months

Uses the following external libraries (all installable with pip)

matplotlib 1.4.2 : a plotting library with many contents, available under BSD freeware license from matplotlib.org

Make sure you comment out the graph you don't want to see! Find the call for that at the bottom of this file!
"""

__author__ = 'Curtis and Dimitar and Shawn'
__email__ = "curtis.mccord@mail.utoronto.ca"

__copyright__ = "No rights reserved"
__license__ = "Free"

__status__ = "Functional"


# !/usr/bin/env python

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import mining
import datetime

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')

# Some empty lists for storage
best_stock_prices = []
best_stock_dates = []
worst_stock_prices = []
worst_stock_dates = []
monthly_prices = []
monthly_dates = []
datetime_list = []
best_months = []
worst_months = []
monthly_averages_list = []
stock_title = ""


def visualize_stock(stock_file_path):
    """
    Uses a .json to generate a graph properly indexed and titled
    :param stock_file_path: the .json you want to import
    :return: a matplotlib graph
    """
    global stock_title
    stock_title = set_stock_title(stock_file_path)
    set_stock_data(stock_file_path)
    sort_stock_results(best_months, worst_months, monthly_averages_list)
    format_dates(monthly_dates)
    plot_graph()


def set_stock_title(stock_name):
    """
    Sets stock_title variable so we get a nice title for our graph out of the file name
    :param stock_name: the .json filename
    :return: a str which has cut out all of the formatting matter and leaves only the ostensible name of the stock
    """
    stock_title = stock_name.split('.')[0]
    if stock_title.__contains__("/"):
        stock_title=stock_title.split("/")[-1]
    return stock_title


def set_stock_data(stock_file):
    """
    Makes lists of data to plot based on entered .json file.
    :param stock_file: a .json containing the correct information
    :return: best_months, worst_months, and monthly_averages
    """
    global best_months
    global worst_months
    global monthly_averages_list
    mining_var = mining.StockMiner(stock_title, stock_file)
    best_months = mining_var.six_best_months()
    worst_months = mining_var.six_worst_months()
    monthly_averages_list = mining_var.get_monthly_averages_list()


def sort_stock_results(best_months_list, worst_months_list, monthly_list):
    """
    Takes the results of StockMiner's lists and organizes the contents into variables for graphing
    :param best_months_list: the return of mining.best_six_months, tuples of the best performing stock dates/prices
    :param worst_months_list: the return of mining.worst_six_months, tuples of the worst performing stock dates/prices
    :param monthly_list: the return of mining.monthly_averages, tuples of the entire historical data set
    :return: returns a whole bunch of lists of semi-organized data
    """
    global best_months
    global worst_months
    global monthly_averages_list

    for datum in best_months:
        best_stock_prices.append(datum[1])

    for datum in worst_months:
        worst_stock_prices.append(datum[1])

    for datum in monthly_averages_list:
        monthly_dates.append(datum[0])
        monthly_prices.append(datum[1])


def format_dates(dates_str_list):
    """
    Takes the date strs and creates them as datetime objects
    :param dates_str_list: a list of strs representing
    :return:  datetime_list: a list of datetime objects
    """
    for date in dates_str_list:
        datetime_list.append(datetime.datetime.strptime(date, "%Y/%m").date())


def plot_graph():
    """
    Plots a graph with specs listed below
    :return: a nice matplotlib graph
    """
    # sets the parametres of the graph to be plotted
    fig, ax = plt.subplots()

    # Plots the actual graph out of the above lists
    stock_line = plt.plot(datetime_list,
                          monthly_prices,
                          color='#33CCFF',
                          linewidth=3.0,
                          linestyle='-')
    # Demarcates the fields of best and worst performing months
    plt.axhspan(ymin=min(best_stock_prices),
                ymax=max(best_stock_prices),
                xmin=0,
                xmax=1,
                color='#99CC00')
    green_best = mpatches.Patch(color='#99CC00')
    plt.axhspan(ymin=min(worst_stock_prices),
                ymax=max(worst_stock_prices),
                xmin=0,
                xmax=1,
                color='#FF0066')
    red_worst = mpatches.Patch(color='#FF0066')


    # all the labelling, ticks based on dates, and some style stuff
    ax.set_title(stock_title + '\nHistorical Monthly Prices')
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
    ax.legend([green_best, red_worst], [ 'Best Months', 'Worst Months'],
              loc=9, bbox_to_anchor=(0.5, -0.1), ncol=3)


    # sets the display parametres for mouseover (x = time, y = price)
    def price(x): return '$%1.2f'% x
    ax.format_xdata = mdates.DateFormatter('%Y/%m')
    ax.format_ydata = price

    ax.grid(True)

    fig.autofmt_xdate()
    fig.savefig('bonus_02_visual.png')
    plt.show()


if __name__ == '__main__':
    """
    So when you want to view a graph, just comment the other one out.
    """
    # visualize_stock('data/GOOG.json')
    visualize_stock('data/TSE-SO.json')