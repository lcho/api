from sys import argv

script, input_file = argv

def print_all(solar):
	print solar.read()
	
def rewind(solar):
	solar.seek(0)
	
def print_a_line(line_count, solar):
	print line_count, solar.readline(),
	
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

rewind(current_file)

print "\nPrint it one more time."

current_line = 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

current_line += 1
print_a_line (current_line, current_file)

