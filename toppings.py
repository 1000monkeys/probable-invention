if __name__ == "__main__":
    requested_topping = 'mushrooms'

    if requested_topping != 'anchovies':
        print("Hold the anchovies!")

    requested_toppings = ['mushrooms', 'extra cheese']

    if 'mushrooms' in requested_topping:
        print("Adding mushrooms.")

    if 'pepperoni' in requested_toppings:
        print("Adding pepperoni.")

    if 'extra cheese' in requested_toppings:
        print("Adding extra cheese.")

    print("\nFinished making your pizza!")