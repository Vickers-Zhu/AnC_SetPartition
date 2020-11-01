import os
import sys
sys.path.append('./heuristics')
sys.path.append('./exact')
import csv
from gd_partition import GdPartition
from ex_partition import ExPartition


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
    pt = ExPartition(input_data)
    pt.partition(0)
    for i in range(0, 4):
        output_data.append(pt.p[i])


def save(output_data, output_path):
    print("save")
    with open(os.path.join(output_path, "result.csv"), 'w') as file:
        writer = csv.writer(file)
        writer.writerows(output_data)
