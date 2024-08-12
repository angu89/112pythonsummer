import yt_dlp

PLAYLIST_URL = 'https://youtube.com/playlist?list=PLmh66cIsVZUsdWj-Mcb3MJnC7tgfqCOgy&si=kLkOBoHukybvF-Fc'

DIR = 'C:\\Youtube'


ydl_opts = {
    'format': 'worst',

    'outtmpl': f'{DIR}/%(playlist_title)s.%(title)s.%(ext)s',
}


try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        ydl.download([PLAYLIST_URL])
    print(f"Playlist downloaded successfully to {DIR}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")        

    

