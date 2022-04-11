# 1 + 1

import csv

import os



file_to_load = '/Users/user/Downloads/election_results-2.csv'
file_to_save = '/Users/user/election_analysis.txt'


election_data = open(file_to_load, 'r')

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    








outfile = open(file_to_save, "w")
outfile.write('Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson')
















