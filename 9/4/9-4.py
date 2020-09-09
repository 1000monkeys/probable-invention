from restaurant import Restaurant

restaurant = Restaurant("Denny's", "Hotdogs!")

print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)
restaurant.increment_number_served(75)
print(restaurant.number_served)
