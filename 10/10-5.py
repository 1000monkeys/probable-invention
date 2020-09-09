while True:
    reason = input("Why do you like programming? ")
    with open("programming.txt", 'a') as file_object:
        file_object.write(reason + "\n")