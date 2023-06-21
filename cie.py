import re

def marks(response):
    table= response.find('table', class_="uk-table cn-cie-table uk-table-responsive")
    for i, row in enumerate(table.find_all('tr')):
        if i==0:
            continue
        data=[el.text.strip() for el in row.find_all('td')]
        l=len(data)
        if l<9:
            for i in range(9-l):
                data.append('-')

        sample = {
            'cie1':data[0],
            'cie2':data[1],
            'cie3':data[2],
            'cie4':data[3],
            'quiz1':data[4],
            'quiz2':data[5],
            'quiz3':data[6],
            'final':data[7],
            'attendance':data[8]

        }
        return sample

def final_cie(response):
    try:
        return int(re.findall(r'\d+', (response.select("span.uk-label:nth-child(1)")[0]).text)[0])
    except:
        return 0