#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Dictionary Value Finder, Version 0.4-Beta (Dop Not Distribute)
By Rick Pelletier (galiagante@gmail.com), 09 November 2022
Last Update: 19 November 2024

In this updated version, I used 'yield' instead of 'append'. This means that
the function will return a generator object rather than creating an entire
list. When you need to access the values, you can simply iterate over the
generator like so:

    dictionary = {...}  # your dictionary here
    key_to_find = 'your_key_here'

    for value in findkeys(dictionary, key_to_find):
        print(value)

This will print all values associated with `key_to_find` without storing them
all in memory at once.
"""


import sys
import argparse
import json


def findkeys(dictionary_data:dict, key_value:str) -> list:
    results = list()

    if isinstance(dictionary_data, dict):
        for key, value in dictionary_data.items():
            if key == key_value:
                yield value
            elif isinstance(value, dict):
                yield from findkeys(value, key_value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        yield from findkeys(item, key_value)

    return list(results)


if __name__ == '__main__':
    exit_value = 0
    count = 0

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", type=str, required=True)
    parser.add_argument("--key", "-k", type=str, required=True)
    args = parser.parse_args()

    try:
        with open(args.file) as json_data:
            d = json.load(json_data)

            if (results := findkeys(d, args.key)):
                for value in findkeys(d, args.key):
                    #print(value)
                    count += 1

                print(f'Results found: {count}')

            else:
                print('No data')

    except IOError as e:
        print(e)
        exit_value = 1

    sys.exit(exit_value)
else:
    sys.exit(1)

# end of script
