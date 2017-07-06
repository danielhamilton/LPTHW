# import the package
from sys import argv
# run the script and include the name of the input file
# (i.e. python ex20.py test.txt)
script, input_file = argv
# prints the entire test.txt file
def print_all(f):
	print f.read()
# defines rewind function
def rewind(f):
	f.seek(0)
# defines print a line function and prints line count + 
# the line from the txt file
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."
# using the rewind function from above, 
# it opens and seeks the current file (txt file) content
rewind(current_file)

print "Let's print three lines:"

# assigns 1 to current line, then adds 1 for each
# iteration through the lines.
current_line = 1
print_a_line(current_line, current_file),
# will output line 2
current_line = current_line + 1
print_a_line(current_line, current_file),
# will output line 3
current_line = current_line + 1
print_a_line(current_line, current_file)