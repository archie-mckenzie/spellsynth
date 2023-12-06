# Spellsynth

A System for Fine-Tuning <b>Spe</b>cialized <b>L</b>arge <b>L</b>anguage Models from <b>Synth</b>etic Data 

<a href='http://spellsynth.com'>spellsynth.com</a>

Archie McKenzie '24
<br/>
Department of Computer Science
<br/>
Princeton University

2023-24 Thesis
<br/>
Advised by Professor Brian Kernighan

## Introduction

Spellsynth is a system for fine-tuning powerful LLM translators. The fine-tuning datasets in <code>data/final</code>, as well as the weights to the <code>llama-2</code>-based models, are freely licensed.

This repo contains the data and instructions for fine-tuning four language models, using the OpenAI (<a href='https://platform.openai.com'>openai.com</a>) and Replicate (<a href='https://replicate.com'>replicate.com</a>) platforms.

<ul>
    <li><code>spellsynth-el-llama-2</code> and <code>spellsynth-el-gpt4</code></li>
    <li><code>kaleidograph-llama-2</code> and <code>kaleidograph-gpt-4</code></li>
</ul>

<i>Currently under construction. Please check back later.</i>

## Prerequisites

- Python >3.10.5 installed
- pip installed

## Setup

### Create a Virtual Environment
```bash
python3 -m venv spellsynth-env
source spellsynth-env/bin/activate  # On Windows, use `spellsynth-env\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root directory and add the following:

```bash
OPENAI_API_KEY='YOUR_OPENAI_API_KEY'
REPLICATE_API_TOKEN='YOUR_REPLICATE_API_TOKEN'
```

You only need API keys for the platforms you are using. 

## Data

### Sourcing

<a href='https://tatoeba.org'>Tatoeba.org</a> is a free digital collection of sentences and translations. <a href='https://tatoeba.org/en/downloads'>Download</a> the latest language pair data into `data/raw` or decompress all files in `data/raw/compressed`. Copy the result into a new folder `data/raw/uncompressed`.

Raw sentence pair data used for `spellsynth-el` models: English-Greek (`en-el.tsv`).

Raw sentence pair data used for `kaleidograph` models: twenty languages, chosen based on availability of data and worldwide reach:

<ul>
    <li>
        English
    </li>
    <li>
        Romance languages
        <ul>
            <li>French, Spanish, Portuguese, Italian</li>
        </ul>
    </li>
    <li>
        Germanic languages
        <ul>
            <li>German, Dutch</li>
        </ul>
    </li>
    <li>
        European (other)
        <ul>
            <li>Greek, Russian, Polish</li>
        </ul>
    </li>
    <li>
        East Asian
        <ul>
            <li>Chinese, Japanese, Korean</li>
        </ul>
    </li>
    <li>
        West Asian
        <ul>
            <li>Hebrew, Arabic, Persian, Turkish</li>
        </ul>
    </li>
    <li>
        Global (other)
        <ul>
            <li>Hindi, Swahili, Indonesian</li>
        </ul>
    </li>
</ul>

Note: all sentence data was collected on 12/6/23. 



