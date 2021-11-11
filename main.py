import classes
import json

# Load test mum
with open("test_mum.json", "r") as f:
    test_mum = json.load(f)
mom = classes.Mum(test_mum["name"], test_mum["age"], test_mum["height_m"], test_mum["weight_kg"], test_mum["iq"],
                  test_mum["attractiveness"], test_mum["scariness"], test_mum["nationality"])

# Testing funcs
mom.insult()
print("\n")
mom.fact()