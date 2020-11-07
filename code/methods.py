import random
import os
import csv


def generate_csv(n, output_path):
    array = generate_input(n)
    with open(os.path.join(output_path, "test2.csv"), 'w') as file:
        writer = csv.writer(file)
        writer.writerow(array)


def generate_input(n):
    array = []
    for i in range(0, n):
        array.append(random.randint(1, 10))
    return array
