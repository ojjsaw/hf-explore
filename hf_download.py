"""Script to Download OpenVINO Model from HuggingFace"""

import sys
import os
from huggingface_hub import snapshot_download

def download_snapshot(repo_id, project_path):
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    
    try:
        snapshot_download(repo_id, local_dir=project_path, local_dir_use_symlinks=True)
    except Exception as err:
        print(f"ERROR DOWNLOADING MODEL: {err}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the repo_id and local_dir as command line arguments.")
        sys.exit(1)
    
    repo_id = sys.argv[1]
    project_path = sys.argv[2]
    download_snapshot(repo_id, project_path)
    
