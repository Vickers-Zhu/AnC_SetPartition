import os
import sys
sys.path.append('./heuristics')
import csv
from gd_partition import GdPartition


def run(input_path, output_path):
    input_data = []
    output_data = []

    read_and_load(input_path, input_data)

    calc(input_data, output_data)

    save(output_data, output_path)


def read_and_load(input_path, input_data):
    with open(os.path.join(input_path, "test1.csv"), 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in row:
                input_data.append(int(i))


def calc(input_data, output_data):
    print("calculation")
    pt = GdPartition(input_data)
    pt.partition()


def save(output_data, output_path):
    print("save")
