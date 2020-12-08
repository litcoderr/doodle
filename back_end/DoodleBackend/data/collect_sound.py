from youtubesearchpython import SearchVideos
from . import meta

START_INDEX = 0
END_INDEX = 10 # TODO Change to songs that consist of image

def get_url(m):
    query = "{} {}".format(m["song_name"], m["album_name"])
    search = SearchVideos(query, offset = 1, mode = "dict", max_results = 1)
    if len(search.result()["search_result"]) > 0:
        url = search.result()["search_result"][0]["link"]
        return url
    else:
        return None

if __name__ == "__main__":
    for m in meta[START_INDEX:END_INDEX]:
        try:
            url = get_url(m)
            if url != None:
                print("{}: {}".format(m["song_name"], url))
            else:
                print("no urls fetched")
        except KeyboardInterrupt:
            break
        except:
            pass
