try:
    with open('PrideAndPrejudice.txt', 'r', encoding="utf8") as file_object:
        contents = file_object.read()
        print("Pride: " + str(contents.lower().count("pride")))
        print("Prejudice: " + str(contents.lower().count("prejudice")))
        print("The: " + str(contents.lower().count("the")))

except FileNotFoundError as err:
    print(err)
