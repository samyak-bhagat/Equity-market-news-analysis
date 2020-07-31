#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np

from historical_data import *

# In[4]:
company = pd.read_csv(r'C:\Users\SanyuktaTanwar\Desktop\New folder\moneycontrol_companies.csv')
tolist=list(company['Company Name'])
main_title = st.title("Corporate Action Robot")
st.sidebar.title("Search")

category_selectbox = st.sidebar.selectbox(
    'What do you want to see?',
    ('Historical Data', 'News', 'Announcements')
)

#search bar for company
company_name = st.selectbox("Enter Company's Name",tolist)


if(category_selectbox == 'Historical Data'):

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
            st.write("Board Meetings")
            st.dataframe(get_board_meetings(links[0]))

        elif(corp_action == 'AGM/EGM'):
            st.write("AGM/EGM")
            st.dataframe(get_AGM_EGM(links[1]))
            
        elif(corp_action == 'Dividend'):
            st.write("Dividend")
            st.dataframe(get_dividend(links[2]))

        

        elif(corp_action == 'Bonus'):
            st.write("Bonus")
            st.dataframe(get_bonus(links[3]))
            
        elif(corp_action == 'Splits'):
            st.write("Splits")
            st.dataframe(get_split(links[4]))
           
        elif(corp_action == 'Rights'):
            st.write("Rights")
            st.dataframe(get_rights(links[5]))
            
            
elif(category_selectbox == 'News'):
    st.subheader('News')




elif(category_selectbox == 'Announcements'):
    st.subheader('Announcements')







# In[ ]:




