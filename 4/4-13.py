if __name__ == "__main__":
    dishes = (
        "Stampot hutspot",
        "Boerenkool",
        "Patat speciaal",
        "Hot dog",
        "Pizza"
    )

    for dish in dishes:
        print(dish)

    # Can't change a tupel
    # dishes[0] = "Poop"

    dishes = (
        dishes[0],
        dishes[1],
        dishes[2],
        "Salad",
        "Apple"
    )

    for dish in dishes:
        print(dish)