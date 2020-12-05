import random
import os
import csv
import matplotlib.pyplot as plt


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


def generate_plot(x, y):
    plt.plot(x, y, label="time consuming")
    plt.xlabel('numbers of weights')
    plt.ylabel('time')
    plt.legend()
    plt.show()


def fitness(partitions: []):
    value_max = sum(partitions[0])
    value_min = sum(partitions[0])
    for w in partitions:
        sum_w = sum(w)
        if sum_w < value_min:
            value_min = sum_w
        if sum_w > value_max:
            value_max = sum_w
    return value_max - value_min


def test_correctness(partitions: [], num_of_weights: int):
    suc_part = ""
    min_dif = 100
    for time in partitions:
        count = 0
        for partition in time:
            for weight in partition:
                count = count + 1
        if count == num_of_weights:
            print(True)
            if fitness(time) < min_dif:
                min_dif = fitness(time)
                suc_part = time
    return suc_part


def test_sum_of_weights(partitions: []):
    sm = 0
    for w in partitions:
        sm += sum(w)
    return sm == 0
