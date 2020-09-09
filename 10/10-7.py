while True:
    number_one = input("Number 1: ")
    number_two = input("Number 2: ")

    try:
        answer = int(number_one) + int(number_two)
        print(answer)
    except (TypeError, ValueError):
        print("Please input a number!!")
