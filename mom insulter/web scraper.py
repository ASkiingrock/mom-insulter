# wasn't bothered to build a web scraper
# just copied yo mama jokes from a website, but there were new lines characters so JSON didn't like it
# imported it into word, ctrl h and then select paragraph mark, replace all
# do the same, and then manual new line, replace all
# then its just a solid slab of text

import re
import json

with open("test.json", "r", encoding="utf-8") as file:
    yo_mama_jokes = json.load(file)

# split into sentences
yo_mama_jokes = str(yo_mama_jokes)
yo_mama_jokes = ''.join([i for i in yo_mama_jokes if not i.isdigit()])
sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', yo_mama_jokes)

# split into yo mama's so... (a[0]) and then insult (a[2])
for item in sentences:
    if "Yo mama so" not in item:
        sentences.remove(item)
    else:
        say_split = item.split("Yo mama so", 1)
        say_split = say_split[1][1:-1]
        a = str(say_split).partition(',')
        category = a[0]
        insult = a[2]
        full_split = item.split("Yo mama so ")
        full_split_2 = full_split[1].split(", ")
        # this does work yet
        with open("test.json", "r", encoding="utf-8") as file:
            yo_mama_jokes = json.load(file)
        if category.lower() in "olddumbtallshortrichpoorother":
            yo_mama_jokes[category.lower()].append(insult[1:])
        else:
            try:
                yo_mama_jokes["other"][full_split_2[0]] = full_split_2[1]
            except IndexError:
                print("there was 1 sussy error ..... it's probably fine")
        with open("test.json", "w", encoding="utf-8") as file:
            json.dump(yo_mama_jokes, file, indent=4)
