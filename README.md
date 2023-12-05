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

Spellsynth is a system for fine-tuning powerful LLM translators.

This repo contains the data and scripts for four translators:

<ul>
    <li><code>spellsynth-el-llama-2</code> and `spellsynth-el-gpt4`</li>
    <li>`kaleidograph-llama-2` and `kaleidograph-gpt-4`</li>
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