if __name__ == "__main__":
    age = int(input("What yous your age? "))

    amount = 0;
    if age < 3:
        amount = 0
    elif 3 < age < 12:
        amount = 10
    elif 12 < age:
        amount = 15

    print("You have to pay " + str(amount) + " for your movie ticket!")