import json


# find all categories
def keys():
    with open("insults.json", "r", encoding="utf-8") as file:
        json_object = json.load(file)
        joke_categories = json_object.keys()
        values = []
        for item in joke_categories:
            values.append(len(json_object[item]))
        keys_values = sorted(zip(values, joke_categories))
        print(keys_values)


# comment this out depending on whether you want to see the keys
keys()
