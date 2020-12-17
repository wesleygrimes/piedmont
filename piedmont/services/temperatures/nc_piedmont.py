from piedmont.services.utils import cronos

cronos_stations = [{"code": "KCLT", "label": "Charlotte", "elevation": "748ft"},
                   {"code": "NCAT", "label": "Greensboro", "elevation": "792ft"},
                   {"code": "KSVH", "label": "Statesville", "elevation": "965ft"},
                   {"code": "KFQD", "label": "Rutherfordton", "elevation": "1078ft"},
                   {"code": "KHKY", "label": "Hickory", "elevation": "1189ft"},
                   {"code": "KMWK", "label": "Mount Airy", "elevation": "1247ft"},
                   {"code": "KMRN", "label": "Morganton", "elevation": "1270ft"},
                   {"code": "KUKF", "label": "North Wilkesboro", "elevation": "1301ft"}, ]


def get_nc_piedmont_temperatures():
    temperatures_with_labels = []

    for station in cronos_stations:
        data = cronos.get_temperature(
            station["code"], station["label"], station["elevation"])

        temperatures_with_labels.append({
            "label": data["label"],
            "temp": data["temp"]}
        )

    return temperatures_with_labels
