#wasn't bothered to build a web scraper
#just copied yo mama jokes from a website, but there were new lines characters so JSON didn't like it
#imported it into word, ctrl h and then select paragraph mark, replace all
#do the same, and then manual new line, replace all
#then its just a solid slab of text

import re
import json
with open ("test.json", "r") as file:
    yomamas = json.load(file)

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
#this doesn't work yet
        with open ("test.json", "r") as file:
            yomamas = json.load(file)
            if category.lower() in "olddumbtallshortrichpoorother":
                json.update({(category.lower()):insult})
            else:
                json.update({"other":a})

        
        

