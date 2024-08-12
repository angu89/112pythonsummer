import yt_dlp

URLs = [
    'https://www.youtube.com/watch?v=YQ-qToZUybM',
    'https://www.youtube.com/watch?v=4NRXx6U8ABQ',
    'https://www.youtube.com/watch?v=1fUEMeA5cF8',
    ]

DIR = 'C:\\Youtube'

for URL in URLs:

    ydl_opts = {
        'format': 'worst',

        'outtmpl': f'{DIR}/%(title)s.%(ext)s',
    }


    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info_dict = ydl.extract_info(URL, download=True)


            video_id = info_dict.get("id", None)


            video_title = info_dict.get("title", None)


            downloaded_format_id = info_dict.get("format_id", None)

        if video_id and downloaded_format_id:
            print(f"Video '{video_title}' downloaded successfully with the lowest resolution!")
            print(f"Video ID: {video_id}")
            print(f"Downloaded format itag: {downloaded_format_id}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")        

        

