# your code goes here

import sys


def create_ratings_dict():
    file_open = open(sys.argv[1])
    rest_ratings = {}

    for line in file_open:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        rest_ratings[restaurant] = rating

    user_restaurant = raw_input("What restaurant do you want to rate? ")
    user_rating = raw_input("What's your rating for {}? ".format(user_restaurant))

    rest_ratings[user_restaurant] = user_rating

    print

    restaurant_names = sorted(rest_ratings)

    for restaurant in restaurant_names:
        print "{} is rated at {}.".format(restaurant, rest_ratings[restaurant])

    # this works too:
    # for rest, rating in sorted(rest_ratings.items()):
    #     print "{} is rated at {}.".format(rest, rating)

create_ratings_dict()
