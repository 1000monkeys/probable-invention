from random import randint

if __name__ == "__main__":
    pizzas = ["Salami", "Vier Kazen", "Pepperoni"]
    friend_pizzas = pizzas[:]

    pizzas.append("Hawai")
    friend_pizzas.append("Ham and bacon")

    for pizza in pizzas:
        print("My favorite pizzas are: " + pizza)

    for pizza in friend_pizzas:
        print("My friends favorite pizzas are: " + pizza)

