#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np

from historical_data import *
from company_details import *

# In[4]:


company = pd.read_csv('moneycontrol_companies.csv')
company = company.sort_values(by=['Company Name'], ignore_index=True)
tolist=list(company['Company Name'])
main_title = st.title("Corporate Action Robot")
st.sidebar.title("Search")

category_selectbox = st.sidebar.selectbox(
    'What do you want to see?',
    ('Historical Data', 'Announcements')
)

#search bar for company
company_name = st.multiselect("Enter Company's Name",tolist)


if(category_selectbox == 'Historical Data'):

    if(st.button("Search")):
        
        board = pd.DataFrame()
        agm = pd.DataFrame()
        dividend = pd.DataFrame()
        bonus = pd.DataFrame()
        splits = pd.DataFrame()
        rights = pd.DataFrame()

        for j in company_name:    
            x = company.loc[company['Company Name']==j]
            l = x['Link'].iloc[0]
            links = corporate_action_links(l)


            temp = get_board_meetings(links[0])
            temp['Company'] = [j]*len(temp)
            board = board.append(temp, ignore_index=True)

            temp = get_AGM_EGM(links[1])
            temp['Company'] = [j]*len(temp)
            agm = agm.append(temp, ignore_index=True)
            
            temp = get_dividend(links[2])
            temp['Company'] = [j]*len(temp)
            dividend = dividend.append(temp, ignore_index=True)

            temp = get_bonus(links[3])
            temp['Company'] = [j]*len(temp) 
            bonus = bonus.append(temp, ignore_index=True)

            temp = get_split(links[4])
            temp['Company'] = [j]*len(temp)
            splits = splits.append(temp, ignore_index=True)

            temp = get_split(links[4])
            temp['Company'] = [j]*len(temp)
            rights = rights.append(temp, ignore_index=True)

        st.info("Board Meetings")
        temp = board.sort_values(by=['Meeting Date'], ignore_index=True)
        st.dataframe(temp.iloc[::-1])

        st.info("AGM/EGM")

        #st.dataframe(agm)

        temp = agm.sort_values(by=['Announcement Date'], ignore_index=True)
        st.dataframe(temp.iloc[::-1])

        st.info("Dividend")
        temp = dividend.sort_values(by=['Announcement Date'], ignore_index=True)
        st.dataframe(temp.iloc[::-1])

        st.info("Bonus")
        temp = bonus.sort_values(by=['Announcement Date'], ignore_index=True)
        st.dataframe(temp.iloc[::-1])

        st.info("Splits")
        temp = splits.sort_values(by=['Announcement Date'], ignore_index=True)
        st.dataframe(temp.iloc[::-1])

        st.info("Rights")
        temp = rights.sort_values(by=['Announcement Date'], ignore_index=True)
        st.dataframe(temp.iloc[::-1])
         
            
elif(category_selectbox == 'News'):
    st.subheader('News')




elif(category_selectbox == 'Announcements'):
    st.subheader('Announcements')


    if(st.button("Search")):
        for i in company_name:
            st.header(i)    
            x = company.loc[company['Company Name']==i]
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


    #st.subheader('Company Details')

    #comp_details = st.selectbox('See following Company Details',
    #       ('Quarters', 'Profit & Loss', 'Balance Sheet', 'Cash Flow', 'Ratios', 'Investors')
    #)

    if(st.button("Search")):
        for i in company_name:
            #screener.in -> links
            
            bse_code=0
            nse_code=""
            x = bn.loc[ bn['Name'] == i]
            bse_code = str(x['BSE Code'].iloc[0])
            nse_code = str(x['NSE Code'].iloc[0])
            
            if bse_code != 'nan':
                bse_code = str(int(bse_code))
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

            #if(comp_details == 'Quarters'):
            st.info("Quarterly Results (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[0]))
            
            #elif(comp_details == 'Profit & Loss'):
            st.info("Profit & Loss (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[1]))
            
            #elif(comp_details == 'Balance Sheet'):
            st.info("Balance Sheet (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[2]))
            
            #elif(comp_details == 'Cash Flow'):
            st.info("Cash Flows (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[3]))
            
            #elif(comp_details == 'Ratios'):
            st.info("Ratios (Consolidated Figures in Rs. Crores)")
            st.dataframe(getdata(x[4]))
            
            #elif(comp_details == 'Investors'):
            st.info("Shareholding pattern (in percentages)")
            st.dataframe(getdata(x[5]))







# In[ ]:




