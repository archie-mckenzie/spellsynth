# scripts/spellsynth-el/create_final.py
# Collate processed datasets into final .jsonl file for training
# Author: Archie McKenzie 
# © 2023, MIT License

# ----- IMPORTS ----- #

import tiktoken

# ----- FUNCTIONS ----- #

def count_tokens(string: str):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(string))

def convert_to_jsonl():
    print()

# ----- MAIN ----- #

def main():
    print()

# ----- SETUP ----- #

if __name__ == '__main__':
    print()