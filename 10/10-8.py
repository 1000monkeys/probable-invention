try:
    with open("cats.txt", 'r') as file_object:
        for line in file_object:
            print(line)

    with open("dogs.txt", 'r') as file_object:
        for line in file_object:
            print(line)

except FileNotFoundError:
    print("File not found/does not exist!")