def make_shirt(size="Large", message="I love Python."):
    print("Making a shirt with size: " + size)
    print("Message: " + message + "\n")


if __name__ == "__main__":
    make_shirt()
    make_shirt("Small")
    make_shirt("Medium", "I hate Python.")
