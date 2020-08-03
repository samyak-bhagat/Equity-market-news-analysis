# sm445_Data_Pirates
**This repository holds the project under problem statemet SM445 of SIH2020. The problem statement is provided by FIS Global. The project is a corporate action bot.**





[**INTRODUCTION**]


**Team Name-Data_Pirates**


## Contributors to this project are (Team Member - JK Lakshmipat University, Jaipur):
   1. Muskaan Jain- https://github.com/codracker
      EmailID - muskaanjain@jklu.edu.in, Mobile - 8384854406
   2. Harshaditya Gaur- https://github.com/HarshAditya23
      EmailID - harshadityagaur@jklu.edu.in Mobile - 9116190180
   3. Viral Natani- https://github.com/viralnatani
      EmailID - viralnatani@jklu.edu.in, Mobile - 9414834346
   4. Samyak Bhagat- https://github.com/samyak-bhagat
      EmailID - samyakbhagat@jklu.edu.in, Mobile - 7976378845
   5. Vanshika Sharma- https://github.com/sVanshika
      EmailID - vanshikasharma@jklu.edu.in, Mobile - 8890776688
   6. Sanyukta Tanwar- https://github.com/sanyukta0830
      EmailID - sanyuktatanwar@jklu.edu.in, Mobile - 9414177538

## Mentors:
   1. Dr. Amit Sinhal 
      EmailID - amit.sinhal@jklu.edu.in
      Mobile - +919425476655
   2. Mr. Santosh Kumar 
      EmailID - santosh.verma@jklu.edu.in
      Mobile - +919711492804

**Problem Statement**
The Corporate Action Robot is to be developed for retrieving accurate, and complete information on historical, current, and future expected corporate action in timely manner from free sources.Capability of crawling public web pages to retrieve information (Historical,current, future)
Ability of process information available in free text format like pdf, and MS word document 
Extract important information from retrieved pages/files on corporate action



[**RESOURCES**]



## **This project is being built on the following environment:**
    Processor: Intel(R)
    OS: Windows 7,8,10
    IDE: Anaconda Distributions(Jupyter Notebook)
    Language: Python3
    Web Browser: Google Chrome/Mozilla Firefox
    Additional Softwares: MS-Excel, Adobe PDF Reader, Notepad
    Python Language
            Libraries- Numpy, Pandas, beautifulsoup, urllib, requests

    IDE:
          Anaconda Distributions(Jupyter)     

    Frontend:
          Streamlit

    Backend:
           Spacy
 
    Database:
          MySql





## **Let us first crawl the workflow of the project:**
      > Web Scraping
      > Data Extraction
      > Text Analytics(PDF)
      > Deploying on UI(Streamlit)
     
     
 ## **Refrences**
      1.https://www.investopedia.com/
      
     
   
   
## **Inputs Supported by System**


[**DESIGN**]
  
  
##**ARCHITECTURE DIAGRAM ** 
  
  
  
  
##**DATA FLOW**
  
## **1. Web Scraping**
      > Moneycontrol - @https://www.moneycontrol.com/
      > Rediff.com - @https://www.rediff.com/
      > Livemint - @https://www.livemint.com/
      > Screener.in - @https://www.screener.in/
      
   
**To do scrapping following libraries have been used:**

1.Beautiful Soup- Beautiful Soup is a Python library for pulling data out of HTML and XML files
   >pip install beautifulsoup
   
2.urllib- Collects several modules for working with URls- i.e. requests for opening and reading urls
   >pip install urllib

3.requests- Standard for making HTTP requests
  >pip install requests


## **2. Data Extraction**


## **3. User Interface** 

Streamlit Installation
>pip install streamlit

To run Streamlit
>Type Streamlit run [Filename]


After the successful retrieval and processing of data, the product has to be displayed somewhere. So, the UI(user interface) is built upon the newly developed open-source app framework that is Streamlit[https://www.streamlit.io/]. Various components of streamlit have been taken in use to develop the required UI.

## **Few of the components are:**
    > st.sidebar
    > st.title
    > st.selectbox
    > st.subheader
    > st.button
      
    
 Supporting Libraries with Streamlit-
 
 1. Pandas
 >pip install pandas
 
 2. Numpy
 >pip install numpy



##**ML MODEL**
   >NLP by Spacy using NER(Name Entity Recognition)with custom entities and annotations
