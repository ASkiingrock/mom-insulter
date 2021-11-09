#wasn't bothered to build a web scraper
#just copied yo mama jokes from a website, but there were new lines characters so JSON didn't like it
#imported it into word, ctrl h and then select paragraph mark, replace all
#do the same, and then manual new line, replace all
#then its just a solid slab of text

import re
import json
with open ("yo_mama_analyser_output.json", "r") as file:
    yomamas = json.load(file).get("scarymommy.com")

old = []
dumb = []
tall = []
short = []
rich = []
poor = []
other = []

#split into sentences
yomamas = str(yomamas)
yomamas = ''.join([i for i in yomamas if not i.isdigit()])
sentences = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', yomamas)

#split into yo mama's so... (a[0]) and then insult (a[2])
for item in sentences:
    if "Yo mama so" not in item:
        sentences.remove(item)
    else: 
        saysplit = item.split("Yo mama so",1)
        saysplit = saysplit[1][1:-1]
        a = str(saysplit).partition(',')
        category = a[0]
        insult = a[2]
#this works, although it adds some weird characters to the json if you run it, so ill iron that out later
        match category:
            case "old":
                old.append(insult)
            case "dumb":
                dumb.append(insult)
            case "tall":
                tall.append(insult)
            case "short":
                short.append(insult)
            case "rich":
                rich.append(insult)
            case "poor":
                poor.append(insult)
            case _:
                other.append(insult)
with open ("yo_mama_analyser_output.json", "r") as file:
    json_object = json.load(file)

json_object["old"] = (old)
json_object["dumb"] = (dumb)
json_object["tall"] = (tall)
json_object["short"] = (short)
json_object["rich"] = (rich)
json_object["poor"] = (poor)
json_object["other"] = (other)

with open("yo_mama_analyser_output.json", "w") as file:
    json.dump(json_object, file)
    file.close()


        
        

