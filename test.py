from optimum.intel import OVModelForCausalLM
from transformers import AutoTokenizer, pipeline
from optimum.intel import OVStabi

model_id = "helenai/gpt2-ov"
model = OVModelForCausalLM.from_pretrained(model_id, local_files_only=True)
tokenizer = AutoTokenizer.from_pretrained(model_id)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
results = pipe("He's a dreadful magician and")
print(results)




