import os
import time
from heuristics.gd_partition import GdPartition
from exact.ex_partition import ExPartition
from methods import generate_input


def run(input_path, output_path):
    input_data = {}
    output_data = {}

    read_and_load(input_path, input_data)

    calc(input_data, output_data)

    save(output_data, output_path)


def read_and_load(input_path, input_data):
    print('Read and Load')
    f_list = os.listdir(input_path)
    lines = []
    new_lines = []
    for i in f_list:
        if os.path.splitext(i)[1] == '.txt':
            f = open(os.path.join(input_path, i), 'r')
            lines = lines + f.readlines()
            f.close()
    for line in lines:
        new_str = str(line).strip().replace('\t', '').replace('\r', '').replace('\n', '')
        if new_str == "":
            continue
        new_lines.append(new_str)
    i = 0
    atom = []
    inputs = []
    for line in new_lines:
        i = i + 1
        if i == 1:
            continue
        elif i == 2:
            atom.append(line)
        elif i == 3:
            atom.append(int(line))
        elif i == 4:
            arr_str = line.split(',')
            arr = []
            for st in arr_str:
                arr.append(int(st))
            atom.append(arr)
            inputs.append(atom)
            atom = []
            i = 0
    input_data['input'] = inputs


def calc(input_data, output_data):
    print("calculation")
    outputs = []
    output = {}
    for atom in input_data['input']:
        input_array = ""
        if len(atom[2]) == 1:
            input_array = generate_input(atom[2][0])
        else:
            input_array = atom[2]
        pt = ""
        if atom[0] == 'o':
            pt = ExPartition(input_array)
            output['type'] = "O"
        else:
            pt = GdPartition(input_array)
            output['type'] = "H"

        start = time.process_time()
        pt.partition()
        output = {'result': pt.p,
                  'time': time.process_time() - start}
        outputs.append(output)
        output_data['output'] = outputs


def save(output_data, output_path):
    print("save")
    f = open(os.path.join(output_path, 'result.txt'), 'w')
    for line in output_data['output']:
        f.write(str(line) + '\n')
    f.close()
