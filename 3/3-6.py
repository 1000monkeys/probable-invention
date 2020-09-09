if __name__ == "__main__":
    guests = ['bjorn', 'nico', 'arjan', 'bert']

    for guest in guests:
        print(guest.title() + " is invited for dinner!")

    print(guests[3] + " cannot come to the dinner party. :(")
    guests[3] = "jan"

    for guest in guests:
        print(guest.title() + " is invited for dinner!")

    print("The table grew more spots! So we are inviting some more people!")
    guests.insert("kjell")
    guests.insert(2, "two face")
    guests.append("Jouri")

    for guest in guests:
        print(guest.title() + " is invited for dinner!")
