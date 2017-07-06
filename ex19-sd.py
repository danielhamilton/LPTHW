#using ex19.py to build this one
def boxes(number_of_boxes, cases_of_boxes):
    print "You have %d boxes!" % number_of_boxes
    print "You have %d cases of boxes!" % cases_of_boxes
    print "You can do a lot with those."

print "We can just use the numbers like this:"
boxes(20, 200)
print "++++++++++++++"

print "Or assign new variables like this:"
boxNo = 40
boxCase = 400
print boxes(boxNo, boxCase)
print "++++++++++++++"

print "Or do random math:"
boxes(boxNo * 10, boxCase / 40)

print "-+-+-+-+-+-+-+-+-+"

print "Let's see what this does:"
print boxNo + 5
print boxNo * boxCase
print boxes(2, 3)
print "Hey, this is a number, too! %r" % boxCase 
print str(boxNo) + " should say 40 and " + str(boxCase) + " should say 400."