"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import pprint as pp

from models import NearEarthObject, CloseApproach
from helpers import cd_to_datetime, datetime_to_str
from database import NEODatabase

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data )from the given CSV file.

    neo=[]
    index=[3, 4, 7, 15 ] # The data columns we need from the CSV file 

    with open(neo_csv_path) as file: 
        data=csv.reader(file) # Returns a reader object 

        next(data) # skip the header 
        for i, row in enumerate(data):
            srow = [ row[j] for j in index]

            neo.append(NearEarthObject(
                    designation=srow[0], 
                    name=srow[1], 
                    hazardous=srow[2], 
                    diameter=srow[3],
                    approaches=[])) 

    # return a list of neo objects
    return neo

def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.

    approaches=[] # A list of Close Approach indexed by designation (key is des)

    index=[0, 3, 4, 7] # The data columns we need from the JSON file 

    with open(cad_json_path) as file:
        data = json.load(file) 
        for i, record in enumerate(data['data']):
            srow=[record[j] for j in index ]

            approaches.append(
                    CloseApproach(
                        des=srow[0], 
                        cd=srow[1] , 
                        dist=srow[2], 
                        v_rel=srow[3]))
    return approaches

neo=load_neos("./data/neos.csv")
approaches=load_approaches("./data/cad.json")
