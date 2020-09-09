if __name__ == "__main__":
    vacation_destination = []

    amount_destination = int(input("How many people will be inputting their destination? "))

    counter = 0
    while amount_destination > counter:
        destination = input("What is your dream vacation destination? ")
        vacation_destination.append(destination)
        counter += 1

    for destination in vacation_destination:
        print(destination)