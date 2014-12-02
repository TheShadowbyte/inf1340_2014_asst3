#!/usr/bin/env python3

""" This  """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from mining import *
from bonus_01_compare import *
from bonus_02_visual import *


def test_goog():
    google_stock = StockMiner('GOOG', 'data/GOOG.json')
    assert google_stock.six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38),
                                              ('2008/01', 599.42), ('2008/05', 576.29), ('2008/06', 555.34)]
    assert google_stock.six_worst_months() == [('2004/08', 104.66), ('2004/09', 116.38), ('2004/10', 164.52),
                                               ('2004/11', 177.09), ('2004/12', 181.01), ('2005/03', 181.18)]


# tests that correct results are returned for TSE-SO stocks
def test_tse():
    tse_stock = StockMiner('TSE-SO', 'data/TSE-SO.json')
    assert six_best_months() ==

    assert six_worst_months() ==

# Tests that mining throws the correct error when files are missing
def test_files_presence():
    with pytest.raises(FileNotFoundError):
        StockMiner('GOOG', "")

# Tests that mining throws the correct error when files are of the wrong type (not .jsons)
def test_file_types():
    with pytest.raises(TypeError):
        StockMiner('GOOG', "data/file.txt")

# Tests that mining throws the correct error when .jsons are empty
def test_enough_data():
    with pytest.raises(ValueError):
        StockMiner('GOOG', 'data/empty.json')

# Tests that bonus_01_compare returns the correct values
def test_bonus_01():
    assert compare_two_stocks("data/GOOG.json", "data/TSE-SO.json") == \
        "Stock 1 has a higher standard deviation, which is 143.6229"
