#!/usr/bin/env python3

""" Reads Jsons containing daily stock data and returns the best and worst performances by month """
__author__ = 'Curtis and Dimitar and Shawn'

# imports one per line
import json
import datetime

class StockMiner():

    def __init__(self, stock_name, stock_file_name):
        """
        Opens JSONs containing historical stock data and compiles monthly averages of trade volume and closing price.
        :param stock_name: string that will store the stock name of the chosen JSON file
        :param stock_file_name: A JSON formatted file where daily stock data is kept
        :return: monthly_averages, a list of tuples of monthly stock data
        """

        self.stock_name = stock_name
        self.monthly_averages = []
        self.stock_data = self.read_json_from_file(stock_file_name)
        self.init_monthly_averages_list()

    def init_monthly_averages_list(self):
        """
        Initialization function to store the month strings and corresponding stock averages to the monthly_averages list
        """
        # temporary storage dictionaries to store monthly sum of numerator and denominator
        monthly_sum = {}

        for daily_stock_result in self.stock_data:
            year_month = datetime.datetime.strptime(daily_stock_result['Date'], '%Y-%m-%d').strftime('%Y/%m')
            trade_volume = int(daily_stock_result['Volume'])
            closing = float(daily_stock_result['Close'])

            # creates dictionary to store numerator and denominator for each month
            # year_month as a key, and pair of numerator and denominator as a value (dictionary type)
            if year_month in monthly_sum:
                monthly_sum[year_month]['numerator'] += trade_volume * closing
                monthly_sum[year_month]['denominator'] += trade_volume
            else:
                monthly_sum[year_month] = {'numerator': trade_volume * closing, 'denominator': trade_volume}

        # Once monthly sum is compiled, produce the list of tuples to store monthly averages values.
        for yr_month_key in monthly_sum:
            numerator = monthly_sum[yr_month_key]['numerator']
            denominator = monthly_sum[yr_month_key]['denominator']
            self.monthly_averages.append((yr_month_key, round(numerator/denominator, 2)))

        # Raise ValueError if the given stock file has less than 5 distinct months
        if len(self.monthly_averages) <= 5:
            raise ValueError("Given Stock file does not contain 5 distinct months")

    def six_best_months(self):
        """
        Using the monthly averages generated by red_stock_data, generates a list of the six best performing months
        by volume and capacity
        (lst) -> (tup, le)
        :return: best_six, a list of the six best performing months of monthly_averages
        """
        # Use monthly_averages variable and apply sorting algorithms on list to get the best 6
        best_six = sorted(self.monthly_averages, key=lambda averages: averages[1], reverse=True)[:6]
        return best_six

    def six_worst_months(self):
        """
        Using the monthly averages generated by red_stock_data, generates a list of the six worst performing months
        by volume and capacity
        (lst) -> (tup, le)
        :return: worst_six, a list of the six best performing months of monthly_averages
        """
        # Use monthly_averages variable and apply sorting algorithms on list to get the worst 6
        worst_six = sorted(self.monthly_averages, key=lambda averages: averages[1])[:6]
        return worst_six

    @staticmethod
    def read_json_from_file(file_name):
        """
        Opens a JSON with file reader and loads it as a Python data structure
        :param file_name: a JSON formatted file
        :return: list converted from json file
        """
        with open(file_name) as file_handle:
            file_contents = file_handle.read()

        return json.loads(file_contents)

    def get_monthly_averages_list(self):
        """
        Return the list of tuples containing the monthly averages
        :return:List, tuples of monthly averages, sorted from smalled to largest.
        """

        sorted_list = sorted(self.monthly_averages, key=lambda yr_month: yr_month[0])
        return sorted_list
