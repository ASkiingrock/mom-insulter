import random
import json
#/Users/owensmith/Documents/VS Code/mom insulter/yourmom.json
class your_mom:
    def __init__(self, name, age, heightm, weightkg, iq):
        self.name = name
        self.age = age
        self.heightm = heightm
        self.weightkg = weightkg
        self.iq = iq
    def insult(self):
        with open("/Users/owensmith/Documents/VS Code/mom insulter/yourmom.json", "r") as f:
            yourmom = json.load(f)
        #change random.chocie
        bmi = self.weightkg/(self.heightm**2)
        if self.age > 60:
            print(f'Yo mama is {self.age}, which is over 60, therefore: she old.')
            print("Yo mama so old,", random.choice(yourmom["old"]), "\n")
        if self.heightm < 1.55:
            print(f"Yo mama is {self.height}, which is fairly under the average of 1.62m")
            print("Yo mama so short,", random.choice(yourmom["short"]), "\n")
        if bmi > 25:
            print(f"Yo mama has a bmi of {bmi:.2f}, which classifies her as overweight or obese.")
            print("Yo mama so fat,", random.choice(yourmom["fat"]), "\n")
        if self.iq < 85:
            print(f"Yo mama has an iq of {self.iq}, which is fairly below the average of 100 and classifies her as mentally impaired.")
            print("Yo mama so stupid,", random.choice(yourmom["stupid"]), "\n")

mom = your_mom('al', 70, 1.59, 100, 70)
print("\n")
mom.insult()
print("\n")
