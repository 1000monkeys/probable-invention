from random import randint

if __name__ == "__main__":
    announcement = ["I love the cheesy ", "I can always go for a ", "Wake me up for a "]
    pizzas = ["Salami", "Vier Kazen", "Pepperoni"]

    for pizza in pizzas:
        print(announcement[randint(0, len(announcement)) - 1] + pizza + ".")

    print("Pizza is the best thing since sliced bread. Actually it is even better! It's crunchy bread, I love pizza so much.")