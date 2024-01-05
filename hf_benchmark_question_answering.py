import os
import sys
import time
from datetime import datetime
import pytz
import torch
from transformers import AutoTokenizer
from optimum.intel import OVModelForQuestionAnswering

def infer_question_answering(model_id, prompt, max_output_tokens, context, project_path):
    try:
        start_time = time.time()
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = OVModelForQuestionAnswering.from_pretrained(model_id)

        load_time = time.time() - start_time
        print(f"Model Load Time: {load_time:.2f} seconds")
        
        inputs = tokenizer(prompt, context, return_tensors="pt", truncation=True)
        inference_start_time = time.time()
        # outputs = model(**inputs)
        outputs = model(**inputs,
                        truncation=True,
                        max_new_tokens=max_output_tokens
                        )

        inference_time = time.time() - inference_start_time
        print(f"Inference Time: {inference_time:.2f} seconds")

        answer_start_index = torch.argmax(outputs.start_logits, axis=-1).item()
        answer_end_index = torch.argmax(outputs.end_logits, axis=-1).item()

        predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index + 1]
        answer = tokenizer.decode(predict_answer_tokens)
        
        print(f"Prompt: {prompt}")
        print(f"Answer: {answer}")

        current_time = datetime.now(pytz.utc)
        time_stamp = f"{current_time.strftime('%Y_%m_%d%H_%M_%S')}"        
        dir_path = f"{project_path}/benchmark/{time_stamp}"
                
        # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_path = f"{dir_path}/generated_text.txt"
        #Write the Sentiment to an output file    
        with open(file_path, 'w') as file:
            file.write(f"Prompt: {prompt}\n")
            file.write(f"Answer: {answer}\n")
        print(f"Generated Text File Saved at: {file_path}")

    except Exception as err:
        print(f"Error: {err}")
        sys.exit(99)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage for question-answering: hf_benchmark_question_answering.py <model_name> <question> <context> <project_path>")
        sys.exit(1)

    model_id = sys.argv[1]
    prompt = sys.argv[2]
    max_output_tokens = sys.argv[3]
    context = sys.argv[4]
    project_path = sys.argv[5]
    infer_question_answering(model_id, prompt, max_output_tokens, context, project_path)