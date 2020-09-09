if __name__ == "__main__":
    car = "subaru"
    house = 300001
    kids = True
    job = False
    stable = True
    hourly_wage = 18.86

    print("Is car == subaru? I predict True")
    print(car == 'subaru')

    print("Is house above 300000? I predict True")
    print(house > 300000)

    print("Is kids and stable True? I predict True")
    print(kids and stable)

    print("Is stable True? I predict True")
    print(stable)

    print("Is hourly wage above 15.00? I predict True")
    print(hourly_wage > 15.00)

    print("Is car capitalized? I predict False")
    print(car == "Subaru")

    print("Is house below 200000 and job True? I predict False")
    print(house < 200000 and job)

    print("Is job false? I predict False")
    print(job is not False)

    print("Is job true and hourly wage above 10? I predict False")
    print(job is not False and hourly_wage > 10)

    print("Is kids false and hourly wage below 5? I predict False")
    print(kids is False and hourly_wage > 5)
