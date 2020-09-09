if __name__ == "__main__":
    amount = int(input("With how many people would you be dining? "))

    if amount > 8:
        print("You will have to wait till a table has become available.")
    else:
        print("You can be seated right now, Follow me.")