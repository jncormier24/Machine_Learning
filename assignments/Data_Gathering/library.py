#!/usr/bin/python

"""
Load dataset
  Which dataset? 
  How much of the set?
  which test data?
  Load data set, test data, training data into memory
"""

"""
load_data
parameters: data
returns: requested data set
"""
def load_data( data ):
	location = '../ml-100k/'
	file = location + data
	return file

"""
load_user
parameters: user id
returns: user information
"""
def load_user( uid ):
	fopen = '../ml-100k/u.user'
	users = open( fopen, 'r' )
	for user1 in users:
		user2 = user1.split('|')
		if( uid == user1[0] ):
			return user2[1], user2[2], user2[3], user2[4]
