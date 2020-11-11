import os
import csv
import time
from heuristics.gd_partition import GdPartition
from exact.ex_partition import ExPartition


def run(input_path, output_path):
    input_data = {}
    output_data = {}

    read_and_load(input_path, input_data)

    calc(input_data, output_data)

    save(output_data, output_path)


def read_and_load(input_path, input_data):
    input_1 = os.path.join(input_path, "test1.csv")
    input_2 = os.path.join(input_path, "test2.csv")
    inputpath = ""
    if os.path.exists(input_1):
        inputpath = input_1
        input_data['option'] = 1
    elif os.path.exists(input_2):
        inputpath = input_2
        input_data['option'] = 2
    input_array = []
    with open(inputpath, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in row:
                input_array.append(int(i))
    input_data['array'] = input_array


def calc(input_data, output_data):
    print("calculation")
    pt = ""
    start = ""
    if input_data['option'] == 1:
        print("Step: 1")
        pt = ExPartition(input_data['array'])
        start = time.process_time()
        pt.partition()
        output_data['time'] = format(time.process_time() - start, 'f')
    elif input_data['option'] == 2:
        print("Step: 2")
        pt = GdPartition(input_data['array'])
        start = time.process_time()
        pt.partition()
        output_data['time'] = format(time.process_time() - start, 'f')
    output = []
    for i in range(0, 4):
        output.append(pt.p[i])
    output_data['result'] = output


def save(output_data, output_path):
    print("save")
    with open(os.path.join(output_path, "result.csv"), 'w') as file:
        writer = csv.writer(file)
        writer.writerows(output_data['result'])
        writer.writerow("Time: "+str(output_data['time']))
