from characters import characters
# Produce a list of characters with the last name "Targaryn"
new_list = []
def targaryen_family():
        for i in characters:
                if i["name"] != '':
                        if "Targaryen" in i["name"]:
                                new_list = i["name"]
                                print(new_list)
                                

print(targaryen_family())