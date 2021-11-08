import random
import json


class Trait:

    def __init__(self, name):
        self.name = name


class YourMom:
    def __init__(self, name, age, height_m, weight_kg, iq, attractiveness):
        self.name = name
        self.age = age
        self.height_m = height_m
        self.weight_kg = weight_kg
        self.iq = iq
        self.attractiveness = attractiveness

        self.traits = []
        if self.age > 60:
            self.traits.append(old)
        if self.height_m < 1.55:
            self.traits.append(short)
        bmi = self.weight_kg / (self.height_m ** 2)
        if bmi > 25:
            self.traits.append(fat)
        if self.iq < 85:
            self.traits.append(stupid)
        if self.attractiveness < 5:
            self.traits.append(ugly)

    def insult(self):
        with open("insults.json", "r") as f:
            insults = json.load(f)

        if old in self.traits:
            print("Yo mama so old,", random.choice(insults["old"]), "\n")
        if short in self.traits:
            print("Yo mama so short,", random.choice(insults["short"]), "\n")
        if fat in self.traits:
            print("Yo mama so fat,", random.choice(insults["fat"]), "\n")
        if stupid in self.traits:
            print("Yo mama so stupid,", random.choice(insults["stupid"]), "\n")
        if ugly in self.traits:
            print("Yo mama so ugly,", random.choice(insults["ugly"]), "\n")

    def fact(self):
        bmi = self.weight_kg / (self.height_m ** 2)
        if self.age > 60:
            print(f'Yo mama is {self.age}, which is over 60, therefore: she old.')
        if self.height_m < 1.55:
            print(f"Yo mama is {self.height_m}, which is fairly under the average of 1.62m")
        if bmi > 25:
            print(f"Yo mama has a bmi of {bmi:.2f}, which classifies her as overweight or obese.")
        if self.iq < 85:
            print(
                f"Yo mama has an iq of {self.iq}, which is fairly below the average of 100 and classifies her as "
                f"mentally impaired.")
        if self.attractiveness < 5:
            print(f"Yo mama is a {self.attractiveness} out of 10. She ugly.")


old = Trait("old")
short = Trait("short")
fat = Trait("fat")
stupid = Trait("stupid")
ugly = Trait("ugly")

mom = YourMom('al', 0, 2, 10, 40, 1)
print("\n")
mom.insult()
print("\n")
