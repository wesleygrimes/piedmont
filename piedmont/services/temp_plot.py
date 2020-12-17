import piedmont.services.cronos as cronos
import piedmont.services.rays_weather as rays_weather
import piedmont.services.nc_high_peaks as nc_high_peaks

import numpy as np
import math
import shapefile
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from matplotlib import cm
from bs4 import BeautifulSoup
from datetime import datetime


def wncbar():
    barnames = []
    temperatures = []

    south_asheville = cronos.get_south_asheville_station_data()

    if south_asheville['success']:
        barnames.append(south_asheville['label'])
        temperatures.append(south_asheville['temp'])

    boone = cronos.get_boone_station_data()

    if boone['success']:
        barnames.append(boone['label'])
        temperatures.append(boone['temp'])

    grandfather = cronos.get_grandfather_station_data()

    if grandfather['success']:
        barnames.append(grandfather['label'])
        temperatures.append(grandfather['temp'])

    mitchell = cronos.get_mitchell_station_data()

    if mitchell['success']:
        barnames.append(mitchell['label'])
        temperatures.append(mitchell['temp'])

    bearwallow_mountain = cronos.get_bearwallow_mountain_station_data()

    if bearwallow_mountain['success']:
        barnames.append(bearwallow_mountain['label'])
        temperatures.append(bearwallow_mountain['temp'])

    valle_crucis = rays_weather.get_valle_crucis_station_data()

    if valle_crucis['success']:
        barnames.append(valle_crucis['label'])
        temperatures.append(valle_crucis['temp'])

    avery = rays_weather.get_avery_station_data()

    for data in avery:
        barnames.append(data['label'])
        temperatures.append(data['temp'])

    mitchell_top = nc_high_peaks.get_mitchell_top_data()

    if mitchell_top['success']:
        barnames.append(mitchell_top['label'])
        temperatures.append(mitchell_top['temp'])

    print(temperatures)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')

    # data and bar names
    height = temperatures
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    if len(height) > 0:
        maximum = max(height)+3
        minimum = min(height)-3
        font = {'size': 16, 'color': 'white'}
        font2 = {'size': 22, 'color': 'white'}

    # color
        color_1 = np.array(height)
        color_2 = cm.cool(1-(color_1 / float(max(color_1))))
        ax.xaxis.label.set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')

    # horizontal bars
        plt.barh(y_pos, height, color=color_2)

    # y-axis names
        plt.yticks(y_pos, bars, **font)

    # x-axis
        plt.xlim(minimum, maximum)

    # x label
        plt.xlabel('Temperature (°F)', **font)

        for i, v in enumerate(height):
            plt.text(v, i-0.1, str(v), color='white', fontsize='13')
        plt.title('Mountains, NC\nVertical Temperature Profile', **font2)

        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        #plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
        plt.text(-0.27, -0.12, "Source: NCSCO", color='white', size=16,
                 horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        plt.text(-0.27, 1.05, "Valid: " + current_time, color='white', size=16,
                 horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        plt.figtext(0.5, -0.2, "AppalachianWX.com", color='white',
                    size=10, horizontalalignment='center', transform=ax.transAxes)
        # show/save graphic
        plt.savefig("output/wncbarplot.png", bbox_inches='tight',
                    facecolor=fig.get_facecolor())
        # plt.show()
    elif len(height) == 0:
        fig = plt.figure()
        fig.patch.set_facecolor('grey')
        ax = plt.axes()
        ax.set_facecolor('grey')
        plt.text(0.5, 0.5, "All Stations Down", color='white', size=22,
                 horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        plt.savefig("output/wncbarplot.png", bbox_inches='tight',
                    facecolor=fig.get_facecolor())


wncbar()


def windbarb():

    url = 'https://climate.ncsu.edu/cronos/?station=grandfathr'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

    try:

        Table = str(
            soup.find('table', {"class": "CurrentConditions"}).find_all('tr'))
        Tr = Table.split(',')

        Wind_1 = str(Tr[6])
        Wind_2 = Wind_1.split('<')
        Wind_3 = str(Wind_2[9])
        Wind_4 = Wind_3.split('>')
        Wind_5 = str(Wind_4[1])
        Wind_Sum = Wind_5[1:]
        print(Wind_Sum)
        if Wind_Sum == 'Calm ':
            print("in calm")
            u = 1
            v = 1

            Time_1 = str(Tr[3])
            Time_2 = Time_1.split('<')
            Time_3 = str(Time_2[0])
            Time_4 = Time_3.split('@ ')
            Time_5 = str(Time_4[1])
            Time_6 = Time_5.split(' (')
            Time_7 = str(Time_6[0])
            print(Time_7)

            fig = plt.figure()
            fig.patch.set_facecolor('grey')
            ax = plt.axes()
            ax.set_facecolor('grey')
            ax.axis('off')
            ax.barbs(0, 0, u, v, length=15, pivot='middle', color='white')
            plt.xlim(-0.73, 0.8)
            plt.ylim(-0.8, 0.8)
            plt.text(0, -0.6, Wind_Sum, ha='center', size=15, color='white')
            plt.text(0, -0.75, "Valid: " + Time_7,
                     ha='center', size=15, color='white')
            plt.text(0, -0.85, "Source: NCSCO",
                     ha='center', size=12, color='white')
            plt.text(0, 0.70, 'Current Winds on Grandfather Mountain',
                     color='white', size=19, weight='bold', ha='center')

            plt.savefig("output/barbplot.png", bbox_inches='tight',
                        facecolor=fig.get_facecolor())

        else:
            print("in not calm")
            Dir_1 = Wind_5.split('(')
            Dir_2 = str(Dir_1[1])
            Dir_3 = Dir_2.split('°')
            Dir_4 = eval(Dir_3[0])
            print(Dir_4)
            Speed_1 = Wind_5.split('at ')
            Speed_2 = str(Speed_1[1])
            Speed_3 = Speed_2.split(' mph')
            Speed_4 = eval(Speed_3[0])

            Time_1 = str(Tr[3])
            Time_2 = Time_1.split('<')
            Time_3 = str(Time_2[0])
            Time_4 = Time_3.split('@ ')
            Time_5 = str(Time_4[1])
            Time_6 = Time_5.split(' (')
            Time_7 = str(Time_6[0])
            print(Time_7)

            if Dir_4 < 90:
                offset = 90 - Dir_4
                deg_direction = Dir_4 + 90 + 2*offset
            else:
                offset = 90 - Dir_4

            deg_direction = Dir_4 + 90 + 2*offset
            rad_direction = math.radians(deg_direction)
            speed = Speed_4
            u = speed*math.cos(rad_direction)
            v = speed*math.sin(rad_direction)

            fig = plt.figure()
            fig.patch.set_facecolor('grey')
            ax = plt.axes()
            ax.set_facecolor('grey')
            ax.axis('off')
            ax.barbs(0, 0, u, v, length=15, pivot='middle', color='white')
            plt.xlim(-0.73, 0.8)
            plt.ylim(-0.8, 0.8)
            plt.text(0, -0.6, Wind_Sum, ha='center', size=15, color='white')
            plt.text(0, -0.75, "Valid: " + Time_7,
                     ha='center', size=15, color='white')
            plt.text(0, -0.87, "Source: NCSCO",
                     ha='center', size=12, color='white')
            plt.text(0, 0.70, 'Current Winds on Grandfather Mountain',
                     color='white', size=19, weight='bold', ha='center')

            plt.savefig("output/barbplot.png", bbox_inches='tight',
                        facecolor=fig.get_facecolor())

    except:
        print("Grandfathr missing")


windbarb()


def piedmontbar():

    names = ('Charlotte 748ft', 'Greensboro 792ft', 'Statesville 965ft', 'Rutherfordton 1078ft',
             'Hickory 1189ft', 'Mount Airy 1247ft', 'Morganton 1270ft', 'North Wilkesboro 1301ft')

    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KCLT'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KCLT missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=NCAT'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("NCAT missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KSVH'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KSVH missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KFQD'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KFQD missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KHKY'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KHKY missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KMWK'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KMWK missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KMRN'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KMRN missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KUKF'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KUKF missing")
        i = i + 1

    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')

    # data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    maximum = max(height)+3
    minimum = min(height)-3
    font = {'size': 16, 'color': 'white'}
    font2 = {'size': 22, 'color': 'white'}

    # color
    color_1 = np.array(height)
    color_2 = cm.cool(1-(color_1 / float(max(color_1))))
    ax.xaxis.label.set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # horizontal bars
    plt.barh(y_pos, height, color=color_2)

    # y-axis names
    plt.yticks(y_pos, bars, **font)

    # x-axis
    plt.xlim(minimum, maximum)

    # x label
    plt.xlabel('Temperature (°F)', **font)

    for i, v in enumerate(height):
        plt.text(v, i-0.1, str(v), color='white', fontsize='13')
    plt.title('Western Piedmont, NC\nVertical Temperature Profile', **font2)

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    #plt.text(0.87,0.94,current_time,color='white',size=18,horizontalalignment='center',verticalalignment='center',transform = ax.transAxes)
    plt.text(-0.27, -0.12, "Source: NCSCO", color='white', size=16,
             horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    plt.text(-0.27, 1.05, "Valid: " + current_time, color='white', size=16,
             horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    plt.figtext(0.5, -0.2, "AppalachianWX.com", color='white',
                size=10, horizontalalignment='center', transform=ax.transAxes)
    # show/save graphic
    plt.savefig("output/piedmontbarplot.png", bbox_inches='tight',
                facecolor=fig.get_facecolor())
    # plt.show()


piedmontbar()


def vabar():

    names = ('Charlottesville 641ft', 'Lynchburg 938ft', 'Roanoke 1175ft',
             'Waynesboro 1436ft', 'Blacksburg 2132ft', 'Hillsville 2693ft')

    barnames = []
    Temperature = []
    Elevation = []
    i = 0

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KCHO'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KCHO missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KLYH'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KLYH missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KROA'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KROA missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KW13'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KW13 missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KBCB'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KBCB missing")
        i = i + 1

    # CRONOS
    url = 'https://climate.ncsu.edu/cronos/?station=KHLX'
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, features='html.parser')

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
        Temp = eval(Temp_8)
        Temperature.append(Temp)
        barnames.append(names[i])
        i = i + 1

    except:
        print("KHLX missing")
        i = i + 1

    print(Temperature)

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')

    # data and bar names
    height = Temperature
    bars = barnames
    y_pos = np.arange(len(bars))

    #max/mins & fonts
    maximum = max(height)+3
    minimum = min(height)-3
    font = {'size': 16, 'color': 'white'}
    font2 = {'size': 22, 'color': 'white'}

    # color
    color_1 = np.array(height)
    color_2 = cm.cool(1-(color_1 / float(max(color_1))))
    ax.xaxis.label.set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # horizontal bars
    plt.barh(y_pos, height, color=color_2)

    # y-axis names
    plt.yticks(y_pos, bars, **font)

    # x-axis
    plt.xlim(minimum, maximum)

    # x label
    plt.xlabel('Temperature (°F)', **font)

    for i, v in enumerate(height):
        plt.text(v, i-0.1, str(v), color='white', fontsize='13')
    plt.title('Western Virginia\nVertical Temperature Profile', **font2)

    now = datetime.now()
    current_time = now.strftime("%I:%M %p")
    plt.text(-0.27, 1.05, "Valid: " + current_time, color='white', size=16,
             horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    plt.text(-0.27, -0.12, "Source: NCSCO", color='white', size=16,
             horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
    plt.figtext(0.5, -0.2, "AppalachianWX.com", color='white',
                size=10, horizontalalignment='center', transform=ax.transAxes)
    # show/save graphic
    plt.savefig("output/vabarplot.png", bbox_inches='tight',
                facecolor=fig.get_facecolor())
    # plt.show()


vabar()
