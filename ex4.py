cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = -drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers/ cars_driven
# ^ These are variables, underscores are used to put an imaginary space
#between words in variable names
#= is making names for things and also helping with later equatins
#add .0 for floating point, not necessary on double digits

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "emtpy cars today."
print "We can transport", carpool_capacity, "People today."
print "We have", passengers, "to carpool today"
print "We need to put about", average_passengers_per_car, "In each car."
