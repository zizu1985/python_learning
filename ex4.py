# Total number of cars
cars = 100
# Single car capacity
space_in_car = 4.0
# Total number of drivers
drivers = 30
# Total number of passengers to transport
passengers = 90
# Number of car which stay in hq
cars_not_driven = cars - drivers
# Number of active car for today
cars_driven = drivers
# Total capacity for active cars
carpool_capacity = cars_driven * space_in_car
# Average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars , "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("Wer can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
