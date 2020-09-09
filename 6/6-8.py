if __name__ == "__main__":
    dj = {
        'type': 'cat',
        'owner': 'kjell'
    }

    jessie = {
        'type': 'cat',
        'owner': 'kirsten'
    }

    lois = {
        'type': 'cat',
        'owner': 'benthe'
    }

    pets = [dj, jessie, lois]

    for pet in pets:
        for key, value in pet.items():
            print(str(key) + " is " + str(value))