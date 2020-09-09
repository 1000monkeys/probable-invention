if __name__ == "__main__":

    print("BEGIN VERSION 1-2 & 3")
    # Version 1-2 & 3
    active = True
    toppings = []
    while active:
        topping = str(input("What kind of topping would you like on your pizza? "))

        if topping == 'quit':
            break

        toppings.append(topping)
        print(topping + " will be added to your pizza!")

    print("These are the toppings on your pizza: ")
    for topping in toppings:
        print(topping)

    print("BEGIN VERSION 2")
    # Version 2
    toppings = []
    while len(toppings) < 3:
        topping = str(input("What kind of topping would you like on your pizza? (You need to select atleast 3) "))

        if topping == 'quit':
            break

        toppings.append(topping)
        print(topping + " will be added to your pizza!")

    print("These are the toppings on your pizza: ")
    for topping in toppings:
        print(topping)