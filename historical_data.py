from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import pandas as pd
from IPython.display import display_html
   

''' links to all corporate actions of a company'''
def corporate_action_links(link):
    viewmore_link = get_viewmore(link)
    url = requests.get(viewmore_link).text
    soup = BeautifulSoup(url,'lxml')

    board_meetings = soup.find('a', {'class':'Boardmeetings'}).get('href')
    agm_egm= soup.find('a', {'class':'AGMEGM'}).get('href')
    dividends= soup.find('a', {'class':'Dividends'}).get('href')
    bonus= soup.find('a', {'class':'Bonus'}).get('href')
    splits= soup.find('a', {'class':'Splits'}).get('href')
    rights= soup.find('a', {'class':'Rights'}).get('href')
    
    return [board_meetings, agm_egm, dividends, bonus, splits, rights]

''' link to viewmore tab'''
def get_viewmore(link):
    url = requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    viewmore = soup.find('div', {'class':'corportate_action'}).find('div', {'class':'viewmore'}).find('a').get('href')

    return viewmore

''' methods for scraping corp actions '''
def get_board_meetings(link):
    url=requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    My_table = soup.find('table',{'class':'mctable1 MT20 board-meeting-table'}) #html of table
    
    td = My_table.find_all('td') #column tag
    td = [(i.text) for i in td] #removing tag
    
    if len(td)>=2:
        date=[]
        remark=[]
        for i in range(0,len(td),2):
            date.append(td[i])
            remark.append(td[i+1])

        dfs = pd.DataFrame(columns=['Meeting Date', 'Remarks'])
        dfs['Meeting Date'] = date
        dfs['Meeting Date'] = pd.to_datetime(dfs['Meeting Date'])
        dfs['Remarks'] = remark

        return dfs
    else:
        dfs = pd.DataFrame(columns=['Meeting Date', 'Remarks'])
        dfs['Meeting Date'] = td
        dfs['Remarks'] = ""
        return dfs
    
def get_dividend(link):
    url=requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    My_table = soup.find('table',{'class':'mctable1'})
    
    td = My_table.find_all('td')
    td = [(i.text) for i in td] #removing tag
    
    if len(td)>=6:
        announcement_date=[]
        effective_date=[]
        dividend_type=[]
        dividend=[]
        remarks=[]
        for i in range(0, len(td), 5):
            announcement_date.append(td[i])
            effective_date.append(td[i+1])
            dividend_type.append(td[i+2])
            dividend.append(td[i+3])
            remarks.append(td[i+4])

        dfs = pd.DataFrame(columns=['Announcement Date', 'Effective Date', 'Dividend Type', 'Dividend (%)', 'Remarks'])
        dfs['Announcement Date'] = announcement_date
        dfs['Effective Date'] = effective_date
        dfs['Announcement Date'] = pd.to_datetime(dfs['Announcement Date'])
        dfs['Dividend Type'] = dividend_type
        dfs['Dividend (%)'] = dividend
        dfs['Remarks'] = remarks

        return dfs
    else:
        dfs = pd.DataFrame(columns=['Announcement Date', 'Effective Date', 'Dividend Type', 'Dividend (%)', 'Remarks'])
        dfs['Announcement Date'] = td
        dfs['Effective Date'] = ""
        dfs['Dividend Type'] = ""
        dfs['Dividend (%)'] = ""
        dfs['Remarks'] = ""
        return dfs
    
def get_AGM_EGM(link):
    url=requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    My_table = soup.find('table',{'class':'mctable1'})
    
    td = My_table.find_all('td')
    td = [(i.text) for i in td] #removing tag
    
    if len(td)>=6:
        announcement_date=[]
        purpose=[]
        date=[]
        date_from=[]
        book_closure_to=[]
        remark=[]
        for i in range(0, len(td), 6):
            announcement_date.append(td[i])
            purpose.append(td[i+1])
            date.append(td[i+2])
            date_from.append(td[i+3])
            book_closure_to.append(td[i+4])
            remark.append(td[i+5])

        dfs = pd.DataFrame(columns=['Announcement Date', 'Purpose', 'Date', 'From', 'Book Closure To', 'Remark'])
        dfs['Announcement Date'] = announcement_date
        dfs['Announcement Date'] = pd.to_datetime(dfs['Announcement Date'])
        dfs['Purpose'] = purpose
        
        dfs['Date'] = date

        #dfs['Date'] = pd.to_datetime(dfs['Date'])
        
        dfs['From'] = date_from
        dfs['Book Closure To'] = book_closure_to
        dfs['Remark'] = remark

        return dfs
    
    else:
        dfs = pd.DataFrame(columns=['Announcement Date', 'Purpose', 'Date', 'From', 'Book Closure To', 'Remark'])
        dfs['Announcement Date'] = td
        dfs['Purpose'] = ""
        dfs['Date'] = ""
        dfs['From'] = ""
        dfs['Book Closure To'] = ""
        dfs['Remark'] = ""

        return dfs
    
