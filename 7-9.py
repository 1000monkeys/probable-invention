if __name__ == "__main__":
    sandwich_orders = ['BLT', 'Pastrami', 'Meatball', 'Pastrami', 'Spicy italian', 'Pastrami']
    finished_sandwiches = []

    print("We are out of pastrami!")
    while 'Pastrami' in sandwich_orders:
        sandwich_orders.remove('Pastrami')

    while len(sandwich_orders) > 0:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich + " sandwich!")
        finished_sandwiches.append(sandwich)

    print("Finished sandwiches: ")
    for sandwich in finished_sandwiches:
        print(sandwich)
