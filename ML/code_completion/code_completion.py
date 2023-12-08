import os
import re
import argparse
from tqdm import tqdm

from transformers import pipeline, set_seed
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers.pipelines.base import Pipeline

def load_generation_pipe(model_name_or_path: str, gpu_device: int=0):
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    pipe = pipeline(
        'text-generation',
        model=model,
        tokenizer=tokenizer,
        device=gpu_device
    )

    print("load generation pipeline from {} over, vocab size = {}, eos id = {}, gpu device = {}.".format(
        model_name_or_path, len(tokenizer), tokenizer.eos_token_id, gpu_device)
    )

    return pipe

def code_completion(
    model_name_or_path: str,
    temperature: float,
    top_p: float,
    num_samples_per_task: int,
    max_new_tokens: int,
    gpu_device: int,
    output_dir: str,
    prompts: list,
    ) -> str:
    
    pipe: Pipeline = load_generation_pipe(model_name_or_path, gpu_device=gpu_device)
    
    for prompt in prompts:
        input_ids = pipe.tokenizer(prompt, return_tensors='pt').input_ids
        outputs = pipe.model.generate(input_ids=input_ids.to(pipe.device),
                                max_length=64 + len(input_ids[0]),
                                temperature=1.0,
                                top_k=50,
                                top_p=0.95,
                                repetition_penalty=1.0,
                                do_sample=True,
                                num_return_sequences=1,
                                length_penalty=2.0,
                                early_stopping=True,
                                pad_token_id=pipe.tokenizer.eos_token_id,
                                eos_token_id=pipe.tokenizer.eos_token_id,
                                )
        decoded = pipe.tokenizer.decode(outputs[0], skip_special_tokens=True)
    # print("Input :", prompt)
    # print("Output:", decoded)
    return (prompt, decoded)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run evaluation for code generation model on human-eval.')

    parser.add_argument('-model', '--model_name_or_path', type=str, default="model_code_completion_PyCodeGPT")
    parser.add_argument('-o', '--output_dir', type=str, default="results")
    parser.add_argument('-n', '--num_completions', type=int, default=100)
    parser.add_argument('-t', '--temperature', type=float, default=0.2)
    parser.add_argument('-p', '--top_p', type=float, default=0.95)
    parser.add_argument('-l', '--max_new_tokens', type=int, default=100)
    parser.add_argument('-gpu', "--gpu_device", type=int, default=0) # -1 for cpu / 0 for gpu

    args = parser.parse_args()

    prompts = ["def finbonacci("]

    (input, output) = code_completion(
        model_name_or_path=args.model_name_or_path,
        temperature=args.temperature,
        top_p=args.top_p,
        num_samples_per_task=args.num_completions,
        max_new_tokens=args.max_new_tokens,
        gpu_device=args.gpu_device,
        output_dir=args.output_dir,
        prompts=prompts
    )
    
    print("Input :", input)
    print("Output:", output)
    print("="* 40)