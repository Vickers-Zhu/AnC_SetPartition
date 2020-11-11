import os
from run import run
from methods import generate_csv
from methods import generate_plot


if __name__ == '__main__':
    input_path = "./"
    output_path = "./"

#     x1 = [1, 2, 3, 4, 5, 6]
#     y1 = [0.001149, 0.001285, 0.008426, 0.0011493, 0.000379, 0.003285]
#     x = [2000, 4000, 6000, 8000, 10000]
#     y = [0.020125, 0.088366, 0.144212, 0.260007, 0.380806]

#     generate_csv(10000, input_path)

    run(input_path, output_path)

#     generate_plot(x, y)
