import requests

#IMG = 'http://www.shu.edu.tw/BBS/Ann_Spotlight/28311/20210503%E6%A0%A1%E9%96%802.jpg'
IMG = 'https://images.chinatimes.com/newsphoto/2021-05-06/656/20210506001660.jpg'
URL = 'http://notify-api.line.me/api/notify'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer p0cCIzsWQsWHzI6EtLHIEvQCtJfiHMIjdFyfiwNje4d '
P['message'] = '群組網路圖片'
F['imageFile'] = requests.get(IMG).content
response = requests.post(URL, headers=H, params=P, files=F)

print(response.status_code)
print(response.text)