import pandas as pd
from pre_processing import pre_process_data
from reports import get_balance_sheet, get_gross_margin, get_profit_loss
import glob
import schedule
import time
from datetime import date


# Credit Super Programmer - Jeff Repayose
msg = "XXXXXXXXXXXXXXXXXXXXXXX"
def fs_auto():
    if date.today().day != 1:
        return

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
    ytd_bs = get_balance_sheet(processed_data)
    ytd_gm = get_gross_margin(processed_data)
    ytd_pnl = get_profit_loss(processed_data)

    # saving the reports into one excel file
    with pd.ExcelWriter('data/financial_reports.xlsx') as writer: 
        ytd_bs.to_excel(writer, sheet_name='balance_sheet')
        ytd_gm.to_excel(writer, sheet_name='gross_margin')
        ytd_pnl.to_excel(writer, sheet_name='profit_and_loss') 
 

schedule.every().day.at("10:00").do(fs_auto) 

while 1:
    schedule.run_pending()
    time.sleep(1)

# Thanks again to Jeff Repayose for the code
