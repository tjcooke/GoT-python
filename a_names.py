from characters import characters

# How many character names start with "A"?
def a_Names(characters):
        aNames = 0
        for names in characters:
                if names["name"][0] == "A":
                        aNames += 1
        print(aNames)
a_Names(characters)