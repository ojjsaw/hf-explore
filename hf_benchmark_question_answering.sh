#!/bin/bash
MODEL_ID=$1
PROMPT=$2
MAX_OUTPUT_TOKENS=$3
CONTEXT=$4
PROJECT_PATH=$5
source /data/venv/openvino_2023.1.0/.venv/bin/activate

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

python "${SCRIPT_DIR}"/hf_benchmark_question_answering.py "${MODEL_ID}" "${PROMPT}" "${MAX_OUTPUT_TOKENS}" "${CONTEXT}" "${PROJECT_PATH}"


# Check the exit status of the Python script
if [ $? -eq 1 ]; then
    echo "Invalid arguments provided for benchmarking command"
fi

if [ $? -eq 99 ]; then
    echo "An error occurred during the benchmarking process"
fi

deactivate