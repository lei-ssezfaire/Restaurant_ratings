# your code goes here
import sys
import random


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
		rating = int(rating)
		ratings_dict[name] = rating
		restaurant_names.append(name)
	restaurant_names = sorted(restaurant_names)

	for restaurant in restaurant_names:
		if restaurant in ratings_dict:
			print "{} is rated at {}.".format(restaurant, ratings_dict[restaurant])

	# new_restaurant = raw_input("Enter a new restaurant:\n")

	# while True:

	# 	try:
	# 		new_rating = int(raw_input("Enter restaurant rating from 1-5:\n"))
	# 		break

	# 	except ValueError:
	# 		print "Enter a whole number only."


	# ratings_dict[new_restaurant] = new_rating
	# restaurant_names.append(new_restaurant)
	# restaurant_names = sorted(restaurant_names)

	# for restaurant in restaurant_names:
	# 	if restaurant in ratings_dict:
	# 		print "{} is rated at {}.".format(restaurant, ratings_dict[restaurant])

	user_name = raw_input("Hello, foodie!  What's your name?\n")
	random_restaurant = random.choice(ratings_dict.keys())
	print "Check out {}, it has a rating of {}".format(
		random_restaurant, ratings_dict[restaurant])
	user_submitted_rating = raw_input("Choose a new rating!\n")
	ratings_dict[random_restaurant] = user_submitted_rating

	for restaurant in restaurant_names:
		if restaurant in ratings_dict:
			print "{} is rated at {}.".format(restaurant, ratings_dict[restaurant])


print_ratings(sys.argv[1])



