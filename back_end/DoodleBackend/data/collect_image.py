import os
from tqdm import tqdm
from .bing_image_downloader import downloader
from . import meta, get_id_str, DATASET_ROOT

START_IDX = 0
END_IDX = 40000

def get_query(m):
    return "{album_name} album art".format(album_name=m["album_name"])

def get_image(idx, m):
    image_root = os.path.join(DATASET_ROOT, "raw", "image")
    prefix = get_id_str(idx)
    query = get_query(m)

    downloader.download(query, prefix, limit=1,  output_dir=image_root, adult_filter_off=True, force_replace=False, timeout=60)

if __name__ == "__main__":
    print("Total {} songs...".format(len(meta)))
    print("Collecting Album Art Images...")

    failed_list = []
    for idx, m in enumerate(tqdm(meta[START_IDX: END_IDX])):
        try:
            get_image(idx, m)
        except:
            failed_list.append([idx])
    
    print("failed: {}".format(failed_list))
    # TODO save failed list later