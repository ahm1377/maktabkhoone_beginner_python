import csv
from statistics import mean 
from collections import OrderedDict

def calculate_averages(input_file_name, output_file_name):
    linelist = list()
    name = list()
    avgnum = list()
    with open(input_file_name) as csvinfile:
        reader = csv.reader(csvinfile)
        for row in reader:
            print(row[0])

inp = 'C:\\Users\\ali mosaffa\\Desktop\\pytest.csv'
outp = 'C:\\Users\\ali mosaffa\\Desktop\\pytestout.csv'
calculate_averages(inp, outp)
