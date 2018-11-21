"""
This programme converts csv files to json files
"""


import numpy as np
import csv
import pandas as pd
import json as js


INPUT_CSV = "labor-force-participation-rate-black-or-african-american.csv"
OUTPUT_JSON = "data.json"

def converter(INPUT_CSV):
    with open(INPUT_CSV) as csvfile:
        data = csv.DictReader(csvfile)

        # main json dictionary
        json_dict = {}

        # list of values needed
        value = []
        date = []

        # iterate over rows of file to extract data needed
        for row in data:
            value.append(row['value'])
            date.append(row['date'])

        # append lists to json dictionary
        json_dict["value"] = value
        json_dict["date"] = date

    # write the dictionary into the json file
    with open(OUTPUT_JSON, 'w') as output:
        js.dump(json_dict, output)

if __name__ == "__main__":
    converter(INPUT_CSV)
