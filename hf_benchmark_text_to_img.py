import os
import sys
import time
from datetime import datetime
import pytz
from transformers import pipeline
from optimum.intel import OVStableDiffusionPipeline

def infer_txt_to_img(model_id, prompt, num_inference_steps, output_images, project_path):
    try:
        start_time = time.time()
        
        pipeline = OVStableDiffusionPipeline.from_pretrained(model_id, compile=False)
        pipeline.reshape(batch_size=1, height=512, width=512, num_images_per_prompt=output_images)
        pipeline.compile()
        
        compile_time = time.time() - start_time
        print(f"Model Load Time: {compile_time:.2f} seconds")

        # Start time tracking for inference
        inference_start_time = time.time()
        
        images = pipeline(prompt, num_inference_steps=num_inference_steps, output_type="pil").images
        
        # Calculate the total inference time
        inference_end_time = time.time()
        total_inference_time = inference_end_time - inference_start_time
        print(f"Inference Time: {total_inference_time:.2f} seconds")

        print(f"Prompt: {prompt}")

        # Calculate images per minute (60 / total_inference_time in seconds)
        images_per_minute = ((60 * output_images) / total_inference_time) if total_inference_time > 0 else 0
        print(f"Images/Minute: {images_per_minute:.2f}")

        current_time = datetime.now(pytz.utc)
        time_stamp = f"{current_time.strftime('%Y_%m_%d%H_%M_%S')}"       
        dir_path = f"{project_path}/benchmark/{time_stamp}"

        # Check if the directory exists, and create it if it doesn't
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Save all images to the new directory
        for i, img in enumerate(images):
            file_path = f"{dir_path}/output_image_0{i + 1}.png"
            img.save(file_path)
            print(f"Generated Output Images Saved at: {file_path}")

    except Exception as err:
        print(f"Error: {err}")
        sys.exit(99)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage for text-to-image: hf_benchmark_text-to-img.py <model_name> <prompt> <num_inference_steps> <num_output_images> <project_path>")
        sys.exit(1)
    model_id = sys.argv[1]
    prompt = sys.argv[2]
    num_inference_steps = int(sys.argv[3])
    output_images = int(sys.argv[4])
    project_path = sys.argv[5]
    infer_txt_to_img(model_id, prompt, num_inference_steps, output_images, project_path)