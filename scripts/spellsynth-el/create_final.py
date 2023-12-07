import tiktoken

def count_tokens(string: str):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(string))

def convert_to_jsonl():
    print()

def main(sentences_filepath):
    print()

if __name__ == '__main__':
    SENTENCES_FILEPATH = 'data/processed/en-el-sentences.json'
    main(SENTENCES_FILEPATH)
