import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {}
P['Authorization'] = 'CWA-B368A0F0-D84C-4945-A50C-7164383DEBCB'
r = requests.get(URL, params=P)
#print(type(r))
t = r.json()
print(t)