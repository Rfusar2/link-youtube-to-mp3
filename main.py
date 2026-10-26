from pytubefix import YouTube
from pytubefix.cli import on_progress
from json import loads
from os import makedirs

with open("config.json") as f:
    CONF = loads(f.read())

makedirs("FILES", exist_ok=True)

with open(CONF["file_links"]) as f:
    for r in f.readlines():
        try:
            r = r.strip()
            if r != "":
                url = r
                yt = YouTube(url, on_progress_callback = on_progress)
                print(yt.title)
                print("AVVIO")
                ys = yt.streams.get_audio_only()
                ys.download(output_path=CONF["folder_output"])
                print("FINE")
        except:
            ...
