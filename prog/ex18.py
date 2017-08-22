def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
def print_two_again(sherman, brady):
	sherman = raw_data(arg1)
	brady = raw_data(arg2)
	print "arg1: %r, arg2: %r" %(sherman, brady)
	
def print_one(arg1):
	print "arg1: %r" %arg1
	
def print_none():
	print "I got nothin'."
	
print_two("Wilbert", "Sible")
print_two_again("Wilbert", "Sible")
print_one("Second")
print_none()