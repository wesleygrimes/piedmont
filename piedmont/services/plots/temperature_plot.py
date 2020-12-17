import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import io
import base64

from matplotlib.patches import PathPatch
from matplotlib.collections import LineCollection
from matplotlib import cm
from datetime import datetime


def get_temperature_plot_base64(title, output_file, temperatures, labels):
    matplotlib.use('Agg')

    img = io.BytesIO()

    fig = plt.figure()
    fig.patch.set_facecolor('grey')
    ax = plt.axes()
    ax.set_facecolor('grey')

    # data and bar names
    height = temperatures
    bars = labels
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
        plt.title(title, **font2)

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
        #plt.savefig(output_file, bbox_inches='tight', facecolor=fig.get_facecolor())

        plt.savefig(img, bbox_inches='tight',
                    facecolor=fig.get_facecolor(), format="png")

        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode()

        return plot_url

    elif len(height) == 0:
        fig = plt.figure()
        fig.patch.set_facecolor('grey')
        ax = plt.axes()
        ax.set_facecolor('grey')
        plt.text(0.5, 0.5, "All Stations Down", color='white', size=22,
                 horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)

        plt.savefig(img, bbox_inches='tight',
                    facecolor=fig.get_facecolor(), format="png")

        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode()

        return plot_url
