# using ex19.py to build this one
# define the function for use throughout. whenever boxes is called 
# it will print this statement
def boxes(number_of_boxes, cases_of_boxes):
    print "You have %d boxes!" % number_of_boxes
    print "You have %d cases of boxes!" % cases_of_boxes
    print "You can do a lot with those."

# assign numbers to the arguments and it will print the statement with them included
print "We can just use the numbers like this:"
boxes(20, 200)
print "++++++++++++++"

# assign new variables and apply them to the function
print "Or assign new variables like this:"
boxNo = 40
boxCase = 400
print boxes(boxNo, boxCase)
print "++++++++++++++"

# use those variables and do math 
print "Or do random math:"
boxes(boxNo * 10, boxCase / 40)

print "-+-+-+-+-+-+-+-+-+"

# just play around with different things
print "Let's see what this does:"
print boxNo + 5
print boxNo * boxCase
print boxes(2, 3)
print "Hey, this is a number, too! %r" % boxCase 
print str(boxNo) + " should say 40 and " + str(boxCase) + " should say 400."