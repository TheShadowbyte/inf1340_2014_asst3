__author__ = 'curtismccord'

#!/usr/bin/env python
# a bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

#Import jsons and functions OR function results


six_best_months = [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42), ('2008/05', 576.29), ('2008/06', 555.34)]

six_worst_months = [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01), ('2005/03', 181.18)]

best_stock_prices = []
best_stock_dates = []
worst_stock_prices = []
worst_stock_dates = []

def sort_stock_tuples(stock_result):
    """
    (list of tuples) - > list
    """
    for datum in stock_result:
        if datum[1] > 300:
            best_stock_dates.append(datum[0])
            best_stock_prices.append(datum[1])
        else:
            worst_stock_dates.append(datum[0])
            worst_stock_prices.append(datum[1])


sort_stock_tuples(six_best_months)
sort_stock_tuples(six_worst_months)

N = 6

ind = np.arange(N)  # the x locations for the groups
width = 0.45       # the width of the bars

fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)

prices1 = ax1.bar(ind, best_stock_prices, width, color='#99CC00', align='center')

prices2 = ax2.bar(ind, worst_stock_prices, width, color='#FF0066', align='center')

# add some text for labels, title and axes ticks
ax1.set_title('stock_name\n best average prices')
ax2.set_title('stock_name\n worst average prices')
ax1.set_xticks(ind)
ax2.set_xticks(ind)
ax2.spines["left"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.set_xticklabels( (best_stock_dates), rotation='90')
ax2.set_xticklabels( (worst_stock_dates), rotation='90')
ax1.yaxis.grid(b=True, linestyle="--")
ax2.yaxis.grid(b=True, linestyle="--")
ax1.set_ylabel('$ USD')

plt.tight_layout()
fig.savefig('stock_bar.png', transparent=True)
plt.show()