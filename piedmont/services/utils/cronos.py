import urllib
from bs4 import BeautifulSoup


def get_temperature(station_code, station_label, station_elevation):
    url = 'https://climate.ncsu.edu/cronos/?station=' + station_code
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    output = dict()
    output['label'] = station_label + " " + station_elevation
    output['temp'] = 0.00
    output['success'] = False

    try:

        Table = str(
            soup.find('table', {"class": "CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Temp_1 = str(Tr[4])
        Temp_2 = Temp_1.split('<')
        Temp_3 = str(Temp_2[9])
        Temp_4 = Temp_3.split('>')
        Temp_5 = str(Temp_4[1])
        Temp_6 = Temp_5.split('°')
        Temp_7 = str(Temp_6[0])
        Temp_8 = Temp_7.strip(' ')
        output['temp'] = eval(Temp_8)
        output['success'] = True

    except:
        print(station_code + " missing")

    return output
