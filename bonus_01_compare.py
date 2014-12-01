""" Bonus question 1: Comparison of two stocks' standard deviations. """

__author__ = 'Dimitar'

import math
import mining


def compare_two_stocks(stock1, stock2):
    """
    Calculates and compares the standard deviation of two stocks' monthly averages.
    :param stock1: String of the first stock's file location
    :param stock2: String of the second stock's file location
    :return: A message indicating which stock has a higher standard deviation, or if they are both the same.
    """

    # Initiates the objects for both stocks from the StockMiner class and calls the method
    # for getting the monthly average lists for both stocks. The variables store a list of
    # tuples of monthly averages.
    first_stock = mining.StockMiner("first_stock", stock1).get_monthly_averages_list()
    second_stock = mining.StockMiner("second_stock", stock2).get_monthly_averages_list()

    # Creates a list for each stock. The lists are populated by the second elements of the tuples
    # within the fetched monthly averages lists. The first elements are undesired since they are dates.
    first_stock_list = [element[1] for element in first_stock]
    second_stock_list = [element[1] for element in second_stock]

    stock1_mean_sum = 0
    stock1_counter = 0
    squared_values_list1_mean = 0
    squared_values_list1 = []

    stock2_mean_sum = 0
    stock2_counter = 0
    squared_values_list2_mean = 0
    squared_values_list2 = []

    # Adds together all the monthly averages from the first stock's monthly averages list.
    for entry in first_stock_list:
        stock1_mean_sum += entry
        stock1_counter += 1

    # Calculates the mean of the first stock's monthly averages.
    stock1_mean = stock1_mean_sum / stock1_counter

    # As per the formula for standard deviation, the first stock's mean is subtracted from
    # each of the monthly averages and those numbers are squared. The results are appended
    # to a list of squared values.
    for value in first_stock_list:
        value_squared1 = (value - stock1_mean) ** 2
        squared_values_list1.append(value_squared1)

    # Sum the squared values from the first stock's squared values list.
    for item in squared_values_list1:
        squared_values_list1_mean += item

    # Calculates the mean of the first stock's squared values.
    squared_values_list1_mean /= len(squared_values_list1)

    # Adds together all the monthly averages from the second stock's monthly averages list.
    for entry in second_stock_list:
        stock2_mean_sum += entry
        stock2_counter += 1

    # Calculates the mean of the second stock's monthly averages.
    stock2_mean = stock2_mean_sum / stock2_counter

    # As per the formula for standard deviation, the second stock's mean is subtracted from
    # each of the monthly averages and those numbers are squared. The results are appended
    # to a list of squared values.
    for value in second_stock_list:
        value_squared2 = (value - stock2_mean) ** 2
        squared_values_list2.append(value_squared2)

    # Sum the squared values from the second stock's squared values list.
    for item in squared_values_list2:
        squared_values_list2_mean += item

    # Calculates the mean of the second stock's squared values.
    squared_values_list2_mean /= len(squared_values_list1)

    # The mean values within the squared values lists are square rooted and rounded to 4 decimal places,
    # the latter is done in order to escape any possible floating-point errors.
    std_dev_1 = round(math.sqrt(squared_values_list1_mean), 4)
    std_dev_2 = round(math.sqrt(squared_values_list2_mean), 4)

    # Compares the standard deviations of the two stocks and returns which one is larger.
    # A case where they are the same is also included.
    if std_dev_1 > std_dev_2:
        return "Stock 1 has a higher standard deviation, which is " + str(std_dev_1)
    elif std_dev_1 < std_dev_2:
        return "Stock 2 has a higher standard deviation, which is " + str(std_dev_2)
    elif std_dev_1 == std_dev_2:
        return "The 2 stocks have the same standard deviation, which is " + str(std_dev_1)
    else:
        raise ValueError("Error with output.")


compare_two_stocks("data/GOOG.json", "data/TSE-SO.json")