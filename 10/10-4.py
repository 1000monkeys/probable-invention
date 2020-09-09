while True:
    name = input("What is your name? ")
    with open("guest_book.txt", 'a') as file_object:
        file_object.write(name + "\n")