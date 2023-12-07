import tiktoken

def count_tokens(string: str):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(string))

def main(sentences_filepath):

    print()

if __name__ == '__main__':
    DATASET_FILEPATH = 'data/processed/en-el-sentences.tsv'
    main(DATASET_FILEPATH)
