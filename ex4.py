cars = 100
space_in_car = 4
drivers = 30
passenger = 90
cars_not_driven = cars - drivers # hmm interesant, dus als ik iets wil koppelen moet ik het hernoemen in een andere zin zoals #5 en 1
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passenger_per_car = passenger / cars_driven

print("There are", cars, "Cars available.")
print("There are only", drivers, "drivers available")
print("there will be", cars_not_driven, "empty cars")
print("we can transport", carpool_capacity, "people today")
print("we have", passenger, "to carpool")
print("we need to put about", average_passenger_per_car, "in each car")
