# this defines the function with 2 arguments. they can really be anything
# as long as it's consistent. 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# this example shows how 20 and 30 are applied to cheese_count and 
# boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this assigns values to the new variables, but then uses the function
# to assign the new variables to the function cheese_and_crackers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# you can do math inside the function too, just make sure you have 
# both arg represented
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# you can apply the new variables and add things to them, too
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)