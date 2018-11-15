#!/usr/bin/env python
# Name: Eefje Roelfsema
# Student number: 10993673

"""
This programme examines several data informatoin of countries
"""
import numpy as np
import csv
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import json as js

# input csv file and ouput json file
INPUT_CSV = "input.csv"
OUTPUT_JSON = "output.json"

# main function
def main(input):

    # list to make dataframe with correct values
    list = []

    # open csv datafile
    with open("input.csv") as csvfile:
        data = csv.DictReader(csvfile)

        # iterate through all the rows in the csv-file
        for row in data:

            # delete words unknown and dollars from gdp column
            row["GDP ($ per capita) dollars"] = row["GDP ($ per capita) dollars"].strip(" dollars, unknown")

            # convert gdp string into float if not empty
            if row["GDP ($ per capita) dollars"] != '':
                row["GDP ($ per capita) dollars"] = float(row["GDP ($ per capita) dollars"])

            # define value as none
            else:
                row["GDP ($ per capita) dollars"] = None

            # check if row of infants is not empty
            if row["Infant mortality (per 1000 births)"] != '':

                # replace comma's with dots
                row["Infant mortality (per 1000 births)"] = row["Infant mortality (per 1000 births)"].replace(",", ".")

                # make floats of strings
                row["Infant mortality (per 1000 births)"] = float(row["Infant mortality (per 1000 births)"])

            # define as none
            else:
                row["Infant mortality (per 1000 births)"] = None

            # remove extra spaces in Region column
            row["Region"] = row['Region'].strip(" ")

            # add row to list
            list.append(row)

    # make a dataframe of list of adjusted values, make header the first row
    dataframe = pd.DataFrame(list, columns = list[0])

    # call in functions to examine and to write to json file
    gdp(dataframe["GDP ($ per capita) dollars"])
    infant_mortility(dataframe["Infant mortality (per 1000 births)"])
    json(dataframe)


# gdp function to examine the gdp column
def gdp(dataframe_gdp):
    # calculate Mean, Median, Mode of GDP, Q1 and Q3 for data with outliers
    mean = dataframe_gdp.mean()
    median = dataframe_gdp.median()
    mode = dataframe_gdp.mode()
    std = dataframe_gdp.std()
    q1 = dataframe_gdp.quantile(q=0.25)
    q3 = dataframe_gdp.quantile(q=0.75)

    print(dataframe_gdp)

    print(f"Mean with outliers: ", mean)
    print(f"Median with outliers: ", median)
    print(f"Mode with outliers: ", mode)
    print(f"Standard deviation with outliers: ", std)

    #make histogram of the GDP
    n , bins, patches = plt.hist(dataframe_gdp, 50, alpha=0.75)
    plt.xlabel('GDP')
    plt.ylabel('Probability')
    plt.title('Histogram of GDP of countries')
    # plt.axis([0,60000,0,0.00008])
    plt.grid(True)
    plt.show()

    # calulate lower-and upperbound
    lowerbound = q1 - 1.5*(q3-q1)
    upperbound = q3 + 1.5*(q3-q1)

    # make new list to remove outliers
    gdp_list = []
    for gdp in dataframe_gdp:
        if gdp >lowerbound or gdp < upperbound:
            gdp_list.append(gdp)

    # make new dataframe for removed outlier list
    dataframe_gdpadjust = pd.DataFrame(gdp_list)

    print(dataframe_gdpadjust)

    # calculate Mean, Median, Mode of GDP for data without outliers
    mean_adjust = dataframe_gdpadjust.mean()
    median_adjust = dataframe_gdpadjust.median()
    mode_adjust = dataframe_gdpadjust.mode()
    std_adjust = dataframe_gdpadjust.std()

    print(f"Mean without outliers: ", mean_adjust)
    print(f"Median without outliers: ", median_adjust)
    print(f"Mode without outliers: ", mode_adjust)
    print(f"Standard deviation without outliers: ", std_adjust)

    # make new histogram without outliers
    n , bins, patches = plt.hist(dataframe_gdpadjust[0], alpha=0.75)
    plt.xlabel('GDP')
    plt.ylabel('Probability')
    plt.title('Histogram of GDP of countries with deleted outliers')
    # plt.axis([0,60000,0,0.00008])
    plt.grid(True)
    plt.show()

# def moratility function to examin mortality column
def infant_mortility(dataframe_infant):
    # calculate Minimum, First Quartile, Median, Third Quartile and Maximum
    minimum = dataframe_infant.min()
    q1 = dataframe_infant.quantile(q=0.25)
    median = dataframe_infant.median()
    q3 = dataframe_infant.quantile(q=0.75)
    maximum = dataframe_infant.max()

    # make a list to put values into the boxplot
    list = []

    # iterate over all the rates in the dataframe
    for rate in dataframe_infant:

        # only add real values to the list
        if not np.isnan(rate):
            list.append(rate)

    # make boxplot of infant mortality
    plt.boxplot(list)
    plt.title("Boxplot of infant moratility rates")

    # print(plt.boxplot(list))
    plt.show()
    # hallo

# write the output file in json
def json(dataframe):

    # main dictoinary
    json_dict = {}

    # iterate over the rows in the dataframe
    for index, row in dataframe.iterrows():

        # make temporary dictionary
        information = {}

        # put needed information in the temporary dictonary
        information["Region"] = row["Region"]
        information["Pop. Density (per sq. mi.)"] = row["Pop. Density (per sq. mi.)"]
        information["Infant mortality (per 1000 births)"] = row["Infant mortality (per 1000 births)"]
        information["GDP ($ per capita) dollars"] = row["GDP ($ per capita) dollars"]

        # add the information to the dictionary under the country-name
        json_dict[row["Country"]] = information

    # write the dictionary into the json file
    with open(OUTPUT_JSON, 'w') as output:
        js.dump(json_dict, output)

if __name__ == "__main__":
    main(INPUT_CSV)
