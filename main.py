import classes
import json
import random

# Load test mum
with open("test_mum.json", "r") as f:
    test_mum = json.load(f)
mom = classes.Mum(test_mum["name"], test_mum["age"], test_mum["height_m"], test_mum["weight_kg"], test_mum["iq"],
                  test_mum["attractiveness"], test_mum["scariness"], test_mum["nationality"], test_mum["yearly_income"])

with open("insults.json", "r") as f:
    insultsjson = json.load(f)
    entry_list = list(insultsjson)
    category = random.choice(entry_list)
    punchline = random.choice(insultsjson[category])
    
random_insult = (f"Yo mama so {category}, {punchline}.")

# Testing funcs
choice = input("\nWould you like a personalised insult, or a random one? (p or r)\n>> ")
if choice.lower() == "p":
    print("\n")
    mom.both()
elif choice.lower() == "r":
    print("\n")
    print(random_insult)
    print("\n")