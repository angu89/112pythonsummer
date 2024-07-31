#LINENOTIFY傳送本機圖片
import requests

URL = 'http://notify-api.line.me/api/notify
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer WB8Z17Gy0hSv4HpqNGJZmrgsLhibpqU6rKGz0IhI8Fh'
P['message'] = '本機圖片'
F['imageFile'] = open(r'C:\Users\m303\Pictures\harris.jpg', 'rb')#圖檔絕對路徑
requests.post(URL, headers=H, params=P, files=F)
