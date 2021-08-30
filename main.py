import pandas as pd
from pre_processing import pre_process_data
from reports import get_balance_sheet, get_gross_margin, get_profit_loss
import glob


# reading all csv files in the folder and concatenating them
all_data = pd.DataFrame()
path = '/Users/jennifersequina/Desktop/Projects/financial_reports_automation/data/monthly_file/'
for file in glob.glob(path+'*.csv'):
    x = pd.read_csv(file, low_memory=False)
    all_data = pd.concat([all_data, x], axis=0)

# pre-processing of data using the function created
processed_data = pre_process_data(all_data)

print(processed_data['Year/month'].value_counts())

# generating reports using functions
YTD_BS = get_balance_sheet(processed_data)
YTD_GM = get_gross_margin(processed_data)
YTD_PNL = get_profit_loss(processed_data)

# saving the reports into one excel file
with pd.ExcelWriter('data/financial_reports.xlsx') as writer:
    YTD_BS.to_excel(writer, sheet_name='balance_sheet')
    YTD_GM.to_excel(writer, sheet_name='gross_margin')
    YTD_PNL.to_excel(writer, sheet_name='profit_and_loss')
