if __name__ == "__main__":
    age = 13

    if age < 2:
        print("You little baby!")
    elif 2 < age < 4:
        print("You toddler!")
    elif 4 <= age < 13:
        print("You child!")
    elif 13 <= age < 20:
        print("You teenager!")
    elif 20 <= age < 65:
        print("You adult!")
    elif age <= 65:
        print("You elder!")