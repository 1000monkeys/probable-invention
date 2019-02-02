if __name__ == "__main__":
    guests = ['bjorn', 'nico', 'arjan', 'bert']

    for guest in guests:
        print(guest.title() + " is invited for dinner!")

    print(guests[3] + " cannot come to the dinner party. :(")
    guests[3] = "jan"

    for guest in guests:
        print(guest.title() + " is invited for dinner!")

    print("The table grew more spots! So we are inviting some more people!")
    guests.insert(0, "kjell")
    guests.insert(2, "two face")
    guests.append("Jouri")

    for guest in guests:
        print(guest.title() + " is invited for dinner!")

    while len(guests) > 2:
        removed_guest = guests.pop()
        print(removed_guest + " cannot come to the dinner! :(")

    for guest in guests:
        print(guest + " is still invited! :)")

    del guests[1]
    del guests[0]
    print(guests)
