import json

# Read the jokes from the raw jokes file. Gets each line as a list
with open("joke-reading/raw_jokes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("insults.json", "r", encoding="utf-8") as file:
    length = 0
    for line in file:
        length += 1

for line in lines:
    # edit this based on format of text (e.g. starts with yo mama or yo mama's or yo mammy) or else it won't do anything
    if "yo momma" not in line.lower():  # Remove if you mama isn't in the joke
        lines.remove(line)
    else:
        # Splits up the joke into category and punchline
        try:
            # may need to change depending on format
            split_yo_mama = line.lower().split("yo momma so ")
            # returns errors if phrase is not in
            split_joke = split_yo_mama[1].split(", ", 1)
            category = split_joke[0].lower()  # e.g. fat, ugly, old, short
            punchline = split_joke[1].strip()  # What comes after the above

            with open("insults.json", "r", encoding="utf-8") as file:
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

            with open("insults.json", "w", encoding="utf-8") as file:
                json.dump(insults, file, indent=4, ensure_ascii=False)
                file.close()
        except Exception as e:
            print(f"\"{line}\" not correct format ({e})")
            continue

with open("insults.json", "r", encoding="utf-8") as file:
    new_length = 0
    for line in file:
        new_length += 1
    print(f'{new_length - length} lines were added')
    file.close()
