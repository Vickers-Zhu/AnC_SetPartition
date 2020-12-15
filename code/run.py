import os
import time
import traceback

from heuristics.gd_partition import GdPartition
from exact.ex_partition import ExPartition
from methods import generate_input, fitness, test_sum_of_weights, test_correctness


def run(input_path, output_path):
    while True:
        input_data = {}
        output_data = {}
        file_name = input("Please input the file name placed in the same folder as execution.bat\n"
            "Press E to quit.\n").strip()
        if file_name == "E":
            return
        input_path = os.path.join(os.getcwd(), file_name)

        read_and_load(input_path, input_data)

        calc(input_data, output_data)

        save(output_data, output_path)

        os.system("pause")


def read_and_load(input_path, input_data):
    # f_list = os.listdir(input_path)
    lines = []
    new_lines = []
    # for i in f_list:
    #     if os.path.splitext(i)[1] == '.txt':
    try:
        f = open(input_path, 'r')
        lines = lines + f.readlines()
        f.close()
    except Exception as e:
        msg = traceback.format_exc()
        # print(msg)
        print("File not found!!\n"
            "1. Please make sure you the file name has been input correctly\n"
            "2. Please make sure the input text file is in the same directory as execution.bat\n")
    finally:
        pass

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
    outputs = []
    for atom in input_data['input']:
        output = {}
        input_array = ""
        if len(atom[2]) == 1:
            input_array = generate_input(atom[2][0])
            print("Generated array is")
            print(input_array)
        else:
            input_array = atom[2]
        pt = ""
        num_of_weights = len(input_array)
        if atom[0].lower() == 'o':
            pt = ExPartition(input_array)
            output['type'] = "o"
        else:
            pt = GdPartition(input_array)
            output['type'] = "h"

        start = time.process_time()
        result = ""
        try:
            pt.partition()
            result = pt.p[:]
        except Exception as e:
            msg = traceback.format_exc()
            # print(msg)
            print("Error during partition")
        finally:
            pass
        output = {'type': output['type'],
                  'result': result,
                  'time': format(time.process_time() - start, '.10f'),
                  'fitness': fitness(partitions=result)}
        print(output)
        outputs.append(output)
    output_data['output'] = outputs


def save(output_data, output_path):
    f = open(os.path.join(output_path, 'result.txt'), 'w')
    for line in output_data['output']:
        f.write(str(line) + '\n')
    f.close()
