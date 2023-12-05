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

<a href='https://tatoeba.org'>Tatoeba.org</a> is a free digital collection of sentences and translations. Download the latest language pair data from <a href='https://tatoeba.org/en/downloads'>Tatoeba</a> into `data/raw`. Or, decompress all files in `data/compressed` and copy the result into `data/raw`.