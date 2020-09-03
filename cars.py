if __name__ == "__main__":
    cars = ['bmw', 'audi', 'toyoto', 'subaru']

    print(cars)
    cars.sort()
    print(cars)

    cars.sort(reverse=True)
    print(cars)

    cars = ['bmw', 'audi', 'toyoto', 'subaru']
    print("Here is the original list:")
    print(cars)
    print("\nHere is the sorted list:")
    print(sorted(cars))
    print("\nHere is the original list again:")
    print(cars)

    cars.reverse()
    print(cars)

    print(len(cars))

    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())