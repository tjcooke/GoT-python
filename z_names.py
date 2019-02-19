from characters import characters

# How many character names start with "Z"?
def z_Names(characters):
        zNames = 0
        for names in characters:
                if names["name"][0] == "Z":
                        zNames += 1
        print(zNames)
z_Names(characters)