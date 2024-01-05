#!/bin/bash
MODEL_ID=$1
PROJECT_PATH=$2
# shellcheck source=/dev/null
source /data/venv/openvino_2023.1.0/.venv/bin/activate

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python "${SCRIPT_DIR}"/hf_download.py "${MODEL_ID}" "${PROJECT_PATH}"

# Check the exit status of the Python script
if [ $? -ne 0 ]; then
    echo "An error occurred while downloading the model"
else 
    echo "MODEL DOWNLOADED SUCCESSFULLY"
fi

deactivate