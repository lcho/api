from sys import argv; script, from_file, to_file = argv; in_file = open(from_file); raw_input(); out_file = open(to_file,"w"); out_file.write(from_file)