#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np

from historical_data import *
from company_details import *

# In[4]:
company = pd.read_csv('company.csv')
tolist=list(company['Company Name'])
main_title = st.title("Corporate Action Robot")
st.sidebar.title("Search")

#category_selectbox = st.sidebar.selectbox('What do you want to see?',('Historical Data', 'News', 'Announcements', 'Company Details'))

category_selectbox = st.sidebar.selectbox(
    'What do you want to see?',
    ('Historical Data',  'Announcements', 'Company Details')
)

#search bar for company
#company_name = st.selectbox("Enter Company's Name",tolist)
 

if(category_selectbox == 'Historical Data'):

    company_name = st.selectbox("Enter Company's Name",tolist)

    st.subheader('Historical Data')

    corp_action = st.selectbox('Which Corporate Action you want to see?',
            ('Board Meetings', 'Dividend', 'AGM/EGM', 'Bonus', 'Splits', 'Rights')
    )

    if(st.button("Search")):

    
        
            
        x = company.loc[company['Company Name']==company_name]
        #st.write(x)
        l = x['Link'].iloc[0]
        #st.write(l)
        links = corporate_action_links(l)

        if(corp_action == 'Board Meetings'):
            st.info("Board Meetings")
            st.dataframe(get_board_meetings(links[0]))

        elif(corp_action == 'AGM/EGM'):
            st.info("AGM/EGM")
            st.dataframe(get_AGM_EGM(links[1]))
            
        elif(corp_action == 'Dividend'):
            st.info("Dividend")
            st.dataframe(get_dividend(links[2]))

        elif(corp_action == 'Bonus'):
            st.info("Bonus")
            st.dataframe(get_bonus(links[3]))
            
        elif(corp_action == 'Splits'):
            st.info("Splits")
            st.dataframe(get_split(links[4]))
           
        elif(corp_action == 'Rights'):
            st.info("Rights")
            st.dataframe(get_rights(links[5]))
            
            
elif(category_selectbox == 'News'):
    st.subheader('News')
    st.write(company_name)
    




elif(category_selectbox == 'Announcements'):
    st.subheader('Announcements')

    company_name = st.selectbox("Enter Company's Name",tolist)

    if(st.button("Search")):

        x = company.loc[company['Company Name']==company_name]
            #st.write(x)
        l = x['Link'].iloc[0]

        #link='https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS'

        link = l

        def get_announcement(link):
            url=requests.get(link).text
            soup = BeautifulSoup(url,'lxml')
            x = soup.find('div',{'class':'col_right'})
            #print(find)
            x=x.find('div',{'class':'viewmore'})
            x=x.find('a').get('href')
            #print(x)
            x=x+'&pno='
            for i in range(1,10):
                y=x+'&pno='+str(i)
                #print(y)
                get_announcement_summary(y)
                y=''
                
                
            #print(x)

        def get_announcement_summary(x):
            url=requests.get(x).text
            soup = BeautifulSoup(url,'lxml')
            x = soup.find_all('ul',{'class':'announe_list MT20'})
            for result in x:
                li_tags=result.find_all('li')
                for i in li_tags:
                    st.write("Date and Time: ",i.find('ctag').get_text())
                    st.write("Title: ",i.find('a',{'target':'_blank'}).get_text())
                    st.write("Body: ",i.find('p',{'class':'MT2'}).get_text())
                    #print(i.find('a',{'class':'ic_pdf'}))
                    temp=i.find('a',{'class':'ic_pdf'})
                    #print(temp)    
                    if temp is None:
                        st.write("Link: ",temp)
                        st.write("**************")   
                    else:
                        st.write("Link: ",temp.get('href'))
                        st.write("**************")
                    
                

        get_announcement(link)


elif(category_selectbox == 'Company Details'):

    bn = pd.read_csv('bse_nse.csv')

    company_name = st.selectbox("Enter Company's Name", list(bn['Name']))

    st.subheader('Company Details')

    comp_details = st.selectbox('See following Company Details',
            ('Quarters', 'Profit & Loss', 'Balance Sheet', 'Cash Flow', 'Ratios', 'Investors')
    )

    if(st.button("Search")):

        #screener.in -> links
        
        bse_code=0
        nse_code=""
        x = bn.loc[ bn['Name'] == company_name]
        bse_code = str(int(x['BSE Code'].iloc[0]))
        nse_code = str(x['NSE Code'].iloc[0])
        
        if bse_code != 'nan':
            link = 'https://www.screener.in/company/' + bse_code + '/consolidated/'
        elif nse_code != 'nan':
            link = 'https://www.screener.in/company/' + nse_code + '/consolidated/'
        else:
            link=''
        
        #st.write(link)

        #get_announcement_bse(link)

        #processing link and basic scraping '''
        url=requests.get(link).text
        soup = BeautifulSoup(url,'lxml')
        x = soup.find_all('table',{'class':'data-table'})

        if(comp_details == 'Quarters'):
            st.info("Quarterly Results (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[0]))
        
        elif(comp_details == 'Profit & Loss'):
            st.info("Profit & Loss (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[1]))
        
        elif(comp_details == 'Balance Sheet'):
            st.info("Balance Sheet (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[2]))
        
        elif(comp_details == 'Cash Flow'):
            st.info("Cash Flows (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[3]))
        
        elif(comp_details == 'Ratios'):
            st.info("Ratios (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[4]))
        
        elif(comp_details == 'Investors'):
            st.info("Shareholding pattern (in percentages)")
            st.dataframe(getdata(x[5]))







# In[ ]:




