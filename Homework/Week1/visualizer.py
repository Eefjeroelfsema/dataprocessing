#!/usr/bin/env python
# Name: Eefje Roelfsema
# Student number: 10993673
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt
import statistics as s

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

def imp_csv(file):
    # Global dictionary for the data
    data_dict = {str(key): [] for key in range(START_YEAR, END_YEAR)}

    # open movies.csv file
    with open('movies.csv') as csvfile:
        movies = csv.reader(csvfile)

        # skip the first 2 lines of the file (no information there)
        next(movies)
        next(movies)

        # iterate through all the rows in movies.csv
        for row in movies:

            # find release year of film
            year = str(row[2])

            # find rating of film
            rating = float(row[1])

            # append rating to dictionary of year
            data_dict[year].append(rating)

    # calulate mean of ratings per year
    for year in range(START_YEAR, END_YEAR):
        year= str(year)
        data_dict[year] = s.mean(data_dict[year])

    # define points on x and y-asses
    years = list(data_dict.keys())
    average = list(data_dict.values())

    # plot the points in a line graph
    plt.plot(years, average)

    # name title and asses
    plt.title('IMDB rating of films')
    plt.xlabel('Year of release')
    plt.ylabel('Average rating')
    plt.show()

    return True

if __name__ == "__main__":
    imp_csv(INPUT_CSV)
