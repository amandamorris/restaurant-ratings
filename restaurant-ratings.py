# your code goes here

import sys


def create_ratings_dict():
    file_open = open(sys.argv[1])
    rest_ratings = {}

    for line in file_open:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        rest_ratings[restaurant] = rating
    return rest_ratings


def add_user_rating(rest_ratings):
    user_restaurant = raw_input("What restaurant do you want to rate? ")
    user_rating = raw_input("What's your rating for {}? ".format(user_restaurant))

    rest_ratings[user_restaurant] = user_rating


def print_sorted_reviews(rest_ratings):
    restaurant_names = sorted(rest_ratings)

    for restaurant in restaurant_names:
        print "{} is rated at {}.".format(restaurant, rest_ratings[restaurant])

    # this works too:
    # for rest, rating in sorted(rest_ratings.items()):
    #     print "{} is rated at {}.".format(rest, rating)


def perform_user_choice():
    rest_ratings = create_ratings_dict()
    while True:
        print
        user_choice = raw_input("Press 1 to see all ratings, press 2 add a new rating, press q to quit: ")
        print
        if user_choice == "1":
            print_sorted_reviews(rest_ratings)
        elif user_choice == "2":
            add_user_rating(rest_ratings)
        elif user_choice == "q":
            return
        else:
            print "Please press 1, 2, or q."

perform_user_choice()
