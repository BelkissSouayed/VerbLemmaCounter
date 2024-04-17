# Lemmy - Verb Lemma Counting

## Overview
This Python tool identifies the five most common verb lemmas in a text file and prints them along with their frequencies. Optionally, it can also display an example sentence containing each lemma.

## Installation
Ensure you have Python and Poetry installed. Then, run the following command to install dependencies:
`poetry install`

## Usage
Run the program using:
`poetry run python lemmy/main.py <path_to_text_file>`

To include example sentences with each lemma:
`poetry run python lemmy/main.py <path_to_text_file> --example`

## Running Tests
Execute the unit tests with:
`poetry run pytest`


