import os
import youtube_dl
from tqdm import tqdm
from youtubesearchpython import SearchVideos
from . import meta, DATASET_ROOT, get_id_str

filtered_idx = []

image_files = os.listdir(os.path.join(DATASET_ROOT, "raw", "image"))
for file_name in image_files:
    split_arr = file_name.split(".jpg")
    if len(split_arr) == 2:
        filtered_idx += [int(split_arr[0])]

target_length = len(filtered_idx)
    

def get_url(m):
    query = "{} {}".format(m["song_name"], m["album_name"])
    search = SearchVideos(query, offset = 1, mode = "dict", max_results = 1)
    if len(search.result()["search_result"]) > 0:
        url = search.result()["search_result"][0]["link"]
        return url
    else:
        return None

def download(idx, m):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192'
        }],
        'postprocessor_args': [
            '-ar', '16000'
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,
        'quiet': True,
        'outtmpl': os.path.join(DATASET_ROOT, "raw", "sound", "{}.%(ext)s".format(get_id_str(idx)))
    }

    url = get_url(m)
    if url != None:
        # print("{}% [{}/{}] {}: {}".format((idx/target_length)*100, idx, target_length, m["song_name"], url))

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        print("no urls fetched")


if __name__ == "__main__":
    for idx in tqdm(filtered_idx):
        m = meta[idx]
        try:
            download(idx, m)
        except KeyboardInterrupt:
            break
        except:
            pass
