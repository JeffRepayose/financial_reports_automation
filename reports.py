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
    balance_sheet = pivot.loc['BS'].replace(np.NaN, 0)
    return balance_sheet


def get_gross_margin(data):
    pivot = pd.pivot_table(data=data,
                           values=['Amount in local currency'],
                           index=['Category 1', 'Category',  'GL Description'],
                           columns=['Year/month'],
                           aggfunc=np.sum,
                           margins=True,
                           margins_name='YTD Total')
    gross_margin = pivot.loc[['Gross Margin']].replace(np.NaN, 0)
    return gross_margin


def get_profit_loss(data):
    pivot = pd.pivot_table(data=data,
                            values=['Amount in local currency'],
                            index=['Category 1', 'Category', 'GL Description'],
                            columns=['Year/month'],
                            aggfunc=np.sum,
                            margins=True,
                            margins_name='YTD Total')
    profit_loss = pivot.loc[['Gross Margin', 'Operating Expenses']].replace(np.NaN, 0)
    return profit_loss



