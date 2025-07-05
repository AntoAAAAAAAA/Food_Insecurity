import os
import gdown
import zipfile

# File IDs and paths
VISUALS_ID = "1ROtbYVY1-qdU1Uq2P6VZjJFzzGYETN8H"
SHAPEFILE_ID = "1B-ZWE9w-QTXyunczlcrCN8V2TYsxK1mZ"

VISUALS_LOCAL = "visuals.ipynb"
SHAPEFILE_ZIP_PATH = "data/tl_2019_us_county_shapefile.zip"
SHAPEFILE_EXTRACT_PATH = "data/shapefile"
SHAPEFILE_LOAD_PATH = os.path.join(SHAPEFILE_EXTRACT_PATH, "tl_2019_us_county.shp")


def download_if_missing(file_id, output_path):
    if not os.path.exists(output_path):
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)


def prepare_shapefile():
    download_if_missing(SHAPEFILE_ID, SHAPEFILE_ZIP_PATH)
    if not os.path.exists(SHAPEFILE_EXTRACT_PATH):
        with zipfile.ZipFile(SHAPEFILE_ZIP_PATH, "r") as zip_ref:
            zip_ref.extractall(SHAPEFILE_EXTRACT_PATH)
    return SHAPEFILE_LOAD_PATH


def maybe_download_visuals(should_download: bool):
    if should_download:
        download_if_missing(VISUALS_ID, VISUALS_LOCAL)
