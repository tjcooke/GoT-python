from characters import characters

# How many characters are dead?
def dead_characters():
        dead_characters = 0
        for i in characters:
                if i["died"] != '':
                        dead_characters += 1
        print(dead_characters)
dead_characters()