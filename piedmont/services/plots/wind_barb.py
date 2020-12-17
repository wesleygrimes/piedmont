import numpy as np
import math
import urllib.request
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from matplotlib import cm
from bs4 import BeautifulSoup
from datetime import datetime


def get_grandfather_wind_barb():

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
