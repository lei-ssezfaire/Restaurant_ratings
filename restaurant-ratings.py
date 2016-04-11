# your code goes here
import sys

def print_ratings(file_name):
	""" Takes data file and prints ratings """
	
	try: 
		restaurant_data = open(file_name)
	except: 
		print "Not a valid file."
		sys.exit(1)
	ratings_dict = {}
	restaurant_names = []
	for line in restaurant_data:
		line = line.rstrip()
		name, rating = line.split(":")
		ratings_dict[name] = rating
		restaurant_names.append(name)
	restaurant_names = sorted(restaurant_names)
	for restaurant in restaurant_names:
		if restaurant in ratings_dict:
			print "{} is rated at {}.".format(restaurant, ratings_dict[restaurant])

print_ratings(sys.argv[1])



