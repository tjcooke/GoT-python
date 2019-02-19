from characters import characters

# How many characters are not in the show? 
not_in_show = 0
for i in characters:
        if i["tvSeries"] == ['']:
                not_in_show += 1
                
print(not_in_show)