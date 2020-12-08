import os
import json

# Global Level Constants
DATASET_ROOT = "/home/litcoderr/dataset/DoodleDataset"

# Load JSON Meta Data
with open(os.path.join(DATASET_ROOT, "meta", "song_meta.json")) as file:
    print("Loading Meta Data...")
    meta = json.load(file)
with open(os.path.join(DATASET_ROOT, "meta", "genre_gn_all.json")) as file:
    print("Loading Genre Data...")
    genre = json.load(file)

dataset_size = len(meta)
n_digits = len(str(dataset_size))

# Unique Image Id is equivalent to index of meta data
def get_id_str(idx):
    return "{}".format(idx).zfill(n_digits)
