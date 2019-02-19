from characters import characters

# How many characters are valyrian
def valyrian_characters():
        v_characters = 0
        for i in characters:
                if i["culture"] == "Valyrian":
                        v_characters += 1
        print(v_characters)
valyrian_characters()