"""
This programme converts csv files to json files
"""


import numpy as np
import csv
import pandas as pd
import json as js


INPUT_CSV = "who_suicide_statistics.csv"
OUTPUT_JSON = "data.json"

def converter(INPUT_CSV):
    with open(INPUT_CSV) as csvfile:
        data = csv.DictReader(csvfile)

        # main json dictionary
        json_dict = {}

        # list of values needed
        for year in range(1979,2017):
            json_dict[year] = 0

        year_suicide = []
        suicides = 0

        # iterate over rows of file to extract data needed
        for row in data:
            if row['country'] == 'Netherlands':
                json_dict[int(row['year'])]= json_dict[int(row['year'])] + int(row['suicides_no'])


    # write the dictionary into the json file
    with open(OUTPUT_JSON, 'w') as output:
        js.dump(json_dict, output)

if __name__ == "__main__":
    converter(INPUT_CSV)
