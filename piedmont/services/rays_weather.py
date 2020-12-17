import urllib
from bs4 import BeautifulSoup


def get_valle_crucis_station_data():
    url = 'http://booneweather.com/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    Map = str(soup.find('map', {"name": "cc"}))

    output = dict()
    output['label'] = 'Valle Crucis 2670ft'
    output['temp'] = 0.00
    output['success'] = False

    try:
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[3])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        output['temp'] = eval(Temp_3[0])
        output['success'] = True

    except:
        print("Valle Crucis missing")

    return output


def get_avery_station_data():
    url = 'http://averyweather.com/'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')
    Map = str(soup.find('map', {"name": "cc"}))
    output = []

    linville_output = dict()
    linville_output['label'] = 'Linville 3650ft'
    linville_output['temp'] = 0.00
    linville_output['success'] = False

    try:
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[5])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')

        linville_output['temp'] = eval(Temp_3[0])
        linville_output['success'] = True
        output.append(linville_output)

    except:
        print("Linville missing")

    seven_devils_output = dict()
    seven_devils_output['label'] = 'Seven Devils 3940ft'
    seven_devils_output['temp'] = 0.00
    seven_devils_output['success'] = False

    try:
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[11])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        seven_devils_output['temp'] = eval(Temp_3[0])
        seven_devils_output['success'] = True
        output.append(seven_devils_output)

    except:
        print("Seven Devils missing")

    sugar_mountain_output = dict()
    sugar_mountain_output['label'] = 'Sugar Mtn 5000ft'
    sugar_mountain_output['temp'] = 0.00
    sugar_mountain_output['success'] = False

    try:
        Area_1 = Map.split('<area')
        Area_2 = str(Area_1[7])
        Temp_1 = Area_2.split('Temp:&lt;/td&gt;&lt;td&gt;')
        Temp_2 = str(Temp_1[1])
        Temp_3 = Temp_2.split('°F')
        sugar_mountain_output['temp'] = eval(Temp_3[0])
        sugar_mountain_output['success'] = True
        output.append(sugar_mountain_output)

    except:
        print("Sugar Mountain missing")

    return output
