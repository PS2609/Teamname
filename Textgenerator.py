import torch
from transformers import pipeline

model_tag = "postbot/gpt2-medium-emailgen"
generator = pipeline(
    "text-generation",
    model=model_tag,
    device=0 if torch.cuda.is_available() else -1,
)

prompt = """
Hello, 

Following up on the bubblegum shipment."""
result = generator(
    prompt,
    max_new_tokens=64,
    do_sample=True,
    no_repeat_ngram_size=3,
    pad_token_id=generator.tokenizer.eos_token_id,
    
) # generate
print(result[0]['generated_text'])