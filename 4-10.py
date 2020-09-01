if __name__ == "__main__":
    numbers = [value ** 3 for value in range(0, 11, 2)]
    for number in numbers:
        print(number)

    print("The first three items in the list are: ")
    print(numbers[:3])
    print("Three items from the middle of the list are: ")
    print(numbers[2:5])
    print("The last three items in the list are: ")
    print(numbers[-3:])