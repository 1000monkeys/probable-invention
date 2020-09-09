if __name__ == "__main__":
    usernames = [
    ]

    if usernames:
        for username in usernames:
            print("Hello! " + username)
            if username == "beheerder":
                print("Do you want a status rapport? \n")
    else:
        print("We should go find some users!")