''' extracting
1. quarterly results
2. profit and loss
3. balance sheet
4. cash flow
5. ratios
6. shareholding pattern
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import numpy as np

import pandas as pd



    
def getdata(My_table):
    row_dict = {} #dict to append to dataframe as row
    columns = [i.get_text().strip() for i in My_table.find_all('th') ]#list for column name 
        #print(columns)
        
    for i in range(len(columns)):
        row_dict[i] = columns[i]
        #print(row_dict)
        
    df = pd.DataFrame(row_dict, index=[0]) #final dataframe
               
    tr = My_table.find_all('tr')  
    for r in tr:
        th = [i.get_text().strip() for i in r.find_all('td')]  #list of 1 row of dataframe
        if len(th)>0:
            for i in range(len(th)):
                row_dict[i] = th[i]
            #print(row_dict)
            df = df.append(row_dict, ignore_index=True)
            #display(df)
                
        
    df.columns=list(df.iloc[0])
    df = df.drop(0)
    #display(df)
    return df