## Automation of Financial Reporting

### Description:
This project is about generating financial reports (balance sheet & income statement) using one job in python provided that monthly files extracted from SAP will be saved in one directory.

### Methodology:
I created a python file 'pre_processing.py' in order to clean up the data ensuring the amount in raw data will be float type, and doing a vlookup for the GL codes & description, for easy creation of pivot.

I also created 'reports.py' file where it has different functions in creating specific pivot reports such as balance sheet, gross margin and profit&loss.

In main.py, this is where put the job in generating the reports. Here's there's one function started with an if statement to check if date today is not equal to 1, if false, it will push forward the job in the following sequence:
1. Getting all the csv files in the specific directory using the for loop.
2. Concatenating all the data from csv file in the empty data frame 'all_data'.
3. Pre-processing the concatenated data using the pre_processing python file. I also added a print code just to check the value counts of DF.
4. Generating the pivot from the pre_processed data using the functions in reports.py.
5. Putting the generated pivot in Excel file using ExcelWriter, and saving it in the directory,

### Usage:
This automation is useful in generating monthly reports where data is coming from SAP, and will save more time which can be used instead in analyzing the reports itself and provide more meaningful insights to help the business.

### For Improvement:
As of now, I only applied the report format which is as per the requirement in my current job.
I will soon furnish the reports function and add financial ratios to make it more useful for analysis.

# Credit 
Code created by Justine Panetta and Jeff Repayose
