if __name__ == "__main__":
    guests = ['bjorn', 'nico', 'arjan', 'bert']

    for guest in guests:
        print(guest.title() + " is invited for dinner!")

    print(guests[3] + " cannot come to the dinner party. :(")
    guests[3] = "jan"

    for guest in guests:
        print(guest.title() + " is invited for dinner!")
