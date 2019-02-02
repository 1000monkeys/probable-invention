if __name__ == "__main__":
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']

    # Lijsten started op 0, zoals gewoonlijk bij de meeste programmeertalen
    print(bicycles[0])
    print(bicycles[0].title())

    print(bicycles[1])  # 1e item in de lijst
    print(bicycles[3])  # 2e item in de lijst

    print(bicycles[-1])

    message = "My first bicycle was a " + bicycles[0].title() + "."
    print(message)

    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles[0] = "ducati"
    print(motorcycles)

    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles.append("ducati")
    print(motorcycles)

    motorcycles = []
    motorcycles.append("honda")
    motorcycles.append("yamaha")
    motorcycles.append("suzuki")
    print(motorcycles)

    motorcycles.insert(0, "ducati")
    print(motorcycles)

    del motorcycles[0]
    print(motorcycles)

    popped_motorcycle = motorcycles.pop()
    print(motorcycles)
    print(popped_motorcycle)

    last_owned = motorcycles.pop()
    print("The last motorcycle i owned was a " + last_owned.title() + ".")

    first_owned = motorcycles.pop(0)
    print("The first motorcycle i owned was a " + first_owned.title() + ".")

    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles.remove("honda")
    print(motorcycles)

    too_expensive = 'suzuki'
    motorcycles.remove(too_expensive)
    print(motorcycles)
    print("\nA " + too_expensive.title() + " is too expensive for me.")
