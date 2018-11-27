"""
This programme converts csv files to json files
"""


import numpy as np
import csv
import pandas as pd
import json as js


INPUT_CSV = "who_suicide_statistics.csv"
OUTPUT_JSON = "data2.json"

def converter(INPUT_CSV):
    with open(INPUT_CSV) as csvfile:
        data = csv.DictReader(csvfile)

        # main json dictionary
        json_dict = {}

        # list of values needed
        json_dict["Nederland"] = []
        json_dict["Belgie"] = []
        json_dict["Luxemburg"] = []

        year_suicide = []
        suicides = 0

        # iterate over rows of file to extract data needed
        for row in data:
            if row['country'] == 'Netherlands':
                if row['year'] == str(2015):
                    json_dict["Nederland"].append(int(row["suicides_no"]))
            if row['country'] == 'Belgium':
                if row['year'] == str(2015):
                    json_dict["Belgie"].append(int(row["suicides_no"]))
            if row['country'] == 'Luxembourg':
                if row['year'] == str(2015):
                    json_dict["Luxemburg"].append(int(row["suicides_no"]))

    # write the dictionary into the json file
    with open(OUTPUT_JSON, 'w') as output:
        js.dump(json_dict, output)

if __name__ == "__main__":
    converter(INPUT_CSV)
