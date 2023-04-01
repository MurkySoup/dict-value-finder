#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dictionary Value Finder, Version 0.2-Beta (Dop Not Distribute)
By Rick Pelletier (galiagante@gmail.com), 09 November 2022
Last Update: 01 April 2023

The new implementation should be more efficient and easier to read and maintain.
Changes to 'findkeys()' made in this version include:

1. Replace the use of generator functions with a list-based approach to allow
   for easier debugging and better memory management.
2. Simplification of conditional statements.
3. Removal redundant code.
3. Adding a docstring to describe the function's behavior and parameters.
4. Function now returns a proper list rather than an non-iterable object.

"""

import sys
import argparse
import json


"""
Recursively searches a dictionary for a target key and returns all corresponding values.

:param dictionary_data: dictionary to search
:param key_value: target key
:return: list of all values for target key
"""

def findkeys(dictionary_data:dict, key_value:str):
    results = []

    if isinstance(dictionary_data, dict):
        for key, value in dictionary_data.items():
            if key == key_value:
                results.append(value)
            elif isinstance(value, dict):
                results += findkeys(value, key_value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        results += findkeys(item, key_value)

    return list(results)

if __name__ == '__main__':
    exit_value = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument("--key", "-k", type=str, required=True)
    args = parser.parse_args()

    try:
        with open(args.file) as json_data:
            d = json.load(json_data)
    except IOError as e:
        print(e)
        exit_value = 1

    if (results := findkeys(d, args.key)):
        print(results)
        print(f'{len(results)} matches found')
    else:
        print('No data')

    sys.exit(exit_value)
else:
    sys.exit(1)

# end of script
