#!/usr/bin/python

#
# Assignment 1
# By: Joe Cormier 
# Description: This program will got vortex.plymouth.edu/climo.html and retrieve a data file that the user will specify
#   The program will then format the data, sererate each month, do a monthly report, and then do a yearly report
#

#imports
from sys import argv
import urllib
import urllib2

#Prompt for filename
station = raw_input('Please enter a station ID: ')

#Ask user for Fehrenheit or Celecius
temp_type = raw_input('Would you like (F)ehrenheit or (C)elcius: ')

#
#	get_report
#	takes in a station id 
# returns the response page
#
def get_report(station):
	url = "http://vortex.plymouth.edu/cgi-bin/retrieve.cgi"
	data = {}
	data[ 'ident' ] = station
	data = urllib.urlencode(data)
	url = url + '?' + data
	response = urllib2.urlopen(url)
	the_page = response.read()
	return the_page

#
# save_report
# takes in a report and station number and saves the report to a text file
#
def save_report(station, report):
	file = 'station'+station+'.txt'
	local_file = open(file, 'w')
	local_file.write(report)
	local_file.close()
	#with local_file as open(file, 'w'):
		#local_file.write(

#
# load_report
# takes in a station and returns that file to the program
#
def load_report( station ):
	file_name = 'station' + station + '.txt'
	local_file = open( file_name, 'r+' )
	return local_file

#
# create_report
# handles the report genereation
#
def create_report( report ):
	counter = 0
	for line in report:
		if( 0 == counter or 1 == counter or 4 == counter):
			counter += 1
			continue
		else:
			if( 3 == counter ):
				name = line[53:].strip( ' \t\n\r' )
				print name+' name'
				print '+----------+--------+--------+--------+----------+'
			date = clean_date( line[0:6] )
			max_temp = fix_temp( line[6:14].strip( ' \t\n\r' ) )
			min_temp = fix_temp( line[14:22].strip( ' \t\n\r' ) )
			#max_temp = line[6:14].strip( ' \t\n\r' )
			#min_temp = line[14:22].strip( ' \t\n\r ')
			print '|'+date+'|'+max_temp+'|'+min_temp+'|'
			print '+----------+--------+--------+--------+----------+'
			counter += 1
	report.close()

#
# fix_temp
# takes in a temperature and formats correctly
#
def fix_temp( temp ):
	x = 0
	y = '.'
	for var in temp:
		if( ' ' == var ):
			var = y
			temp = temp[0:x] + var + temp[x+1]
			return temp
		x += 1

#
# convert_temp
# takes in a temperature and converts it to fehrenheit from celius (if needed)
#
def convert_temp( temp ):
	if( 'f' == temp_type or 'F' == temp_type or 'fehrenheit' == temp_type or 'Fehrenheit' == temp_type ):
		pass
	if( 'c' == temp_type or 'C' == temp_type or 'celcius' == temp_type or 'Celcius' == temp_type ):
		pass

#
# clean_date
# takes in an unformated date and formats it to mm/dd/yy
#
def clean_date( date ):
	if len(date) != 6:
		print 'Date has incorrect amount of numbers';
		exit(0)
	else:
		#split the date into 3 parts and switch them into the proper order
		first = date[0:2]
		second = date[2:4]
		third = date[4:6]
		date = second+'-'+third+'-'+first
	return date
	
report = get_report( station )
print 'report gotten'
save_report( station, report )
print 'report saved'
local_report = load_report( station )
print 'local loaded'
report = create_report( local_report )
