from piedmont.services.temperatures import nc_mountains, va, nc_piedmont
from piedmont.services.plots import temperature_plot, wind_barb


def get_nc_mountain_temperature_plot_base64():
    temps, labels = nc_mountains.get_nc_mountain_temperatures()

    plot_base64 = temperature_plot.get_temperature_plot_base64("Mountains, NC\nVertical Temperature Profile",
                                                               "output/wncbarplot.png", temps, labels)

    return plot_base64


def get_nc_piedmont_temperature_plot_base64():
    temps, labels = nc_piedmont.get_nc_piedmont_temperatures()

    plot_base64 = temperature_plot.get_temperature_plot_base64("Western Piedmont, NC\nVertical Temperature Profile",
                                                               "output/piedmontbarplot.png", temps, labels)

    return plot_base64


def get_va_temperature_plot_base_64():
    temps, labels = va.get_va_temperatures()

    plot_base64 = temperature_plot.get_temperature_plot_base64("Western Virginia\nVertical Temperature Profile",
                                                               "output/vabarplot.png", temps, labels)

    return plot_base64


def get_grandfather_wind_barb():
    wind_barb = temperature_plot.get_grandfather_wind_barb()

    return wind_barb
