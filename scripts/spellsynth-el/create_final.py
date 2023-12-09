# scripts/spellsynth-el/create_final.py
# Collate processed datasets into final .jsonl file for training
# Author: Archie McKenzie 
# © 2023, MIT License

# ----- IMPORTS ----- #

import tiktoken
import json
import random

# ----- FUNCTIONS ----- #

def count_tokens(string: str):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(string))

def write_as_jsonl(json_array, file_path):
    total_tokens = 0
    with open(file_path, 'w') as file:
        for obj in json_array:
            json_string = json.dumps(obj)
            tokens = count_tokens(json_string)
            total_tokens += tokens
            file.write(json_string + '\n')
    return total_tokens

def format_per_openai(final_dataset):
    return [
        {
            "messages": [
                {
                    "role": "user",
                    "content": data["prompt"]
                },
                {
                    "role": "assistant",
                    "content": data["completion"]
                }
            ]
        } 
        for data in final_dataset
    ]

# ----- MAIN ----- #

def main(data_filepaths, language_prompts, output_directory):

    final_dataset = []

    for filepath in data_filepaths:

        with open(filepath, 'r') as file:
            dataset = json.load(file)

        for data in dataset:
            for prompt_object in language_prompts:
                final_dataset.append({
                    "prompt": prompt_object["prompt"] + (data["en"] if prompt_object["input"] == "en" else data["el"]),
                    "completion": (data["el"] if prompt_object["input"] == "en" else data["en"]),
                })

    openai_tokens = write_as_jsonl(format_per_openai(final_dataset), f'{output_directory}/openai.jsonl')
    print(f'{openai_tokens} tokens written to {output_directory}/openai.jsonl')
    
    replicate_tokens = write_as_jsonl(final_dataset, f'{output_directory}/replicate.jsonl')
    print(f'{replicate_tokens} tokens written to {output_directory}/replicate.jsonl')

# ----- SETUP ----- #

if __name__ == '__main__':
    DATA_FILEPATHS = [
        'data/processed/spellsynth-el/en-el-sentences.json',
        'data/processed/spellsynth-el/en-el-synthdata.json',
        'data/processed/spellsynth-el/en-el-wiki.json'
    ]
    LANGUAGE_PROMPTS = [
        {
            "input": "en",
            "output": "el",
            "prompt": "Translate from English to Greek:\n\n"
        },
        {
            "input": "el",
            "output": "en",
            "prompt": "Translate from Greek to English:\n\n"
        }
    ]
    OUTPUT_DIRECTORY = 'data/final/spellsynth-el'
    # main(DATA_FILEPATHS, LANGUAGE_PROMPTS, OUTPUT_DIRECTORY)
    # commented out to avoid accidentally rewriting files