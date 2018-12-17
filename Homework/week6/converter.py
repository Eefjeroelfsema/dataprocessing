"""
This programme converts csv files to json files
"""

import numpy as np
import csv
import pandas as pd
import json as js


INPUT_CSV = "gdp_forecast.csv"
OUTPUT_JSON = "data.json"

def converter(INPUT_CSV):
    with open(INPUT_CSV) as csvfile:
        data = csv.DictReader(csvfile)

        # main json dictionary
        json_list = []

        # list of values needed
        AUS = {}
        AUT = {}
        BEL = {}
        CAN = {}
        CZE = {}
        DNK = {}
        FIN = {}
        FRA = {}
        DEU = {}
        GRC = {}
        HUN = {}
        ISL = {}
        IRL = {}
        ITA = {}
        JPN = {}
        KOR = {}
        LUX = {}
        MEX = {}
        NLD = {}
        NLZ = {}
        NOR = {}
        POL = {}
        PRT = {}
        SVK = {}
        ESP = {}
        SWE = {}
        CHE = {}
        TUR = {}
        GRB = {}
        USA = {}
        BRA = {}
        CHL = {}
        CHN = {}
        EST = {}
        IND = {}
        IDN = {}
        ISR = {}
        RUS = {}
        ZAF = {}
        SVN = {}
        LVA = {}
        LTA = {}
        COL = {}
        LTU = {}
        ARG = {}

        # iterate over rows of file to extract data needed
        for row in data:
            if row["LOCATION"] == 'AUS':
                AUS['location'] = row['LOCATION']
                AUS[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'ARG':
                ARG['location'] = row['LOCATION']
                ARG[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'AUT':
                AUT['location'] = row['LOCATION']
                AUT[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'BEL':
                BEL['location'] = row['LOCATION']
                BEL[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'CZE':
                CZE['location'] = row['LOCATION']
                CZE[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'DNK':
                DNK['location'] = row['LOCATION']
                DNK[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'FIN':
                FIN['location'] = row['LOCATION']
                FIN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'FRA':
                FRA['location'] = row['LOCATION']
                FRA[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'DEU':
                DEU['location'] = row['LOCATION']
                DEU[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'GRC':
                GRC['location'] = row['LOCATION']
                GRC[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'HUN':
                HUN['location'] = row['LOCATION']
                HUN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'ISL':
                ISL['location'] = row['LOCATION']
                ISL[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'IRL':
                IRL['location'] = row['LOCATION']
                IRL[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'ITA':
                ITA['location'] = row['LOCATION']
                ITA[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'LUX':
                LUX['location'] = row['LOCATION']
                LUX[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'NLD':
                NLD['location'] = row['LOCATION']
                NLD[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'NOR':
                NOR['location'] = row['LOCATION']
                NOR[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'POL':
                POL['location'] = row['LOCATION']
                POL[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'PRT':
                PRT['location'] = row['LOCATION']
                PRT[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'SVK':
                SVK['location'] = row['LOCATION']
                SVK[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'ESP':
                ESP['location'] = row['LOCATION']
                ESP[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'SWE':
                SWE['location'] = row['LOCATION']
                SWE[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'CHE':
                CHE['location'] = row['LOCATION']
                CHE[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'TUR':
                TUR['location'] = row['LOCATION']
                TUR[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'GRB':
                GRB['location'] = row['LOCATION']
                GRB[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'EST':
                EST['location'] = row['LOCATION']
                EST[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'RUS':
                RUS['location'] = row['LOCATION']
                RUS[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'SVN':
                SVN['location'] = row['LOCATION']
                SVN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'LVA':
                LVA['location'] = row['LOCATION']
                LVA[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'LTA':
                LTA['location'] = row['LOCATION']
                LTA[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'CAN':
                CAN['location'] = row['LOCATION']
                CAN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'JPN':
                JPN['location'] = row['LOCATION']
                JPN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'KOR':
                KOR['location'] = row['LOCATION']
                KOR[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'MEX':
                MEX['location'] = row['LOCATION']
                MEX[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'NLZ':
                NLZ['location'] = row['LOCATION']
                NLZ[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'USA':
                USA['location'] = row['LOCATION']
                USA[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'BRA':
                BRA['location'] = row['LOCATION']
                BRA[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'CHL':
                CHL['location'] = row['LOCATION']
                CHL[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'CHN':
                CHN['location'] = row['LOCATION']
                CHN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'IDN':
                IDN['location'] = row['LOCATION']
                IDN[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'IND':
                IND['location'] = row['LOCATION']
                IND[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'ISR':
                ISR['location'] = row['LOCATION']
                ISR[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'ZAF':
                ZAF['location'] = row['LOCATION']
                ZAF[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'COL':
                COL['location'] = row['LOCATION']
                COL[row['TIME']] = row['Value']
            elif row["LOCATION"] == 'LTU':
                LTU['location'] = row['LOCATION']
                LTU[row['TIME']] = row['Value']


        # append lists to json dictionary
        json_list.append(AUS)
        json_list.append(ARG)
        json_list.append(AUT)
        json_list.append(BEL)
        json_list.append(CAN)
        json_list.append(CZE)
        json_list.append(DNK)
        json_list.append(FIN)
        json_list.append(FRA)
        json_list.append(DEU)
        json_list.append(GRC)
        json_list.append(HUN)
        json_list.append(ISL)
        json_list.append(IRL)
        json_list.append(ITA)
        json_list.append(JPN)
        json_list.append(KOR)
        json_list.append(LUX)
        json_list.append(MEX)
        json_list.append(NLD)
        json_list.append(NLZ)
        json_list.append(NOR)
        json_list.append(POL)
        json_list.append(PRT)
        json_list.append(SVK)
        json_list.append(ESP)
        json_list.append(SWE)
        json_list.append(CHE)
        json_list.append(TUR)
        json_list.append(GRB)
        json_list.append(USA)
        json_list.append(BRA)
        json_list.append(CHL)
        json_list.append(CHN)
        json_list.append(EST)
        json_list.append(RUS)
        json_list.append(SVN)
        json_list.append(LVA)
        json_list.append(LTA)
        json_list.append(IND)
        json_list.append(IDN)
        json_list.append(ISR)
        json_list.append(ZAF)
        json_list.append(COL)
        json_list.append(LTU)


    # write the dictionary into the json file
    with open(OUTPUT_JSON, 'w') as output:
        js.dump(json_list, output)

if __name__ == "__main__":
    converter(INPUT_CSV)
