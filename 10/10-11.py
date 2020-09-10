import json

filename = "favorite_number.txt"


def get_stored_favorite_number():
    try:
        with open(filename) as f_obj:
            favorite_number = json.load(f_obj)
            print("I know your favorite number is " + favorite_number + "!")
    except FileNotFoundError:
        favorite_number = input("What is your favorite number? ")
        with open(filename, 'w') as f_obj:
            json.dump(favorite_number, f_obj)
            print("Saved your favorite number! Will remember it!")

    return favorite_number


favorite_number = get_stored_favorite_number()