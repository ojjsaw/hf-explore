#!/bin/bash
MODEL_ID=$1
PROMPT=$2
INFERENCE_STEPS=$3
OUTPUT_IMAGES=$4
PROJECT_PATH=$5
source my_venv/.venv/bin/activate

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python "${SCRIPT_DIR}"/hf_benchmark_text_to_img.py "${MODEL_ID}" "${PROMPT}" "${INFERENCE_STEPS}" "${OUTPUT_IMAGES}" "${PROJECT_PATH}"


# Check the exit status of the Python script
if [ $? -eq 1 ]; then
    echo "Invalid arguments provided for benchmarking command"
fi

if [ $? -eq 99 ]; then
    echo "An error occurred during the benchmarking process"
fi

deactivate