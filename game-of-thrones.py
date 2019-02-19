from characters import characters
# print(len(characters))

#How many character names start with "A"?
def a_Names(characters):
        aNames = 0
        for names in characters:
                if names["name"][0] == "A":
                        aNames += 1
        print(aNames)
a_Names(characters)

#How many character names start with "Z"?
def z_Names(characters):
        zNames = 0
        for names in characters:
                if names["name"][0] == "Z":
                        zNames += 1
        print(zNames)
z_Names(characters)

# How many characters are dead?
def dead_characters():
        dead_characters = 0
        for i in characters:
                if i["died"] != '':
                        dead_characters += 1
        print(dead_characters)
dead_characters()

# How many characters are valyrian
def valyrian_characters():
        v_characters = 0
        for i in characters:
                if i["culture"] == "Valyrian":
                        v_characters += 1
        print(v_characters)
valyrian_characters()

#What actor plays "Hot Pie"
for i in characters:
        if i["name"] == "Hot Pie":
                actorName = i['playedBy']
print(actorName)

#How many characters are not in the show? 
not_in_show = 0
for i in characters:
        if i["tvSeries"] == ['']:
                not_in_show += 1
                
print(not_in_show)
# Who has the most titles? 

for i in characters:
        if i["titles"] != ['']:
                print("Name: %s Titles: %s" % (i["name"], len(i["titles"]))) # I dunno it works
                break

# Produce a list characters with the last name "Targaryn"
new_list = []
def targaryen_family():
        for i in characters:
                if i["name"] != '':
                        if "Targaryen" in i["name"]:
                                new_list = i["name"]
                                print(new_list)
                                

print(targaryen_family())



# print(max_titles)              
# print(maxcount)
# jon_snow = {"url":"https://anapioficeandfire.com/api/characters/583","name":"Jon Snow","gender":"Male","culture":"Northmen","born":"In 283 AC","died":"","titles":["Lord Commander of the Night's Watch"],"aliases":["Lord Snow","Ned Stark's Bastard","The Snow of Winterfell","The Crow-Come-Over","The 998th Lord Commander of the Night's Watch","The Bastard of Winterfell","The Black Bastard of the Wall","Lord Crow"],"father":"","mother":"","spouse":"","allegiances":["https://anapioficeandfire.com/api/houses/362"],"books":["https://anapioficeandfire.com/api/books/5"],"povBooks":["https://anapioficeandfire.com/api/books/1","https://anapioficeandfire.com/api/books/2","https://anapioficeandfire.com/api/books/3","https://anapioficeandfire.com/api/books/8"],"tvSeries":["Season 1","Season 2","Season 3","Season 4","Season 5","Season 6"],"playedBy":["Kit Harington"]}

# # print out the key names individually
# # for k in jon_snow:
# #     print(k)

# # print out just the values
# # for k in jon_snow:
# #     print(jon_snow[k])

# # print both the key and the value
# # for k in jon_snow:
# #    print("%s: %s" % (k, jon_snow[k]))

