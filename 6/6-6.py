if __name__ == "__main__":
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python'
    }

    persons = {
        'jen',
        'sarah',
        'bjorn',
        'benthe'
    }

    for person in persons:
        if person in favorite_languages.keys():
            print(person + ", Thanks for filling this enquete out!")
        else:
            print(person + ", You should really do this enquete!")