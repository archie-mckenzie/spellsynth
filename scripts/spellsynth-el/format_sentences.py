# scripts/spellsynth-el/format_sentences.py
# Format sentences from raw .tsv to .json
# Author: Archie McKenzie 
# © 2023, MIT License

# ----- IMPORTS ----- #

import csv
import json
import tiktoken

# ----- FUNCTIONS ----- #

def count_tokens(string: str):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(string))

# ----- MAIN ----- #

def main(dataset_filepath: str):
    sentences = []
    total_tokens = 0

    with open(dataset_filepath, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            total_tokens += count_tokens(row[1]) + count_tokens(row[3])
            sentences.append({
                'en': row[1],
                'el': row[3]
            })

    with open('data/processed/en-el-sentences.json', 'w') as json_file:
        json.dump(sentences, json_file, ensure_ascii=False, indent=4)

    print(len(sentences))
    print(total_tokens)

# ----- SETUP ----- #

if __name__ == '__main__':
    DATASET_FILEPATH = 'data/raw/uncompressed/en-el.tsv'
    main(DATASET_FILEPATH)
