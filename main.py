import pandas as pd
from pre_processing import pre_process_data
from reports import get_balance_sheet, get_gross_margin, get_profit_loss

data_1 = pd.read_csv('data/01.2021.csv')
data_2 = pd.read_csv('data/02.2021.csv')

# processing data files combined for two months and getting the reports
combined_files = data_1.append(data_2)
print(combined_files['Year/month'].value_counts())

combined_data = pre_process_data(combined_files)

YTD_BS = get_balance_sheet(combined_data)
YTD_GM = get_gross_margin(combined_data)
YTD_PNL = get_profit_loss(combined_data)

with pd.ExcelWriter('data/financial_reports.xlsx') as writer:
    YTD_BS.to_excel(writer, sheet_name='balance_sheet')
    YTD_GM.to_excel(writer, sheet_name='gross_margin')
    YTD_PNL.to_excel(writer, sheet_name='profit_and_loss')
