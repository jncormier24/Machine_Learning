#!/usr/bin/python
import random
from math import sqrt
from math import fabs

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

"""
pearson
parameters: prefs, person1, person2
returns: score
"""
def pearson( prefs, person1, person2 ):
	#get the list of mutally rated items
	similar = {}
	p1 = prefs[person1]
	p2 = prefs[person2]
	for item in p1:
		if item in p2:
			similar[item] = 1
	
	#find the number of elements
	common = len( similar )
	
	#if there are no ratings in common, return 0
	if common == 0:
		return 0
		
	#add up all the preferences
	sum1 = sum( [p1[it] for it in simliar] )
	sum2 = sum( [p2[it] for it in simliar] )
	
	#sum up the squares
	sum1Sq = sum( [pow( p1[it], 2 ) for it in simliar] )
	sum2Sq = sum( [pow( p2[it], 2 ) for it in simliar] )
	
	#sum up the products
	pSum = sum( [p1[it] * p2[it] for it in simliar] )
	
	#calculate pearson score
	num = pSum - ( [sum1 * sum2] / common )
	den = sqrt( ( sum1Sq - pow( sum1, 2 ) / common ) * ( sum2Sq - pow( sum2, 2 ) / common ))
	if den == 0:
		return 0
	
	score = num / den
	
	return score
	
"""
pearson_modified
parameters: person1, person2
returns: score
"""
def pearson_modified( p1, p2 ):
	#get the list of mutally rated items
	
	similar = {}

	for item in p1:
		if item in p2:
			similar[item] = 1
	
	#find the number of elements
	common = len( similar )
	
	#if there are no ratings in common, return 0
	if common == 0:
		return 0
		
	#add up all the preferences
	sum1 = sum( [p1[it] for it in similar] )
	sum2 = sum( [p2[it] for it in similar] )
	
	#sum up the squares
	sum1Sq = sum( [pow( p1[it], 2 ) for it in similar] )
	sum2Sq = sum( [pow( p2[it], 2 ) for it in similar] )
	
	#sum up the products
	pSum = sum( [p1[it] * p2[it] for it in similar] )
	
	#calculate pearson score
	num = pSum - ( (sum1 * sum2) / common )
	den = sqrt( ( sum1Sq - pow( sum1, 2 ) / common ) * ( sum2Sq - pow( sum2, 2 ) / common ))
	if den == 0:
		return 0
	
	score = num / den
	
	print score
	return score

"""
euclidean
parameters:
returns:
"""
def euclidean( prefs, person1, person2 ):
	#get the list of shared items
	similar = {}
	p1 = prefs[person1]
	p2 = prefs[person2]
	
	for item in p1:
		if item in p2:
			similar[item] = 1
	
	#if they have no ratings in common, return 0
	if len( similar ) == 0: 
		return 0
	
	#Add up the squares of all the differences
	sum_of_sq = sum( [pow( p1[item] - p2[item] , 2 ) for item in p1 if item in p2])
	
	return 1/( 1 + sum_of_sq )
"""
euclidean_modified
parameters: p1, p2
returns:
"""
def euclidean_modified( p1, p2 ):
	#get the list of shared items
	similar = {}
	
	for item in p1:
		if item in p2:
			similar[item] = 1
	
	#if they have no ratings in common, return 0
	if len( similar ) == 0: 
		return 0
	
	#Add up the squares of all the differences
	sum_of_sq = sum( [pow( p1[item] - p2[item] , 2 ) for item in p1 if item in p2])
	
	score = 1/( 1 + sum_of_sq )
	return score
	
"""
kcluster
parameters: distance=euclidean_modified, k=4
returns: dictionary of clusters and list of centroids
"""
def kcluster( users, movies, k=10, distance = euclidean_modified ):
	ranges = 960
	clusters = []
	
	#create k randomly placed centroids
	for j in range(k):
		centroid = {}
		for i in range( ranges ):
			x = random.random() * 4.0 + 1
			l = str( i )
			centroid.update( {  l : x } )
		clusters.append( centroid )

	lastmatch = None
	for t in range( 100 ):
		print "Iteration %d " % t
		bestmatches = [[] for i in range(k)]

		#find which centroid is the closest for each thing
		bestmatch = 0
		for j in range( ranges ):
			try:
				movie = movies[ str(j) ]
				bestmatch = 0
				for i in range(k):
					d = fabs( distance( clusters[i], movie ) )
					nd = fabs( distance( clusters[bestmatch], movie ) )
					if( d < nd ):
						bestmatch = i
				bestmatches[bestmatch].append(j)
			except KeyError:
				continue
		
		#If the results are the same as last time, this is complete
		if bestmatches == lastmatch:
			break
		lastmatch = bestmatches
				
		#Move the centroids to the average of their members
		for i in range( k ):
			avgs = [0.0] * len( users )
			if 0 < len( bestmatches[i] ):
				try:
					for movie in bestmatches[i]:
						for m in range(len(movies[movie])):
							avgs[m] += movies[movie][m]
					for j in range( len( avgs ) ):
						avgs[j] /= len(bestmatches[i])
					clusters[i] = avgs
				except KeyError:
					continue

	return bestmatches

"""
print_movies
parameters: movies
prints movies to a file
"""
def print_movies( clusters ):
	i = 0
	movie_ids = {}
	data = '../ml-100k/u.item' 
	data = open( data, 'r' )
	file = open( 'Movie_Data.txt', 'w' )
	
	for line in data:
		line = line.split( '|' )
		movie_id = line[0]
		movie_name = line[1].split( '(' )
		movie_ids.update( { movie_id : movie_name[0] } )
	
	for cluster in clusters:
		for movie in cluster:
			if movie in movie_ids:
				
	
	
	file.close()
	data.close()

"""
always_guess_four
parameters: none
exactly what it says
"""
def always_guess_four():
	return 4

"""
movie_avg
parameters: movie
calc the average for that movie, and guess that every time.
"""			
def movie_avg( movie ):
	for k in range( len( movie ) ):
		rating += movie[k][1]
		
	return rating/len( movie )

"""
user_avg
parameters: user
calc the average for that user, and guess that every time.
"""	
def user_avg( user ):
	for k in range( len( user ) ):
		rating += user[k][1]
		
	return rating/len( user )

"""
calc_og
parameters: user and movie:
	guess = x + M_n + U_m
	x = overall avg rating in data
	M_0 = avg for movie n rating - x
	U_0 = avg user rating m - x
"""	
def calc_og( user, movie ):
	movie_avg = 0.0
	user_avg = 0.0
	guess = 0.0
	for k in range( len( movies[movie] ) ):
		movie_avg += movies[movie][k]
	
	for j in range( len( users[user] ) ):
		user_avg += users[user][j]
	
	movie_avg = movie_avg / len( movies[movie] )
	user_avg = user_avg / len( users[user] )
	
	guess = movie_avg + user_avg 
	
	return guess
	