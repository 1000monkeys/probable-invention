if __name__ == "__main__":
    numbers =  list(range(1, 11))

    for number in numbers:
        if number == 1:
            text = str(number) + "st"
        elif number == 2:
            text = str(number) + "nd"
        elif number == 3:
            text = str(number) + "rd"
        else:
            text = str(number) + "th"

        print(text)