import urllib
from bs4 import BeautifulSoup


def get_mitchell_top_data():
    url = 'https://nchighpeaks.org/davis/index.html'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

    output = dict()
    output['label'] = 'Mt Mitchell #1 6600ft'
    output['temp'] = 0.00
    output['success'] = False

    try:
        Table = str(soup.find('table').find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[0])
        Temp_2 = Temp_1.split('<td class="stats_data">')
        Temp_3 = str(Temp_2[1])
        Temp_4 = Temp_3.split('°F')
        Temp_5 = str(Temp_4[0])
        Temp = eval(Temp_5)
        output['temp'] = eval(Temp)
        output['success'] = True

    except:
        print("Mitchell Top missing")

    return output
