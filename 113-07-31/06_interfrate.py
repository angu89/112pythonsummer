import requests
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# LINE Notify Token
TOKEN = 'Bearer p0cCIzsWQsWHzI6EtLHIEvQCtJfiHMIjdFyfiwNje4d'
URL = 'https://notify-api.line.me/api/notify'

# 送出通知的函式
def send_notification():
    choice = choice_var.get()
    headers = {'Authorization': TOKEN}
    payload = {'message': message_var.get()}
    
    if choice == 'Line Sticker':
        sticker_package_id = sticker_package_id_var.get()
        sticker_id = sticker_id_var.get()
        if not sticker_package_id or not sticker_id:
            messagebox.showwarning("Input Error", "Please provide sticker package ID and sticker ID.")
            return
        payload['stickerPackageId'] = sticker_package_id
        payload['stickerId'] = sticker_id
        response = requests.post(URL, headers=headers, data=payload)
    
    elif choice == 'Local Image File':
        file_path = file_path_var.get()
        if not file_path:
            messagebox.showwarning("Input Error", "Please provide a file path.")
            return
        files = {'imageFile': open(file_path, 'rb')}
        response = requests.post(URL, headers=headers, data=payload, files=files)
        files['imageFile'].close()
    
    elif choice == 'Web Image File':
        img_url = img_url_var.get()
        if not img_url:
            messagebox.showwarning("Input Error", "Please provide an image URL.")
            return
        img_response = requests.get(img_url)
        if img_response.status_code == 200:
            files = {'imageFile': ('image.jpg', img_response.content, 'image/jpeg')}
            response = requests.post(URL, headers=headers, data=payload, files=files)
        else:
            messagebox.showerror("Download Error", "Failed to download the image.")
            return
    
    else:
        messagebox.showwarning("Selection Error", "Please select an option.")
        return

    # 顯示結果
    if response.status_code == 200:
        messagebox.showinfo("Success", "Notification sent successfully!")
    else:
        messagebox.showerror("Error", f"Failed to send notification: {response.text}")

# 建立 GUI 介面
root = tk.Tk()
root.title("LINE Notify GUI")

ttk.Label(root, text="Select what to send:").grid(column=0, row=0, padx=10, pady=5)

choice_var = tk.StringVar()
choices = ['Line Sticker', 'Local Image File', 'Web Image File']
choice_menu = ttk.Combobox(root, textvariable=choice_var, values=choices)
choice_menu.grid(column=1, row=0, padx=10, pady=5)

message_label = ttk.Label(root, text="Message:")
message_label.grid(column=0, row=1, padx=10, pady=5)
message_var = tk.StringVar()
message_entry = ttk.Entry(root, textvariable=message_var)
message_entry.grid(column=1, row=1, padx=10, pady=5)

sticker_package_id_label = ttk.Label(root, text="Sticker Package ID:")
sticker_package_id_label.grid(column=0, row=2, padx=10, pady=5)
sticker_package_id_var = tk.StringVar()
sticker_package_id_entry = ttk.Entry(root, textvariable=sticker_package_id_var)
sticker_package_id_entry.grid(column=1, row=2, padx=10, pady=5)

sticker_id_label = ttk.Label(root, text="Sticker ID:")
sticker_id_label.grid(column=0, row=3, padx=10, pady=5)
sticker_id_var = tk.StringVar()
sticker_id_entry = ttk.Entry(root, textvariable=sticker_id_var)
sticker_id_entry.grid(column=1, row=3, padx=10, pady=5)

file_path_label = ttk.Label(root, text="File Path:")
file_path_label.grid(column=0, row=4, padx=10, pady=5)
file_path_var = tk.StringVar()
file_path_entry = ttk.Entry(root, textvariable=file_path_var)
file_path_entry.grid(column=1, row=4, padx=10, pady=5)
file_path_button = ttk.Button(root, text="Browse", command=lambda: file_path_var.set(filedialog.askopenfilename()))
file_path_button.grid(column=2, row=4, padx=10, pady=5)

img_url_label = ttk.Label(root, text="Image URL:")
img_url_label.grid(column=0, row=5, padx=10, pady=5)
img_url_var = tk.StringVar()
img_url_entry = ttk.Entry(root, textvariable=img_url_var)
img_url_entry.grid(column=1, row=5, padx=10, pady=5)

send_button = ttk.Button(root, text="Send", command=send_notification)
send_button.grid(column=0, row=6, columnspan=3, padx=10, pady=10)

root.mainloop()