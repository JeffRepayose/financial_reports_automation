import pandas as pd
import numpy as np


def get_balance_sheet(data):
    pivot = pd.pivot_table(data=data,
                           values=['Amount in local currency'],
                           index=['Category 1', 'Category', 'GL Description'],
                           columns=['Year/month'],
                           aggfunc=np.sum,
                           margins=True,
                           margins_name='YTD Total')
    bs = pivot.loc[['ASSET', 'LIABILITIES', 'YTD Total']].replace(np.NaN, 0)
    balance_sheet = bs.rename(index={'YTD Total': 'EQUITIES'})
    return balance_sheet


def get_gross_margin(data):
    pivot = pd.pivot_table(data=data,
                           values=['Amount in local currency'],
                           index=['Category',  'GL Description'],
                           columns=['Year/month'],
                           aggfunc=np.sum,
                           margins=True,
                           margins_name='YTD Total')
    gm = pivot.loc[['Sales', 'Cost of Sales', 'YTD Total']].replace(np.NaN, 0)
    gross_margin = gm.rename(index={'YTD Total': 'Gross Margin'})
    return gross_margin


def get_profit_loss(data):
    pivot = pd.pivot_table(data=data,
                            values=['Amount in local currency'],
                            index=['Category 1', 'Category', 'GL Description'],
                            columns=['Year/month'],
                            aggfunc=np.sum,
                            margins=True,
                            margins_name='YTD Total')
    pnl = pivot.loc[['Gross Margin', 'Operating Expenses', 'YTD Total']].replace(np.NaN, 0)
    profit_loss = pnl.rename(index={'YTD Total': 'Net Profit'})
    return profit_loss
