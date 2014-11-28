__author__ = 'curtismccord'

#!/usr/bin/env python
"""
Makes a bar graph out of imported lists of stock tuples
"""
import numpy as np
import matplotlib.pyplot as plt
import mining
import json
import datetime

# Gets the required lists of tuples from mining.py

# stock_name = input('Please enter stock name: ')
# if stock_name != str:
#     raise TypeError

stock_name = 'GOOG'

best_months = mining.StockMiner('GOOG', 'data/GOOG.json').six_best_months()
worst_months = mining.StockMiner('GOOG', 'data/GOOG.json').six_worst_months()

# Some empty lists for storage

best_stock_prices = []
best_stock_dates = []
worst_stock_prices = []
worst_stock_dates = []



def sort_stock_results(best_months_list, worst_months_list):
    """
    Takes the two results of StockMiner's lists and organizes the contents into variables for graphing
    :param best_months_list:
    :param worst_months_list:
    :return:
    """
    for datum in best_months:
        best_stock_dates.append(datum[0])
        best_stock_prices.append(datum[1])

    for datum in worst_months:
        worst_stock_dates.append(datum[0])
        worst_stock_prices.append(datum[1])


# Runs the functions so we can make a graph
sort_stock_results(best_months, worst_months)

N = 6
ind = np.arange(N)  # the x locations for the groups
width = 0.5       # sets the width of the bars
# sets two subplot objects to share a y axis
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

# names the subplots and sets their parametres
prices1 = ax1.bar(ind, best_stock_prices, width, color='#99CC00', align='center')
prices2 = ax2.bar(ind, worst_stock_prices, width, color='#FF0066', align='center')

# sets the titles for each subplots
ax1.set_title(stock_name + '\n best average prices')
ax2.set_title(stock_name + '\n worst average prices')

# sets ticks along the x-axis
ax1.set_xticks(ind)
ax2.set_xticks(ind)

# makes the inside borders invisible
ax2.spines["left"].set_visible(False)
ax1.spines["right"].set_visible(False)

# sets the x-axis labels using the variables generated above and makes them vertical
ax1.set_xticklabels((best_stock_dates), rotation='90')
ax2.set_xticklabels((worst_stock_dates), rotation='90')

# puts a dotted line grid over the subplots to improve visibility
ax1.yaxis.grid(b=True, linestyle="--")
ax2.yaxis.grid(b=True, linestyle="--")

# sets the y- axis label... with subtle LaTeX!
ax1.set_ylabel(r'$\$$ USD')

# tightens and aligns formatting
plt.tight_layout()

# makes the plot interactive
# plt.ion()

# saves a .png file in the directory
fig.savefig('stock_bar.png', transparent=True)

plt.show()
