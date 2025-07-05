import os
import gdown

# File ID for visuals
VISUALS_ID = "1ROtbYVY1-qdU1Uq2P6VZjJFzzGYETN8H"
VISUALS_LOCAL = "visuals.ipynb"

def download_if_missing(file_id, output_path):
    if not os.path.exists(output_path):
        gdown.download(f"https://drive.google.com/uc?id={file_id}", output_path, quiet=False)

def maybe_download_visuals(should_download: bool):
    if should_download:
        download_if_missing(VISUALS_ID, VISUALS_LOCAL)