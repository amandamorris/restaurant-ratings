# your code goes here

import sys
import random


def create_ratings_dict():
    """Reads file and makes dictionary from contents."""

    file_open = open(sys.argv[1])
    rest_ratings = {}

    for line in file_open:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        rest_ratings[restaurant] = rating
    return rest_ratings


def add_user_rating(rest_ratings):
    """Prompts user for rating and adds to dictionary."""

    user_restaurant = raw_input("What restaurant do you want to rate? ")
    user_restaurant = user_restaurant[0].upper() + user_restaurant[1:]
    user_rating = raw_input("What's your rating for {}? ".format(user_restaurant))

    rest_ratings[user_restaurant] = user_rating


def print_sorted_reviews(rest_ratings):
    """Sorts and prints reviews."""

    restaurant_names = sorted(rest_ratings)

    for restaurant in restaurant_names:
        print "{} is rated at {}.".format(restaurant, rest_ratings[restaurant])

    # this works too:
    # for rest, rating in sorted(rest_ratings.items()):
    #     print "{} is rated at {}.".format(rest, rating)


def update_random_rest_rating(rest_ratings):
    """Chooses random restaurant and prompts user for new rating."""

    rand_rest = random.choice(sorted(rest_ratings))
    rand_rating = raw_input("What is your rating for {}? ".format(rand_rest))

    rest_ratings[rand_rest] = rand_rating


def perform_user_choice():
    """Prompts user to choose between data visualization, data append, and quit."""

    rest_ratings = create_ratings_dict()
    while True:
        print
        user_choice = raw_input("Press 1 to see all ratings, press 2 to modify ratings, and press q to quit: ")
        print
        if user_choice == "1":
            print_sorted_reviews(rest_ratings)
        elif user_choice == "2":
            user_choice2 = raw_input("Press 1 to add a new rating, press 2 to update a random rating: ")
            print
            if user_choice2 == "1":
                add_user_rating(rest_ratings)
            elif user_choice2 == "2":
                update_random_rest_rating(rest_ratings)
            else:
                print "Please press 1 or 2."
        elif user_choice == "q":
            return
        else:
            print "Please press 1, 2, or q."


perform_user_choice()
