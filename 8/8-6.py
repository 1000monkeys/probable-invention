def city_country(city="Groningen", country="Netherlands"):
    return city.title() + ", " + country.title()


print(city_country())
print(city_country("Emmen"))
print(city_country("Berlin", "Germany"))