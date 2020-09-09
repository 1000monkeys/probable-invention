if __name__ == "__main__":
    favorite_fruits = [
        'apple',
        'banana',
        'peach',
        'cherry',
        'tomato'
    ]

    if 'banana' in favorite_fruits:
        print("You are right bananas are great!")

    if 'cherry' not in favorite_fruits:
        print("What is wrong with cherry's?")

    if 'tomato' in favorite_fruits:
        print("Tomatos are juicy!")

    if 'peach' in favorite_fruits and 'apple' in favorite_fruits:
        print("Peaches and apples are great!")

    if 'bread' in favorite_fruits:
        print("Bread is not a fruit!")