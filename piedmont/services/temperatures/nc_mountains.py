from piedmont.services.utils import cronos, rays_weather, nc_high_peaks

cronos_stations = [{"code": "FLET", "label": "South Asheville", "elevation": "2060ft"},
                   {"code": "KTNB", "label": "Boone", "elevation": "2980ft"},
                   {"code": "grandfathr", "label": "Grandfather Mtn",
                       "elevation": "5280ft"},
                   {"code": "MITC", "label": "Mt Mitchell #2", "elevation": "6200ft"},
                   {"code": "BEAR", "label": "Bearwallow Mtn", "elevation": "4200ft"}]

rays_weather_station_groups = [{"url": "http://booneweather.com/",
                                "stations": [{"code": 3, "label": "Valle Crucis", "elevation": "2670ft"}]},
                               {"url": "http://averyweather.com/",
                                "stations": [{"code": 5,
                                              "label": "Linville", "elevation": "3650ft"},
                                             {"code": 11,
                                              "label": "Seven Devils", "elevation": "3940ft"},
                                             {"code": 7,
                                              "label": "Sugar Mtn", "elevation": "5000ft"}]}]


def get_nc_mountain_temperatures():
    temperatures = []
    labels = []

    temperatures_with_labels = []

    for station in cronos_stations:
        data = cronos.get_temperature(
            station["code"], station["label"], station["elevation"])

        temperatures_with_labels.append({
            "label": data["label"],
            "temp": data["temp"]}
        )

    for station_group in rays_weather_station_groups:
        data = rays_weather.get_temperatures(
            station_group["url"], station_group["stations"])

        for station in data:
            temperatures_with_labels.append({
                "label": station["label"],
                "temp": station["temp"]}
            )

    mitchell_top = nc_high_peaks.get_mitchell_top_data()

    if mitchell_top["success"]:
        temperatures_with_labels.append({
            "label": mitchell_top["label"],
            "temp": mitchell_top["temp"]}
        )

    for item in temperatures_with_labels:
        temperatures.append(item['temp'])
        labels.append(item['label'])

    return temperatures, labels
