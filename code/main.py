import os
from run import run
from methods import generate_csv


if __name__ == '__main__':
    input_path = "../test/input"
    output_path = "../test/output"
#     generate_csv(100, output_path)
    run(input_path, output_path)
