import pandas as pd
from pandas.api.types import is_string_dtype
import numpy as np

gl_codes = pd.read_csv('data/gl_codes.csv')


def pre_process_data(data):
    concat_data = data.merge(gl_codes, on='Account', how='left')
    if is_string_dtype(concat_data['Amount in local currency']):
        concat_data['Amount in local currency'] = concat_data['Amount in local currency'].str.replace(',', '')
        concat_data['Amount in local currency'] = (concat_data['Amount in local currency'].astype(np.float64).round(2))
    processed_data = concat_data
    return processed_data


# def as_currency(amount):
#     if amount >= 0:
#         return '${:,.2f}'.format(amount)
#     else:
#         return '-${:,.2f}'.format(-amount)