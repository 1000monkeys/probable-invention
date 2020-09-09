def make_car(manufacturer, model, **information):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in information.items():
        car[key] = value

    return car


car = make_car("Subaru", "Impreza WXT", color="Blue", rim_size="120 inch")
print(car)
