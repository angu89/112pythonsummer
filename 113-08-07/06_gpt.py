import requests
import tkinter as tk
from tkinter import ttk

# 設定 API 的 URL 和授權碼
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0003-001'
P = {'Authorization': 'CWA-B368A0F0-D84C-4945-A50C-7164383DEBCB'}

# 發送 GET 請求取得資料
r = requests.get(URL, params=P)
t = r.json()

# 確認 API 請求是否成功
if r.status_code == 200 and 'records' in t and 'location' in t['records']:
    stations = t['records']['location']
else:
    stations = []

# 建立 Tkinter 視窗
root = tk.Tk()
root.title("氣象觀測資料查詢")

# 下拉式選單變數
selected_station = tk.StringVar()

# 建立下拉式選單
station_names = [station['locationName'] for station in stations]
station_dropdown = ttk.Combobox(root, textvariable=selected_station)
station_dropdown['values'] = station_names
station_dropdown.grid(column=0, row=0, padx=10, pady=10)

# 顯示結果的標籤
result_label = tk.Label(root, text="", justify="left")
result_label.grid(column=0, row=1, padx=10, pady=10)

# 查詢並顯示資料的函數
def show_weather_data(*args):
    location = selected_station.get()
    for station in stations:
        if station['locationName'] == location:
            result = f"觀測地點: {station['locationName']}\n"
            result += f"觀測時間: {station['time']['obsTime']}\n"
            elements = station['weatherElement']
            for element in elements:
                if element['elementName'] == 'TEMP':
                    result += f"觀測溫度: {element['elementValue']} °C\n"
                if element['elementName'] == 'HUMD':
                    result += f"觀測濕度: {float(element['elementValue']) * 100:.1f}%\n"
                if element['elementName'] == 'WDSD':
                    result += f"風速: {element['elementValue']} m/s\n"
                if element['elementName'] == 'H_24R':
                    result += f"24小時累積降雨量: {element['elementValue']} mm\n"
                if element['elementName'] == 'Weather':
                    result += f"觀測天氣: {element['elementValue']}\n"
            result_label.config(text=result)
            break

# 綁定選擇事件
selected_station.trace("w", show_weather_data)

# 啟動 Tkinter 主循環
root.mainloop()
