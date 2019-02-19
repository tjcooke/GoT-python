from characters import characters

# What actor plays "Hot Pie"
for i in characters:
        if i["name"] == "Hot Pie":
                actorName = i['playedBy']
print(actorName)