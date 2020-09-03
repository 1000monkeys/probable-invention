if __name__ == "__main__":
    banned_users = ['andrem', 'carolina', 'david']
    user = 'marie'

    if user not in banned_users:
        print(user.title() + ", you can post a response if you wish.")