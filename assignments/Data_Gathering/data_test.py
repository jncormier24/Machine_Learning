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
			movie = line[1]
			rating = float( line[2] )
			time = line[3]
			if user in users:
				users[ user ].update( { movie : rating } )
			else:
				users[ user ] = { movie : rating }
			if movie in movies:
				movies[ movie ].update( { user: rating } )
			else:
				movies[ movie ] = { user: rating }

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
			print "User %r has rated: \n" %( what_user)
			print users[ what_user ]

		elif( '2' == user_input ):
			print """
			What movie would you like to Query?
			"""
			what_movie = raw_input( '> ' )
			print "Movie %r has ratings: \n" %( what_movie )
			print movies[ what_movie ]

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
		(3) K Cluster,
		(4) RMSE, 
		Type 'none' to go back
		"""
		user_input = raw_input( '> ' )
		
		if( '1' == user_input ):
			person1 = raw_input( "Please enter person 1: " )
			person2 = raw_input( "Please enter person 2: " )
			print "The euclidean score is: %r\n" % library.euclidean( users, person1, person2 )
			
		elif( '2' == user_input ):
			person1 = raw_input( "Please enter person 1: " )
			person2 = raw_input( "Please enter person 2: " )
			print "The pearson score is: %r\n" % library.pearson( users, person1, person2 )
		elif( '3' == user_input ):
			matches = library.kcluster( movies )
			for match in matches:
				print match
		elif( '4' == user_input ):
			continue
		else:
			continue

	else:
		if( 'exit' == choice ):
			exit(0)

		else:
			print 'Please enter a proper choice, stoopid'
