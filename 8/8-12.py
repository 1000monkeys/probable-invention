def make_sandwich(bread_name, *toppings):
    print("Making a " + bread_name + " with: ")

    for topping in toppings:
        print("- " + topping)

make_sandwich("Italian herb and cheeses", "Tomato", "Lettuce", "Chicken")
make_sandwich("Brown bread", "Meatball", "Paprika")
make_sandwich("Tosti bread", "Cheese", "Ham", "Mayo", "Curry")
