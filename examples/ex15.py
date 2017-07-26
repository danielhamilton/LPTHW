#imports the argv feature from the sys package
from sys import argv

#the format for this is run the script name and the filename
script, filename = argv

#opens the filename we specify above
txt = open(filename)

#prints message with filename, then content of the txt file    
print "Here's your file %r:" % filename
print txt.read()

#enter the name again
#print "Type the filename again: "
file_again = raw_input("Enter the filename again > ")

#open the file again   
txt_again = open(file_again)

#print the content of the txt again
print txt_again.read()