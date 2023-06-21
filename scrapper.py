import requests
from bs4 import BeautifulSoup
from attendance  import *
from start import *
from cie import *

def SISLogin(usn,date,month,year):
    s=requests.Session()
    r = s.post('https://parents.msrit.edu/index.php', data=payset(usn,date,month,year))
    return (s,r)

def get_data(s,r):

    def SISattendance(s):
        data={}
        att = s.get("https://parents.msrit.edu/"+ i[-1]) #attendance scraping
        soup = BeautifulSoup(att.content, "html.parser")
        data['teacher']=teacher(soup)
        data['attendance_count']=status(soup)
        data['present']=present(soup)
        data['absent']=absent(soup)
        return data


    def SISinternals(s):
        data={}
        att2 = s.get("https://parents.msrit.edu/"+ i[-2]) #cie scraping
        soup2 = BeautifulSoup(att2.content ,"html.parser")
        data['internal_marks']=marks(soup2)
        data['final_cie']=final_cie(soup2)
        return data

    data_list=[]
    soup = BeautifulSoup(r.content, 'html.parser')
    image = soup.find('img', attrs={'class': "uk-preserve-width uk-border"})['src']
    table = soup.find('table', attrs={'class': "dash_od_row uk-table uk-table-striped uk-table-hover cn-pay-table uk-table-middle uk-table-responsive"})
    rows = table.find_all('tr')
    for row in rows[1:]:
        cols = row.find_all(['td','th'])
        data = [col.text.strip() for col in cols]
        data = [data[0],data[1],data[4]]
        data2 =[col.a.get('href') for col in cols if col.a]
        links =[data2[-1],data2[-2]] #cie and attendance links/endpoints
        data.extend(links)
        data_list.append(data)

    main_data={}
    for i in data_list:
        data={}
        data['attendance_status']=i[-3]
        data['subject_name']=i[-4]
        data.update(SISattendance(s))
        data.update(SISinternals(s))
        main_data[i[0]] = data


    return main_data