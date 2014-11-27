__author__ = 'Dimitar'

import math
from mining import *

stock1 = StockMiner("stock1", "data/GOOG.json")
stock2 = StockMiner("stock2", "data/GOOG.json")


def compare_stocks(stock1, stock2):
    stock1_mean_sum = 0
    stock2_mean_sum = 0
    stock1_counter = 0
    stock2_counter = 0
    squared_values_list1_mean = 0
    squared_values_list2_mean = 0
    squared_values_list1 = []
    squared_values_list2 = []
    for entry in stock1:
        stock1_mean_sum += entry
        stock1_counter += 1
    stock1_mean = stock1_mean_sum / stock1_counter
    for entry in stock2:
        stock2_mean_sum += entry
        stock2_counter += 1
    stock2_mean = stock2_mean_sum / stock2_counter
    for value in stock1:
        value_squared1 = (value - stock1_mean) ** 2
        squared_values_list1.append(value_squared1)
    for value in stock2:
        value_squared2 = (value - stock2_mean) ** 2
        squared_values_list2.append(value_squared2)
    for item in squared_values_list1:
        squared_values_list1_mean += item
    squared_values_list1_mean / len(squared_values_list1)
    std_dev_1 = math.sqrt(squared_values_list1_mean)
    print(std_dev_1)
    for item in squared_values_list2:
        squared_values_list2_mean += item
    squared_values_list2_mean / len(squared_values_list2)
    std_dev_2 = math.sqrt(squared_values_list2_mean)
    print(std_dev_2)
    if std_dev_1 > std_dev_2:
        print("Stock 1 has a higher standard deviation.")
    elif std_dev_1 < std_dev_2:
        print("Stock 2 has a higher standard deviation.")
    elif std_dev_1 == std_dev_2:
        print("The 2 stocks have the same standard deviation.")
    else:
        print("Error")

compare_stocks(stock1, stock2)