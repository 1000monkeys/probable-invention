if __name__ == "__main__":
    kjell_info = {
        'name': 'Kjell',
        'last-name': 'Vos',
        'age': 26,
        'city': 'Groningen'
    }

    bjorn_info = {
        'name': 'Bjorn',
        'last-name': 'Vos',
        'age': 30,
        'city': 'Valthermond'
    }

    benthe_info = {
        'name': 'Benthe',
        'last-name': 'Vos',
        'age': 28,
        'city': 'Groningen'
    }

    people = [kjell_info, bjorn_info, benthe_info]

    for person in people:
        for key, value in person.items():
            print(str(key) + " is " + str(value))
