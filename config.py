import yt_dlp as youtube_dl
from youtube_dl import YoutubeDL
import datetime
YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

url = "https://www.youtube.com/watch?v=RaarRogvesU&t=1245s"
# url = ' '.join(url)
with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
                info = ydl.extract_info(url, download=True)
        except:
                info = ydl.extract_info(f"ytsearch:{url}",
                                        download=False)['entries'][0]
                


URL = info['formats'][0]['url']
name = info['title']
time = str(datetime.timedelta(seconds=info['duration']))


print(URL, name, time)