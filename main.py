#!/usr/bin/env python

'''
Purpose: List all taco trucks or lookup the menus of specific taco trucks

Changelog:
===============================================================================================================
Date             Who               Version            Jira#              Description
===============================================================================================================
10/27/2022     Baurzhan Siitov      1.0.0              #308        - initial script, with two options:
                                                                     -all,  get list of taco trucks
                                                                     -name, get menu of specific taco truck      

'''

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="Example: main.py -all : output list of trucks")
    
    parser.add_argument('-name', help="Name of facility")
    parser.add_argument('-all', const="all",nargs='?',  help="List of all Taco Trucks")
    args = parser.parse_args()
    
    # set arguments for utility 
    url = 'https://data.sfgov.org/api/views/rqzj-sfat/rows.json?accessType=DOWNLOAD'
    r = requests.get(url)
    json_content = r.json()
    list_trucks = json_content["data"]
    count =0
    listnames = []
    menu = "Please choose a specific Truck name, to get the menu list"
    name = ""
    location = ""
    
    if args.name != None:
        for truck in list_trucks:
            if args.name in truck[9]:
                count +=1
                if truck[9] == args.name:
                    menu = truck[19]
                    name = truck[9]
                    location = truck[13] +  ", SAN FRANCISCO, CA"
                listnames.append(truck[9])
        print(f"Name/location of Truck: {name} / address: {location.upper()}\nMenu: {menu}\n")
        print(f"[ INFO ] There are: {count} similare names, with requested word/s '{args.name}'")
        print("")
        [print(truck) for truck in set(listnames)]
                
    if args.all != None:
        for truck in list_trucks:
            listnames.append(truck[9])
        [print(num, truck) for num, truck in enumerate(set(listnames))]
    
if __name__=='__main__':
    main()