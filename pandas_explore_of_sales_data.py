# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 17:00:29 2022

@author: bpiechocki
"""
from os import path
import pandas as pd

DATA_DIR = '\\Users\\bpiechocki\\OneDrive - Palco Telecom Service Inc\\Desktop\\Python and FFL\\Further Studies\\Us Regional Sales Data Project'
sales_order = pd.read_csv(path.join(DATA_DIR, 'sales_order_sheet.csv'))
sales_order.shape
sales_order.head()
sales_order.tail()
pd.isna(sales_order) #check for missing values
sales_order.describe() # Calculate summary stats
sales_order_describe = sales_order.describe() # termed summary stats into a dataframe
sales_order.groupby('_SalesTeamID').describe() # show summary stats divided by _SalesTeamID
sales_order.plot.bar() #Doesn't work for this data, Maybe I need to choose a variable
sales_order.plot.box() 
sales_order.plot.density()#It made an output but it looks like rubbish

"""
Report to summarize findings:
There are 7,990 observations. This should be sufficient for our purposes.  There is other data that I would like to use
to create a bigger set. 

Some of the data needs to be reformatted.  For example, the unit price and cost data has commas, so they are not being
intrepreted as integers.     

No data are missing, which is positive. 

"""
Look at pg. 73

