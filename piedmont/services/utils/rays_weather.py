import urllib
from bs4 import BeautifulSoup


def parse_temperature(map, station_code, station_label, station_elevation):
    output = dict()
    output['label'] = station_label + ' ' + station_elevation
    output['temp'] = 0.00
    output['success'] = False

    try:
        Area_1 = map.split('<area')
        Area_2 = str(Area_1[station_code])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        output['temp'] = eval(Temp_3[0])
        output['success'] = True

    except:
        print(station_label + " missing")

    return output


def get_temperatures(url, stations):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    map = str(soup.find('map', {"name": "cc"}))

    output = []

    for station in stations:
        station_output = parse_temperature(
            map, station['code'], station['label'], station['elevation'])
        output.append(station_output)

    return output
