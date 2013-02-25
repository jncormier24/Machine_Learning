#!/usr/bin/python

#
# Library
# By: Joe Cormier 
# Description: this contains all the functions needed for assignment 1.

#imports
from sys import argv
import urllib
import urllib2

#
# get_report
# takes in a station id 
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

#
# load_report
# takes in a station and returns that file to the program
#
def load_report( station ):
  file_name = 'station' + station + '.txt'
  local_file = open( file_name, 'r' )
  return local_file

#
# create_report
# handles the report genereation
#
def create_report( station, report ):
  file = 'station' + station + 'new.txt'
  file = open(file, 'w')
  counter = 0
  for line in report:
    if( 0 == counter or 1 == counter or 4 == counter):
      #don't do anything
      counter += 1
      continue
    else:
      if( 3 == counter ):
        #get the location
        name = line[53:].strip( ' \t\n\r' )
        #report.write( name+' name\n' )
        file.write( name+' name\n' )
      if( 5 < counter ):
        #print dates and other fun stuff
        date = clean_date( line[0:6] )
        days = determine_date( date )
        max_temp = fix_temp( line[6:14].strip( ' \t\n\r' ) )
        min_temp = fix_temp( line[14:22].strip( ' \t\n\r' ) )
        if( len( str( max_temp ) ) == 3):
          if( len( str( min_temp ) ) == 3):
            file.write( '| '+date+' |    '+str( max_temp )+' |    '+str( min_temp )+' |\n' )
          if( len( str( min_temp ) ) == 4):
            file.write( '| '+date+' |   '+str( max_temp )+' |   '+str( min_temp )+' |\n' )
          if( len( str( min_temp ) ) == 5):
            file.write( '| '+date+' |  '+str( max_temp )+' |  '+str( min_temp )+' |\n' )
        if( len( str( max_temp ) ) == 4):
          if( len( str( min_temp ) ) == 3):
            file.write( '| '+date+' |    '+str( max_temp )+' |    '+str( min_temp )+' |\n' )
          if( len( str( min_temp ) ) == 4):
            file.write( '| '+date+' |   '+str( max_temp )+' |   '+str( min_temp )+' |\n' )
          if( len( str( min_temp ) ) == 5):
            file.write( '| '+date+' |  '+str( max_temp )+' |  '+str( min_temp )+' |\n' )
        if( len( str( max_temp ) ) == 5):
          if( len( str( min_temp ) ) == 3):
            file.write( '| '+date+' |    '+str( max_temp )+' |    '+str( min_temp )+' |\n' )
          if( len( str( min_temp ) ) == 4):
            file.write( '| '+date+' |   '+str( max_temp )+' |   '+str( min_temp )+' |\n' )
          if( len( str( min_temp ) ) == 5):
            file.write( '| '+date+' |  '+str( max_temp )+' |  '+str( min_temp )+' |\n' )
      file.write( '+----------+--------+--------+--------+----------+\n' )
      counter += 1
  file.close()
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
      temp = temp[0:x] + var + temp[x+1:0]
      temp = convert_temp( temp )
      return temp
    else:
      x += 1

#
# convert_temp
# takes in a temperature and converts it to fehrenheit from celius (if needed)
#
def convert_temp( temp ):
  temp = float( temp )
  if( 'f' == temp_type or 'F' == temp_type or 'fehrenheit' == temp_type or 'Fehrenheit' == temp_type ):
    temp = ( ( 9 * temp ) / 5 ) + 32
    return temp
  if( 'c' == temp_type or 'C' == temp_type or 'celcius' == temp_type or 'Celcius' == temp_type ):
    return temp

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
  
def determine_date( date ):
  date = str( date )
  month = date[0:2]
  year = date[6:]
  year = '19' + year
  year = int( year )
  if( '01' == month or '03' == month or '05' == month or '07' == month or '08' == month or '10' == month or '12' == month):
    days = 31
  elif( '04' == month or '06' == month or '09' == month or '11' == month):
    days = 30
  elif( '02' == month):
    if( 0 == (4 % year) ):
      days = 29
    else:
      days = 28
  return days
