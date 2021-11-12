# find all categories
def keys():
    with open("/Users/owensmith/Documents/VS Code/mom-insulter/insults.json", "r", encoding="utf-8") as file:
        json_object = json.load(file)
        keys = json_object.keys()
        values = []
        for item in keys:
            values.append(len(json_object[item]))
        keysvalues = sorted(zip(values,keys))
        print(keysvalues)

#comment this out depending on whether you want to see the keys
keys()
