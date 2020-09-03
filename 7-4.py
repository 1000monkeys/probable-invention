if __name__ == "__main__":
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