import piedmont.services as services


def get_nc_mountain_temperature_plot():
    temperatures, labels = services.temperatures.get_nc_mountain_temperatures()

    temperature_plot = services.plots.get_temperature_plot("Mountains, NC\nVertical Temperature Profile",
                                                           "output/wncbarplot.png", temperatures, labels)

    return temperature_plot


def get_nc_piedmont_temperature_plot():
    temperatures, labels = services.temperatures.get_nc_mountain_temperatures()

    temperature_plot = services.plots.get_temperature_plot("Western Piedmont, NC\nVertical Temperature Profile",
                                                           "output/piedmontbarplot.png", temperatures, labels)

    return temperature_plot


def get_va_piedmont_temperature_plot():
    temperatures, labels = services.temperatures.get_va_piedmont_temperatures()

    temperature_plot = services.plots.get_temperature_plot("Western Piedmont, NC\nVertical Temperature Profile",
                                                           "output/piedmontbarplot.png", temperatures, labels)

    return temperature_plot


def get_grandfather_wind_barb():
    return {}
