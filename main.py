import pandas as pd
from pre_processing import pre_process_data
from reports import get_balance_sheet, get_gross_margin, get_profit_loss

data_1 = pd.read_csv('data/01.2021.csv')
data_2 = pd.read_csv('data/02.2021.csv')


# processing data file per month
january_file = pre_process_data(data_1)
february_file = pre_process_data(data_2)

# getting the reports using imported functions
january_BS = get_balance_sheet(january_file)
january_GP = get_gross_margin(january_file)
january_PL = get_profit_loss(january_file)

february_BS = get_balance_sheet(february_file)
february_GP = get_gross_margin(february_file)
february_PL = get_profit_loss(february_file)

# processing data files combined for two months and getting the reports
combined_data = data_1.append(data_2)
print(combined_data['Year/month'].value_counts())

jan_feb_file = pre_process_data(combined_data)

jan_feb_BS = get_balance_sheet(jan_feb_file)
jan_feb_GP = get_gross_margin(jan_feb_file)
jan_feb_PL = get_profit_loss(jan_feb_file)


report = jan_feb_PL.to_excel('data/PNL.xlsx')
