import json

# Read the jokes from the raw jokes file. Gets each line as a list
with open("raw_jokes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    file.close()

for line in lines:
    if "Yo mama" not in line:  # Remove if you mama isn't in the joke
        print("removed")
        lines.remove(line)
    else:
        # Splits up the joke into category and punchline
        split_yo_mama = line.split("Yo mama so ")
        split_joke = split_yo_mama[1].split(", ", 1)
        category = split_joke[0].lower()  # e.g. fat, ugly, old, short
        punchline = split_joke[1].strip()  # What comes after the above

        with open("test.json", "r", encoding="utf-8") as file:
            insults = json.load(file)
            file.close()

        # Attempt to add joke to category, makes category if it doesn't exist
        try:
            for old_joke in insults[category]:
                if f"Yo mama so {category}, {punchline}" != old_joke:  # Checks if joke already exists
                    insults[category].append(punchline)
        except KeyError:
            insults[category] = [punchline]

with open("test.json", "w") as file:
    json.dump(insults, file, indent=4)
    file.close()
