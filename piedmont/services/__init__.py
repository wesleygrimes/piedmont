import piedmont.services.temperatures as temperature_service
import piedmont.services.plots as plot_service


def get_nc_mountain_temperature_plot():
    temps, labels = temperature_service.get_nc_mountain_temperatures()

    temperature_plot = plot_service.get_temperature_plot("Mountains, NC\nVertical Temperature Profile",
                                                         "output/wncbarplot.png", temps, labels)

    return temperature_plot


def get_nc_piedmont_temperature_plot():
    temps, labels = temperature_service.get_nc_piedmont_temperatures()

    temperature_plot = plot_service.get_temperature_plot("Western Piedmont, NC\nVertical Temperature Profile",
                                                         "output/piedmontbarplot.png", temps, labels)

    return temperature_plot


def get_va_temperature_plot():
    temps, labels = temperature_service.get_va_temperatures()

    temperature_plot = plot_service.get_temperature_plot("Western Virginia\nVertical Temperature Profile",
                                                         "output/vabarplot.png", temps, labels)

    return temperature_plot


def get_grandfather_wind_barb():
    wind_barb = plot_service.get_grandfather_wind_barb()

    return wind_barb
