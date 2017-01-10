# your code goes here

import sys


def create_ratings_dict():
    file_open = open(sys.argv[1])
    rest_ratings = {}

    for line in file_open:
        line = line.rstrip()
        token = line.split(":")
        rest_ratings[token[0]] = token[1]
    for restaurant in sorted(rest_ratings):
        print "{} is rated at {}.".format(restaurant, rest_ratings[restaurant])

    # this works too:
    # for rest, rating in sorted(rest_ratings.items()):
    #     print "{} is rated at {}.".format(rest, rating)

create_ratings_dict()
