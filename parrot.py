if __name__ == "__main__":
    prompt = "Enter 'quit' to end the program. "
    prompt += "\nTell me something, and i will repeat it back to you: \n"

    active = True
    while active:
        message = input(prompt)

        if message == 'quit':
            active = False
        else:
            print(message)
