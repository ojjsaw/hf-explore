import sys
import os
from huggingface_hub import snapshot_download

def download_snapshot(model_id, project_path):
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    
    snapshot_download(model_id, local_dir=project_path, cache_dir='/data/dlwb_cloud/hf_models_cache/', local_dir_use_symlinks=True)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide the model_id and project_path as command line arguments.")
        sys.exit(1)
    
    model_id = sys.argv[1]
    project_path = sys.argv[2]
    download_snapshot(model_id, project_path)