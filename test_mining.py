#!/usr/bin/env python3

""" This  """

__author__ = 'Kyungho Jung & Dimitar & Curtis'
# imports one per line
import pytest
from mining import *
from bonus_01_compare import *


def test_goog():
    google_stock = StockMiner('GOOG', 'data/GOOG.json')
    assert google_stock.six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38),
                                              ('2008/01', 599.42), ('2008/05', 576.29), ('2008/06', 555.34)]
    assert google_stock.six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52),
                                               ('2004/11', 177.09), ('2004/12', 181.01), ('2005/03', 181.18)]


# tests that correct results are returned for TSE-SO stocks
def test_tse():
    tse_stock = StockMiner('TSE-SO', 'data/TSE-SO.json')
    assert tse_stock.six_best_months() == [('2007/12', 20.98), ('2007/11', 20.89), ('2013/05', 19.96),
                                           ('2013/06', 19.94), ('2013/04', 19.65), ('2007/10', 19.11)]
    assert tse_stock.six_worst_months() == [('2009/03', 1.74), ('2008/11', 2.08), ('2008/12', 2.25),
                                            ('2009/02', 2.41), ('2009/04', 2.75), ('2009/01', 3.14)]


# Tests that mining throws the correct error when files are missing
def test_files_presence():
    with pytest.raises(FileNotFoundError):
        StockMiner('WRONG_FILE_NAME', "data/no_such_file.json")
    with pytest.raises(FileNotFoundError):
        StockMiner('EMPTY_PATH', "")


# Tests that mining throws the correct error when files are of the wrong type (not .jsons)
def test_file_types():
    with pytest.raises(TypeError):
        StockMiner('WRONG_EXTENSION', "data/file.txt")


# Tests that mining throws the correct error when .jsons are empty
def test_enough_data():
    with pytest.raises(ValueError):
        StockMiner('LessThan6Month', 'data/less_than_6_month.json')

# Tests if stock json file has a correct structure
def test_incorrect_format_json():
    with pytest.raises(KeyError):
        StockMiner('KeyError_STOCK', 'data/key_error_file.json')
    with pytest.raises(KeyError):
        StockMiner('EMPTY_FILE', 'data/empty.json')

# Tests that bonus_01_compare returns the correct values
def test_bonus_01():
    assert compare_two_stocks("data/GOOG.json", "data/TSE-SO.json") == \
        "GOOG has a higher standard deviation, which is 143.6229"
