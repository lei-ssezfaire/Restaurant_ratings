# your code goes here
import sys

def print_ratings(file_name):
	try: 
		restaurant_data = open(file_name)
	except: 
		print "Not a valid file."
		sys.exit(1)
	ratings_dict = {}
	restaurant_names = []
	for line in restaurant_data:
		line = line.rstrip()
		line_data = line.split(":")
		ratings_dict[line_data[0]] = line_data[1]
		restaurant_names.append(line_data[0])
	restaurant_names = sorted(restaurant_names)
	for restaurant in restaurant_names:
		if restaurant in ratings_dict:
			print "{} is rated at {}.".format(restaurant, ratings_dict[restaurant])

print_ratings(sys.argv[1])



