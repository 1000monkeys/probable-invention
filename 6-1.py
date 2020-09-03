if __name__ == "__main__":
    kjell_info = {
        'name': 'Kjell',
        'middle-name': 'Roderick',
        'last-name': 'Vos',
        'age': 26,
        'city': 'Groningen'
    }

    for key, value in kjell_info.items():
        print(str(key) + " is " + str(value))
