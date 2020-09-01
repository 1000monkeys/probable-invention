from random import randint

if __name__ == "__main__":
    announcements = [
        " has 4 legs!",
        " has fur!",
        " walks on all four!",
        " can be a pet."
    ]
    animals = ["Horse", "Dog", "Cat", "Rabbit"]

    for animal in animals:
        print(animal)

    for animal in animals:
        print(animal + announcements[randint(0, len(announcements)) - 1])

    print("All these animals make great pets!")