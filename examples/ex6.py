# make initial statement
x = "There are %d types of people." % 10
# assign the strings to the variables
binary = "binary"
do_not = "don't"
# put those strings into statements using the variables. 
y = "Those who know %s and those who %s." % (binary, do_not)

# print the statements
print x
print y 

# print out that I said those things above
print "I said %r." % x
print "I also said: '%s'." % y

# not funny
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the joke question and the answer assigned to the varible hilarious
print joke_evaluation % hilarious

# variables with two sides, concatenated in the print statement below
w = "This is the left side of..."
e = "a string with a right side."

print w + e