if __name__ == "__main__":
    sandwich_orders = ['BLT', 'Meatball', 'Spicy italian']
    finished_sandwiches = []

    while len(sandwich_orders) > 0:
        sandwich = sandwich_orders.pop()
        print("I made your " + sandwich + " sandwich!")
        finished_sandwiches.append(sandwich)

    print("Finished sandwiches: ")
    for sandwich in finished_sandwiches:
        print(sandwich)
