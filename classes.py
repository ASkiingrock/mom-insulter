import random
import json


# Trait class - thought it might be useful later
class Trait:
    def __init__(self, name):
        self.name = name


# Mum class, contains all the properties of a mother you could make hilarious jokes about
# Will need to add to in future
class Mum:
    def __init__(self, name, age, height_m, weight_kg, iq, attractiveness, scariness, nationality, yearly_income):
        self.name = name  # Name
        self.age = age  # Age
        self.height_m = height_m  # Height in metres
        self.weight_kg = weight_kg  # Weight in kilograms
        self.iq = iq  # IQ
        self.attractiveness = attractiveness  # Attractiveness out of 10
        self.scariness = scariness  # Scariness out of 10
        self.nationality = nationality  # Nationality
        self.yearly_income = yearly_income # Yearly income $

        self.bmi = self.weight_kg / (self.height_m ** 2)  # BMI score

        self.traits = []  # Traits, e.g. "short", "ugly"

        # Append traits
        if self.age > 60:
            self.traits.append(old)
        if self.height_m < 1.55:
            self.traits.append(short)
        if self.bmi > 25:
            self.traits.append(fat)
        if self.iq < 85:
            self.traits.append(stupid)
        if self.attractiveness < 5:
            self.traits.append(ugly)
        if self.scariness > 6:
            self.traits.append(scary)
        if self.nationality.lower() in ["american", "united states", "united states of america", "usa", "us"]:
            self.traits.append(american)
        if self.yearlyincome() <= 60000:
            self.traits.append(poor)
        if self.yearlyincome() >= 330000:
            self.traits.append(rich)

    # Insult function, pretty self-explanatory
    # Start with name to give context for who it is, maybe print stats?
    def insult(self):
        with open("insults.json", "r", encoding="utf-8") as file:  # Load insults json file
            insults = json.load(file)
        print(f'Yo mama\'s name is {self.name}')
        # Make random joke based on what traits are present
        if old in self.traits:
            print("Yo mama so old,", random.choice(insults["old"]))
        if short in self.traits:
            print("Yo mama so short,", random.choice(insults["short"]))
        if fat in self.traits:
            print("Yo mama so fat,", random.choice(insults["fat"]))
        if stupid in self.traits:
            print("Yo mama so stupid,", random.choice(insults["stupid"]))
        if ugly in self.traits:
            print("Yo mama so ugly,", random.choice(insults["ugly"]))
        if scary in self.traits:
            print("Yo mama so scary,", random.choice(insults["scary"]))
        if american in self.traits:
            print("Yo mama so American,", random.choice(insults["american"]))
        if poor in self.traits:
            print("Yo mama so poor,", random.choice(insults["poor"]))
        if rich in self.traits:
            print("Yo mama so rich,", random.choice(insults["rich"]))

    # Fact function, not sure why this exists but Owen made it
    # Gotta explain why she is getting roasted so hard OSCAR
    # You know what? Makes sense
    def fact(self):
        if self.age > 60:
            print(f'Yo mama is {self.age}, which is over 60, therefore: she old.')
        if self.height_m < 1.55:
            print(f"Yo mama is {self.height_m}, which is fairly under the average of 1.62m")
        if self.bmi > 25:
            print(f"Yo mama has a bmi of {self.bmi:.2f}, which classifies her as overweight or obese.")
        if self.iq < 85:
            if self.iq < 50:
                print(f"Yo mama has an iq of {self.iq}, which is extremely below the average of 100 and classifies "
                      f"her as mentally impaired.")
            elif self.iq < 70:
                print(f"Yo mama has an iq of {self.iq}, which is highly below the average of 100 and classifies her "
                      f"as mentally impaired.")
            else:
                print(f"Yo mama has an iq of {self.iq}, which is fairly below the average of 100 and classifies her "
                      f"as mentally impaired.")
                
        if self.attractiveness < 5:
            print(f"Yo mama is a {self.attractiveness} out of 10. She ugly.")


old = Trait("old")
short = Trait("short")
fat = Trait("fat")
stupid = Trait("stupid")
ugly = Trait("ugly")
scary = Trait("scary")
american = Trait("american")
poor = Trait("poor")
rich = Trait("rich")
