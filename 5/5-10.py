if __name__ == "__main__":
    current_users = [
        'beheerder',
        'kjevo',
        'user345',
        'user89',
        'user092'
    ]

    new_users = [
        'kjevo',
        'user89'
    ]

    for username in new_users:
        if username.lower() in current_users:
            print("Your username " + username + " is already in use! Pick another one!")