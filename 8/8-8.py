def make_album(artist, album, amount_songs=""):
    dictionary = {'artist': artist, 'album': album}
    if amount_songs:
        dictionary['amount_songs'] = amount_songs

    return dictionary


while True:
    print("Please enter an artist, album name and the amount of songs on the album(not needed)!")
    print("input 'q' at any time to quit!")

    artist = input("Please enter the artist name: ")
    if artist == "q":
        break

    album = input("Please enter the album name: ")
    if album == "q":
        break

    amount_songs = input("Please enter the amount of songs on the album(x for no): ")
    if amount_songs == "q":
        break

    if amount_songs.capitalize() != "X":
        temp = make_album(artist, album, amount_songs)
    else:
        temp = make_album(artist, album)

    print(temp)


#print(make_album("Kensington", "Control"))
#print(make_album("Infected Mushroom", "Converting Vegetarians 2"))
#print(make_album("Avenged Sevenfold", "The Stage"))
#print(make_album("Big Data", "2.0", "10"))
