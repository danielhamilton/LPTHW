from sys import argv
# remember when launching. need the name of the script + the other filename to open
script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, press CTRL-C(^C)."
print "If you do want that, press RETURN."

raw_input("?")

# pressing return will open the filename in WRITE mode, 
# erase it, and ask for 3 lines of text to replace what is being erased
print "Opening the file..."
#define the variable named target, assign it to open whatever filename
#user specifies and opens it in WRITE mode to erase it
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# writes new lines to the text file and replaces the old one
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()