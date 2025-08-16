#!/usr/bin/python3

''' This module for CSV serelize and deserize to json'''

import csv,json



def convert_csv_to_json(filename):
    try:
        with open(filename,"r", encoding="utf-8") as csvfile:
            dicts =csv.DictReader(csvfile)
            data = list(dicts)
        
            with open("data.json","w", encoding="utf-8") as data_file:
                jsonified_data = json.dump(data,data_file)
            return True
    except:
        return False