def get_bonus(link):
    url=requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    My_table = soup.find('table',{'class':'mctable1 MT20'})

    td = My_table.find_all('td')
    td = [(i.text) for i in td] #removing tag
    
    if len(td)>=4:
        announcement_date=[]
        bonus_ratio=[]
        record_date=[]
        ex_bonus_date=[]

        for i in range(0, len(td), 4):
            announcement_date.append(td[i])
            bonus_ratio.append(td[i+1])
            record_date.append(td[i+2])
            ex_bonus_date.append(td[i+3])

        dfs = pd.DataFrame(columns=['Announcement Date', 'Bonus Ratio', 'Record Date', 'Ex-Bonus Date'])
        dfs['Announcement Date'] = announcement_date
        dfs['Announcement Date'] = pd.to_datetime(dfs['Announcement Date'])
        dfs['Bonus Ratio'] = bonus_ratio
        dfs['Record Date'] = record_date
        dfs['Ex-Bonus Date'] = ex_bonus_date

        return dfs
    else:        
        dfs = pd.DataFrame(columns=['Announcement Date', 'Bonus Ratio', 'Record Date', 'Ex-Bonus Date'])
        dfs['Announcement Date'] = td
        dfs['Bonus Ratio'] = ""
        dfs['Record Date'] = ""
        dfs['Ex-Bonus Date'] = ""
        return dfs
    
def get_split(link):
    url=requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    My_table = soup.find('table',{'class':'mctable1'})
      
    td = My_table.find_all('td')
    td = [(i.text) for i in td] #removing tag
      
    if(len(td)>=4):
        
        announcement_date=[]
        old_fv=[]
        new_fv=[]
        ex_split_date=[]

        for i in range(0, len(td), 4):
            announcement_date.append(td[i])
            old_fv.append(td[i+1])
            new_fv.append(td[i+2])
            ex_split_date.append(td[i+3])

        dfs = pd.DataFrame(columns=['Announcement Date', 'Old FV', 'New FV', 'Ex-Split Date'])
        dfs['Announcement Date'] = announcement_date
        dfs['Announcement Date'] = pd.to_datetime(dfs['Announcement Date'])
        dfs['Old FV'] = old_fv
        dfs['New FV'] = new_fv
        dfs['Ex-Split Date'] = ex_split_date

        return dfs
    
    else:
        dfs = pd.DataFrame(columns=['Announcement Date', 'Old FV', 'New FV', 'Ex-Split Date'])
        dfs['Announcement Date'] = td
        dfs['Old FV'] = ""
        dfs['New FV'] = ""
        dfs['Ex-Split Date'] = ""
        return dfs
    
def get_rights(link):
    url=requests.get(link).text
    soup = BeautifulSoup(url,'lxml')
    My_table = soup.find('table',{'class':'mctable1'})
    
    td = My_table.find_all('td')
    td = [(i.text) for i in td] #removing tag
    
    if(len(td)>=6):
        
        announcement_date=[]
        rights_ratio=[]
        face_value=[]
        premium=[]
        record_date=[]
        ex_rights_date=[]

        for i in range(0, len(td), 6):
            announcement_date.append(td[i])
            rights_ratio.append(td[i+1])
            face_value.append(td[i+2])
            premium.append(td[i+3])
            record_date.append(td[i+4])
            ex_rights_date.append(td[i+5])


        dfs = pd.DataFrame(columns=['Announcement Date', 'Rights Ratio', 'Face Value', 'Premium', 'Record Date', 'Ex-Rights Date'])
        dfs['Announcement Date'] = announcement_date
        dfs['Rights Ratio'] = rights_ratio
        
        dfs['Face Value'] = face_value
        dfs['Premium'] = premium
        dfs['Record Date'] = record_date
        dfs['Announcement Date'] = pd.to_datetime(dfs['Announcement Date'])
        dfs['Ex-Rights Date'] = ex_rights_date

        return dfs
    
    else:
        dfs = pd.DataFrame(columns=['Announcement Date', 'Rights Ratio', 'Face Value', 'Premium', 'Record Date', 'Ex-Rights Date'])
        dfs['Announcement Date']=td
        dfs['Rights Ratio'] = ""
        dfs['Face Value'] = ""
        dfs['Premium'] = ""
        dfs['Record Date'] = ""
        dfs['Ex-Rights Date'] = ""

        return dfs

