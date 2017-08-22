from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)
# we coule do these two on one line too, how?

in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long"%len(indata)

print 
