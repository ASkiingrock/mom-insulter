import random
import json


class Trait:
    def __init__(self, name):
        self.name = name


class Traits:

    def __init__(self):
        self.old = Trait("old")
        self.short = Trait("short")
        self.fat = Trait("fat")
        self.stupid = Trait("stupid")


class YourMom:
    def __init__(self, name, age, height_m, weight_kg, iq):
        self.name = name
        self.age = age
        self.height_m = height_m
        self.weight_kg = weight_kg
        self.iq = iq

        self.traits = []
        if self.age > 60:
            self.traits.append(Traits.old)
        if self.height_m < 1.55:
            self.traits.append(Traits.short)
        bmi = self.weight_kg / (self.height_m ** 2)
        if bmi > 25:
            self.traits.append(Traits.fat)
        if self.iq < 85:
            self.traits.append(Traits.stupid)

    def insult(self):
        with open("insults.json", "r") as f:
            insults = json.load(f)

        # if Traits.old in self.traits:
        #     print("Yo mama so old,", random.choice(insults["old"]), "\n")
        # if Traits.short in self.traits:
        #     print("Yo mama so short,", random.choice(insults["short"]), "\n")
        # if Traits.fat in self.traits > 25:
        #     print("Yo mama so fat,", random.choice(insults["fat"]), "\n")
        # if Traits.stupid in self.traits < 85:
        #     print("Yo mama so stupid,", random.choice(insults["stupid"]), "\n")

    def fact(self):
        bmi = self.weightkg / (self.heightm ** 2)
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


mom = YourMom('Owenna Smithus', 20, 1.59, 20, 90)
print(mom.name)
mom.insult()
print("\n")
