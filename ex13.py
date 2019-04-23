#Import = add features to script from python feature set
#argv is the argument variable = holds the arguments you pass
#to your python script when you run it
from sys import argv
#Unpacks argv- assigns to four variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#feature-Modules make python program do more/ give you features
#You create the 3 variables for the script to run if not error
#will occurr
age = raw_input("how old are you?" )
