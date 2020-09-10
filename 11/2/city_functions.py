def city_country_population(city, country, population=""):
    if population:
        return city.title() + ", " + country.title() + " - population " + str(population)
    else:
        return city.title() + ", " + country.title()