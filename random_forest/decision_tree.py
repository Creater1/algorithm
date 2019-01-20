import numpy as np
from scipy.optimize import fsolve
import random as rd

variables = np.array([[-0.3, 12.1], [4.1, 5.8]])
n, m = variables.shape
lengths = np.zeros(n)
precision = [0.0001, 0.0001]
for i in range(n):
    temp = fsolve(lambda x: ((variables[i][1] - variables[i][0]) * 1 / precision[i]) - 2 ** (x - 1), 50)
    lengths[i] = int(np.floor(temp[0]))

population = []
for i in range(10):
    chromosomes = []
    for length in lengths:
        chromosome = np.random.randint(0, 2, int(length))
        chromosomes.append(chromosome)
    population.append(chromosomes)


update_pop = np.copy(population)
m = len(population)
n = sum(lengths)
gen_num = np.uint8(m * n * 0.4)
gen_index = []
for i in range(gen_num):
    gen_index.append(rd.randint(0, m * n - 1))
for gene in gen_index:
    _m = int(gene // n)
    _n = int(gene % n)
    mutate_chromosomes = population[0]
    try:
        mutate_chromosomes = population[_m]
    except IndexError:
        print("_m:", _m, "_n:", _n, "gene:", gene)
    temp_sum = 0
    pos = 0
    for j in range(len(lengths)):
        if temp_sum <= _n < (temp_sum + lengths[j]):
            pos = int(_n - temp_sum)
            _n = j
            break
        else:
            temp_sum += lengths[j]
    mutate_chromosomes[_n][pos] = 1 - mutate_chromosomes[_n][pos]
    population[_m] = mutate_chromosomes
print(update_pop)