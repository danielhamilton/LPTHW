# practice, starting with escape characters, look for \
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
# poem with tabs and newlines for formatting
poem = """
\tThe Lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# formats output of poem
print "--------------------"
print poem
print "--------------------"

# prove it's working
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# defines function with started argument to set initial values
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
# sets variable and value, assigns secret formula to beans, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# changes variable value to new amount
start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

print secret_formula(2)
print secret_formula(10)
print secret_formula(start_point)
print """    

HH   HH        lll lll        
HH   HH   eee  lll lll  oooo  
HHHHHHH ee   e lll lll oo  oo 
HH   HH eeeee  lll lll oo  oo 
HH   HH  eeeee lll lll  oooo  


#     #                             
#     # ###### #      #       ####  
#     # #      #      #      #    # 
####### #####  #      #      #    # 
#     # #      #      #      #    # 
#     # #      #      #      #    # 
#     # ###### ###### ######  ####  

                                  
"""

