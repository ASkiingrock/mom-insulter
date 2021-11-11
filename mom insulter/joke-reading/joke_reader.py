import json

# Read the jokes from the raw jokes file. Gets each line as a list
with open("raw_jokes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    file.close()

for line in lines:
    if "Yo mama" not in line:  # Remove if you mama isn't in the joke
        lines.remove(line)
    else:
        # Splits up the joke into category and punchline
        split_yo_mama = line.split("Yo mama so ")
        split_joke = split_yo_mama[1].split(", ", 1)
        category = split_joke[0].lower()  # e.g. fat, ugly, old, short
        punchline = split_joke[1].strip()  # What comes after the above

        with open("joke_reader_output.json", "r", encoding="utf-8") as file:
            insults = json.load(file)
            file.close()

        # Attempt to add joke to category, makes category if it doesn't exist
        try:
            for old_punchline in insults[category]:
                if punchline not in insults[category]:  # Checks if joke already exists
                    insults[category].append(punchline)

        # This didn't work because the json dump was outside of the loop so it never saved
        # Works now
        except KeyError:
            insults[category] = []
            insults[category].append(punchline)

        with open("mom insulter/joke-reading/joke_reader_output.json", "w", encoding="utf-8") as file:
            json.dump(insults, file, indent=4, ensure_ascii=False)
            file.close()


# find all categories
def keys():
    with open("mom insulter/joke-reading/joke_reader_output.json", "r", encoding="utf-8") as file:
        categories = json.load(file)
        print(categories.keys())
        categories.close()
