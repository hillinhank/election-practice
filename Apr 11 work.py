# 1 + 1

import csv

import os

total_votes = 0

file_to_load = '/Users/user/Downloads/election_results-2.csv'
file_to_save = '/Users/user/election_analysis.txt'


election_data = open(file_to_load, 'r')

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
print(total_votes)
        
    








outfile = open(file_to_save, "w")
outfile.write('Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson')
















