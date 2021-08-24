import pandas as pd
import numpy as np


def get_balance_sheet(data):
    pivot = pd.pivot_table(data=data,
                           values=['Amount in local currency'],
                           index=['Category', 'Category 1', 'GL Description'],
                           columns=['Year/month'],
                           aggfunc=np.sum,
                           margins=True,
                           margins_name='YTD Total')
    balance_sheet = pivot.loc['BS']
    return balance_sheet


def get_gross_margin(data):
    pivot = pd.pivot_table(data=data,
                           values=['Amount in local currency'],
                           index=['Category', 'Category 1', 'GL Description'],
                           columns=['Year/month'],
                           aggfunc=np.sum,
                           margins=True,
                           margins_name='YTD Total')
    gross_margin = pivot.loc[['Sales', 'Cost of Sales']]
    return gross_margin


def get_profit_loss(data):
    pivot = pd.pivot_table(data=data,
                            values=['Amount in local currency'],
                            index=['Category', 'Category 1', 'GL Description'],
                            columns=['Year/month'],
                            aggfunc=np.sum,
                            margins=True,
                            margins_name='YTD Total')
    profit_loss = pivot.loc[['Sales', 'Cost of Sales', 'Expenses']]
    return profit_loss

