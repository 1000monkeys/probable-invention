def make_album(artist, album, amount_songs=""):
    dictionary = {'artist': artist, 'album': album}
    if amount_songs:
        dictionary['amount_songs'] = amount_songs

    return dictionary


print(make_album("Kensington", "Control"))
print(make_album("Infected Mushroom", "Converting Vegetarians 2"))
print(make_album("Avenged Sevenfold", "The Stage"))
print(make_album("Big Data", "2.0", "10"))
