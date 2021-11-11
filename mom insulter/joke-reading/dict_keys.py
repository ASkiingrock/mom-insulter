import json

with open("mom insulter/joke-reading/joke_reader_output.json", "r", encoding="utf-8") as file:
    categories = json.load(file)

print(categories.keys())