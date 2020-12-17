from piedmont.services.utils import cronos

cronos_stations = [{"code": "KCHO", "label": "Charlottesville", "elevation": "641ft"},
                   {"code": "KLYH", "label": "Lynchburg", "elevation": "938ft"},
                   {"code": "KROA", "label": "Roanoke", "elevation": "1175ft"},
                   {"code": "KW13", "label": "Waynesboro", "elevation": "1436ft"},
                   {"code": "KBCB", "label": "Blacksburg", "elevation": "2132ft"},
                   {"code": "KHLX", "label": "Hillsville", "elevation": "2693ft"}, ]


def get_va_temperatures():
    temperatures_with_labels = []

    for station in cronos_stations:
        data = cronos.get_temperature(
            station["code"], station["label"], station["elevation"])

        temperatures_with_labels.append({
            "label": data["label"],
            "temp": data["temp"]}
        )

    return temperatures_with_labels
