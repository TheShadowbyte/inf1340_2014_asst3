#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
#Global variables.
monthly_averages = []


def read_stock_data(stock_name, stock_file_name):
    """
    docstring
    :param stock_name:
    :param stock_file_name:
    :return:
    """

    #temporary storage arrays to store monthly sum of numerator and denominator
    monthly_sum = {}

    #read json file
    stock_data_history = read_json_from_file(stock_file_name)

    for daily_stock_result in stock_data_history:
        year_month = datetime.datetime.strptime(daily_stock_result['Date'], '%Y-%m-%d').strftime('%Y/%m')
        trade_volume = int(daily_stock_result['Volume'])
        closing = float(daily_stock_result['Close'])

        #creats dictionary to store numerator and denominator for each month
        # year_month as a key, and pair of numerator and denominator as a value (dictionary type)
        if year_month in monthly_sum:
            monthly_sum[year_month]['numerator'] += trade_volume * closing
            monthly_sum[year_month]['denominator'] += trade_volume
        else:
            monthly_sum[year_month] = {'numerator': trade_volume * closing, 'denominator': trade_volume}

    #Once monthly sum is compiled, produce the list of tuples to store monthly averages values.
    for yr_month_key in monthly_sum:
        numerator = monthly_sum[yr_month_key]['numerator']
        denominator = monthly_sum[yr_month_key]['denominator']
        monthly_averages.append((yr_month_key, round(numerator/denominator,2)))

    return

def six_best_months():
    """

    :return:
    """

    #Use monthly_averages variable and apply sorting algorithms on list to get the best 6

    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    """

    :return:
    """

    #Use monthly_averages variable and apply sorting algorithms on list to get the worst 6

    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    """

    :param file_name:
    :return:
    """
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
