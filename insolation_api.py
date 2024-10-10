import requests


class InsolationAPI:
    def __init__(self):
        self.url = "https://power.larc.nasa.gov/api/temporal/monthly/point"

    def get_insolation(self, latitude, longitude, year):
        params = {
            "parameters": "ALLSKY_SFC_SW_DWN",
            "community": "RE",   #'units': 'kW-hr/m^2/day'
            "longitude": longitude,
            "latitude": latitude,
            "format": "json",
            "start": year, 
            "end": year
        }
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            insolation_data = response.json()['properties']['parameter']['ALLSKY_SFC_SW_DWN']
            insolation_by_month_list = list(insolation_data.values())
            return insolation_by_month_list
        except requests.RequestException:
            print("Помилка під час запиту.")
            return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]