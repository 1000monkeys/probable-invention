if __name__ == "__main__":
    favorite_places = {
        'kjell': ['Home', 'Noorderplantsoen', 'Jumbo euroborg'],
        'benthe': ['Car', 'Store', 'House'],
        'bjorn': ['Moviepark Germany', 'Rotterdam', 'Valthermond']
    }

    for name, favorite_place in favorite_places.items():
        print(name + "'s favorite places are:")
        for value in favorite_place:
            print(value)