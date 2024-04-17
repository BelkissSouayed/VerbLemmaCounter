from argparse import ArgumentParser
from typing import List, Dict
from collections import Counter
import random
import spacy

nlp = spacy.load("en_core_web_sm")

def lemmatize_corpus(corpus: str) -> List[str]:
    """
    Lemmatise a txt file.

    :param corpus: The file to be lemmatised.
    :return: A list of [verb lemmas].
    """
    doc = nlp(corpus)
    return [token.lemma_ for token in doc if token.pos_ == "VERB"]




def count_verbs_string(verb_lemmas: List[str]) -> str:
    """
    find the 5 most common verbs in a list
    :param verb_lemmas: the list of all verb lemmas (the output of the first function)
    :return: a string containing the 5 most common verb lemmas along with their frequency
    """

    verb_counter = dict(Counter(verb_lemmas).most_common(5))
    verb_count = []
    for word, count in verb_counter.items():
         verb_count.append(f"{count} {word}") #add a string to the list 
    return "\n".join(verb_count) # join all the strings using a newline  as a separator



def count_verbs(verb_lemmas: List[str]) -> Dict[str, int]:
    """find the 5 most common verbs in a list"""
    verb_counter = dict(Counter(verb_lemmas).most_common(5))
    return verb_counter



def extract_example_sentences(corpus: str, verb_counts: Dict[str, int]) -> None:
    """
    Extract a random example sentence for each of the 5 most common verb lemmas.

    :param corpus: The txt file that contains the sentences.
    :param verb_counts: A dictionary of the 5 most common verb lemmas and their frequency.
    """

    with open(corpus, "r") as f:
        sentences = [sentence.strip() for sentence in f] #turn the corpus into a list of sentences
        for verb, count in verb_counts.items(): #iterating over the verbs and their frequencies
            example_sentences = [sentence for sentence in sentences 
                             if verb in sentence and len(sentence) < 250]  #to not extract super long sentences
            if example_sentences:
                example_sentence = random.choice(example_sentences) #selecting a random sentence from the list
                print(f"{count}\t{verb}\t{example_sentence}")   #print them in the requested format

def main():
    parser = ArgumentParser(description="Identify the five most common verb lemmas.")
    parser.add_argument("corpus", type=str, help="the txt file to lemmatise")
    parser.add_argument(
        "--example", action="store_true", help="print an example sentence  for each verb lemma  from the text file."
    )
  
    args = parser.parse_args()
    
    with open(args.corpus, 'r', encoding='utf-8') as f:
        verb_lemmas = []
        for line in f:
            verb_lemmas += lemmatize_corpus(line)

    verb_counts = count_verbs(verb_lemmas)
    if args.example:
        verb_counts = count_verbs(verb_lemmas)
        extract_example_sentences(args.corpus, verb_counts) 
    else:
        verb_counts = count_verbs_string(verb_lemmas) # this is when I needed the output of the first count function
        print(verb_counts)
        
if __name__ == '__main__':
    main()


