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
import library

#Prompt for filename
station = raw_input('Please enter a station ID: ')

#Ask user for Fehrenheit or Celecius
temp_type = raw_input('Would you like (F)ehrenheit or (C)elcius: ')

report = library.get_report( station )
print 'report gotten'
library.save_report( station, report )
print 'report saved'
local_report = library.load_report( station )
print 'local loaded'
library.create_report( station, local_report )