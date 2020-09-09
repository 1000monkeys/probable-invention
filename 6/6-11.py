if __name__ == "__main__":
    cities = {
        'groningen': {
            'country': 'netherlands',
            'population': '200366',
            'fact': 'My current home!'
        },
        'valthermond': {
            'country': 'netherlands',
            'population': '3488',
            'fact': 'My ancestral home!'
        },
        'rotterdam': {
            'country': 'netherlands',
            'population': '623652',
            'fact': 'Home of Feijenoord!'
        }
    }

    for city, information in cities.items():
        print(city + "'s info:")
        for value in information:
            print(information[value])

        print("\n")
