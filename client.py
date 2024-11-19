from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"  # Can be replaced with other locally supported models
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Input prompt
prompt = "What is Python?"
inputs = tokenizer.encode(prompt, return_tensors="pt")

# Generate response
outputs = model.generate(inputs, max_length=50, num_return_sequences=1)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(response)

