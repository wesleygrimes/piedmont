import urllib
from bs4 import BeautifulSoup


def get_south_asheville_station_data():
    url = 'https://climate.ncsu.edu/cronos/?station=FLET'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    output = dict()
    output['label'] = 'South Asheville 2060ft'
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
        print("FLET missing")

    return output


def get_boone_station_data():
    url = 'https://climate.ncsu.edu/cronos/?station=ktnb'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    output = dict()
    output['label'] = 'Boone 2980ft'
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
        print("KTNB missing")

    return output


def get_grandfather_station_data():
    url = 'https://climate.ncsu.edu/cronos/?station=grandfathr'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    output = dict()
    output['label'] = 'Grandfather Mtn 5280ft'
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
        print("Grandfathr missing")

    return output


def get_mitchell_station_data():
    url = 'https://climate.ncsu.edu/cronos/?station=MITC'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    output = dict()
    output['label'] = 'Mt Mitchell #2 6200ft'
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
        print("MITC missing")

    return output


def get_bearwallow_mountain_station_data():
    url = 'https://climate.ncsu.edu/cronos/?station=BEAR'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    output = dict()
    output['label'] = 'Bearwallow Mtn 4200ft'
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
        print("BEAR missing")

    return output
