import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-B368A0F0-D84C-4945-A50C-7164383DEBCB'
r = requests.get(URL, params=P)
t = r.json()
station_id = 30
print('觀測地點: ', t['records']['Station'][station_id]['StationName'])
print('觀測時間: ', t['records']['Station'][station_id]['ObsTime']['DateTime'])
print('觀測溫度: ', t['records']['Station'][station_id]['WeatherElement']['AirTemperature'])
print('觀測濕度: ', t['records']['Station'][station_id]['WeatherElement']['RelativeHumidity'])
print('觀測天氣: ', t['records']['Station'][station_id]['WeatherElement']['Weather'])
