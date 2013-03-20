#!/usr/bin/python
import library

"""
Load dataset
  Which dataset? 
  How much of the set?
  which test data?
  Load data set, test data, training data into memory

generate a set of predictions for a set of data
	write the base predictor
		always_guess_4_alg
"""

users = {}
movies = {}

while( 1 ):
	print """
	Please select an option: 
	(1) Load a data set,
	(2) Query the data set,
	(3) Run an algorithm,
	Type 'exit' to exit
	"""
	choice = raw_input('> ')

	if( '1' == choice ):
		print 'What is the data set you would like to load?' 
		data_set = raw_input( 'data set >  ' )
		data_set = library.load_data( data_set )
		data_set = open( data_set, 'r' )
		for string in data_set:
		#break the line up 
			line = string.split()
			user = line[0]
			entry = "( %r, %r, %r )" %(line[1], line[2], line[3])
			if user in users:
				users[user].append( entry )
				print "added %r with information %r \n" %( user, users[user] )
			else:
				users[user] = [ entry ]
				print "added %r with information %r \n" %( user, users[user] )
		data_set.close()

	elif( '2' == choice ):
	#query the data set
		print """
		What would you like to do?
		(1) Query a user id,
		(2) Query a movie,
		(3) Show summary
		Type 'none' to go back
		"""
		user_input = raw_input( '> ' )

		if( '1' == user_input ):
			print """
			What user id would you like to Query?
			"""
			what_user = raw_input( '> ' )
			age, sex, job, zipcode = library.load_user( what_user )
			print "The user's age is: %r, they are: %r, they're job is: %r, and they live in: %r." %(age, sex, job, zipcode)
			for line in users:
				print line
			
		elif( '2' == user_input ):
			print """
			What movie would you like to Query?
			"""
			what_movie = raw_input( '> ' )
			
		elif( '3' == user_input ):
			print 'Summary data'

		elif( 'none' == user_input ):
			continue

		else:
			print 'Please pick something from the list'

	elif( '3' == choice ):
	#run an algorithm
		print """
		What is the algorithm you would like to run?
		(1) Euclidean,
		(2) Pearson,
		(3) Tanimoto,
		Type 'none' to go back
		"""
		user_input = raw_input( '> ' )

	else:
		if( 'exit' == choice ):
			exit(0)

		else:
			print 'Please enter a proper choice, stoopid'
