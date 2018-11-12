#!/usr/bin/env python
# Name: Eefje Roelfsema
# Student number: 10993673

"""
This script scrapes IMDB and outputs a CSV file with highest rated movies.
"""
import csv
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup

TARGET_URL = "https://www.imdb.com/search/title?title_type=feature&release_date=2008-01-01,2018-01-01&num_votes=5000,&sort=user_rating,desc"
BACKUP_HTML = 'movies.html'
OUTPUT_CSV = 'movies.csv'


def extract_movies(dom):
    """
    Extract a list of highest rated movies from DOM (of IMDB page).
    Each movie entry should contain the following fields:
    - Title
    - Rating
    - Year of release (only a number!)
    - Actors/actresses (comma separated if more than one)
    - Runtime (only a number!)
    """

    # make lists for all film information needed
    title = []
    rating = []
    year = []
    runtime = []
    actors = []

    # put the film information in films
    films = dom.findAll("div", {"class": "lister-item-content"})

    # iterate through all the films
    for i in range(len(films)):

        # append all information to it's specific list
        title.append(films[i].h3.a.string)
        rating.append(films[i].div.div.strong.string)
        year.append(films[i].h3.findAll("span", {"class": "lister-item-year text-muted unbold"})[0].string.strip("I ()"))
        runtime.append(films[i].p.findAll("span", {"class": "runtime"})[0].text)

        # make new list of for actor
        actor = []

        a = films[i].findAll("a")

        # iterate through all the actors in the specific film and add to list
        for person in a:
            if "_st_" in person['href']:
                actor.append(person.string)

        # remove the brackets
        actor = ', '.join(actor)

        # add list of actors to list of actors
        actors.append(actor)

    return [title,rating,year,actors,runtime]


def save_csv(outfile, movies):
    """
    Output a CSV file containing highest rated movies.
    """
    writer = csv.writer(outfile)

    # sort columns
    writer.writerow(['sep=,'])

    # write first line
    writer.writerow(['Title', 'Rating', 'Year', 'Actors', 'Runtime'])

    # write information into csv file
    for i in range(len(movies[0])):
        writer.writerow([movies[0][i],movies[1][i],movies[2][i],movies[3][i], movies[4][i]])


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('The following error occurred during HTTP GET request to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":

    # get HTML content at target URL
    html = simple_get(TARGET_URL)

    # save a copy to disk in the current directory, this serves as an backup
    # of the original HTML, will be used in grading.
    with open(BACKUP_HTML, 'wb') as f:
        f.write(html)

    # parse the HTML file into a DOM representation
    dom = BeautifulSoup(html, 'html.parser')

    # extract the movies (using the function you implemented)
    movies = extract_movies(dom)


    # write the CSV file to disk (including a header)
    with open(OUTPUT_CSV, 'w', newline='') as output_file:
        save_csv(output_file, movies)
