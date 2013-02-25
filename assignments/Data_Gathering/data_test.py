#!/usr/bin/python2
import library

file = raw_input("Please enter the name of the data file you'd like to read: ")

file = library.load_data( file )

for line in file:
	print line
