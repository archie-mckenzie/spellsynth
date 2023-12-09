# scripts/spellsynth-el/synthesize.py
# Creates synthetic language data using GPT-4
# Author: Archie McKenzie 
# © 2023, MIT License

# ----- IMPORTS ----- #

import json
import random
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed, TimeoutError
import time, datetime
from call_gpt4 import complete

# ----- STATS ----- #

class SynthesisStats:
    def __init__(self, update_interval : str, target_size: str):
        self.update_interval = update_interval
        self.target_size = target_size
        self.successes = 0
        self.failures = 0
        self.next_update = 0

    def update_user(self, succeeded: int = 0, failed: int = 0):
        self.successes += succeeded
        self.failures += failed
        if self.successes + self.failures >= self.next_update and self.update_interval > 0:
            print(f'Synthesized {self.successes} / {self.target_size}\nFailures: {self.failures}\n')
            self.next_update += self.update_interval
        
# ----- MAIN ----- #

def main(
        sentences_filepath: str, 
        output_filepath: str,
        synthesis_prompts: List[Tuple[float, str]],
        target_size: int,
        update_interval: int,
        max_concurrent_syntheses: int,
        timeout: int
    ):

    with open(sentences_filepath, 'r') as file:
        sentences = json.load(file)

    stats = SynthesisStats(update_interval, target_size)

    synthetic_dataset = []

    def create_prompt(sentence_object):
        return (random.choices(synthesis_prompts, weights=[p[0] for p in SYNTHESIS_PROMPTS], k=1)[0][1] + sentence_object["el"])

    def complete_and_translate(prompt):
        try:
            time.sleep(2 / random.uniform(1, 25)) # to avoid being suspected of ddos-ing openai
            completion = complete(prompt)
            final_object = json.loads(completion)
            if final_object["en"] and final_object["el"]:
                return final_object 
            else: return None
        except Exception as exception:
            print(exception)
            return None
        
    with ThreadPoolExecutor() as executor:
        while (len(synthetic_dataset) < target_size):
            sentence_objects_selected = random.sample(list(sentences), target_size - len(synthetic_dataset))
            prompts_selected = [create_prompt(sentence_object) for sentence_object in sentence_objects_selected]
            for i in range(0, len(prompts_selected), max_concurrent_syntheses):
                print(f'With samples {i + 1} -> {min(i + max_concurrent_syntheses, len(prompts_selected))} of {len(prompts_selected)} for this subset:\n')
                print(datetime.datetime.now())
                concurrent_subset = prompts_selected[i : i + max_concurrent_syntheses]
                completed_futures = []
                try:
                    futures = [executor.submit(complete_and_translate, prompt) for prompt in concurrent_subset]
                    for future in as_completed(futures, timeout = timeout):
                        completed_futures.append(future.result(timeout = timeout))
                except TimeoutError as exception:
                    print(exception)
                    print(f"i.e. {len(concurrent_subset) - len(completed_futures)} tasks did not complete in time.\n")
                finally:
                    successful_syntheses = [synthdata for synthdata in completed_futures if synthdata != None]
                    stats.update_user(len(successful_syntheses), len(concurrent_subset) - len(successful_syntheses)) 
                    if len(successful_syntheses) > 0: # if there are successes
                        synthetic_dataset.extend(successful_syntheses)
                        with open(output_filepath, 'w') as file: # just in case!!!!
                            json.dump(synthetic_dataset, file)
                    else:
                        sleep_time = random.uniform(1, 25)
                        print(f'Entire batch failed. Waiting {sleep_time}s before trying another batch.')
                        time.sleep(sleep_time)
                    
    with open(output_filepath, 'w') as file:
        json.dump(synthetic_dataset, file)

# ----- SETUP ----- #

if __name__ == '__main__':
    SENTENCES_FILEPATH = 'data/processed/en-el-sentences.json'
    OUTPUT_FILEPATH = 'data/processed/en-el-synthdata.json'
    SYNTHESIS_PROMPTS = [
        [0.25, 'Write an interesting 30-word paragraph in Greek inspired by the following Greek sentence. Then write the English translation. Give your answer in JSON format with both the Greek and the English. Greek sentence: '],
        [0.25, 'Write an interesting 75-word passage in Greek inspired by the following Greek sentence. Then write the English translation. Give your answer in JSON format with both the Greek and the English. Greek sentence: '],
        [0.25, 'Write an interesting longform passage in Greek inspired by the following Greek sentence. Then write the English translation. Give your answer in JSON format with both the Greek and the English. Greek sentence: '],
        [0.25, 'Write an extensive multi-paragraph response in Greek inspired by the following Greek sentence. Then write the English translation. Make sure to use advanced, but fluid, vocabulary and sentence structure. Give your answer in JSON format with both the Greek and the English. Greek sentence: '],
    ]
    TARGET_SIZE = 10000
    UPDATE_INTERVAL = 100
    MAX_CONCURRENT_SYNTHESES = 100
    TIMEOUT = 250
    main(
        SENTENCES_FILEPATH,
        OUTPUT_FILEPATH,
        SYNTHESIS_PROMPTS,
        TARGET_SIZE,
        UPDATE_INTERVAL,
        MAX_CONCURRENT_SYNTHESES,
        TIMEOUT
    )
