from code.GA import GA

import numpy as np
import random as rd
from scipy.optimize import fsolve
from abc import ABCMeta, abstractmethod


class genetic_process(metaclass=ABCMeta):

    @abstractmethod
    def loss_func(self, chromosomes):
        pass

    @abstractmethod
    def get_elimination_num(self):
        pass

    @staticmethod
    def get_lengths(variables, precision):
        n, m = variables.shape
        lengths = np.zeros(n)
        for i in range(n):
            temp = fsolve(lambda x: ((variables[i][1] - variables[i][0]) * 1 / precision[i]) - 2 ** (x - 1), 50)
            lengths[i] = int(np.floor(temp[0]))
        return lengths

    @staticmethod
    def decode_to_fact(chromosomes, precision, variables):
        fact = []
        i = 0
        for i in range(len(chromosomes)):
            sum = 0
            power = 1
            for j in range(len(chromosomes[i]) - 1, -1, -1):
                sum = sum + chromosomes[i][j] * power
                power = power * 2
            sum = sum * precision[i] + variables[i][0]
            fact.append(sum)
            i += 1
        return fact

    @staticmethod
    def get_initial_population(lengths, population_size):
        population = []
        for i in range(population_size):
            chromosomes = []
            for length in lengths:
                chromosome = np.random.randint(0, 2, int(length))
                chromosomes.append(chromosome)
            population.append(chromosomes)
        return population

    @staticmethod
    def select_new_population(self, population):
        temp_pop = []
        new_pop = []
        best_value = 10000000
        best_chromosomes = []
        pop_size = len(population)
        all_loss = []
        limit = self.get_elimination_num()
        i = 0
        while i < len(population):
            loss = self.loss_func(population[i])
            if loss > limit or np.isnan(loss):
                i += 1
                continue
            #all_loss.append(limit - loss)   #求小值
            all_loss.append(loss) #求大值
            temp_pop.append(population[i])
            if loss < best_value:
                best_value = loss
                best_chromosomes = population[i]
            i += 1
        total = sum(all_loss)
        wheel = []
        a = 0
        for i in range(len(all_loss)):
            a += float(all_loss[i] / total)
            wheel.append(a)
        ms = []
        for i in range(pop_size):
            ms.append(rd.random())
        ms.sort()
        fitin = 0
        newin = 0
        while newin < pop_size:
            try:
                if ms[newin] < wheel[fitin]:
                    new_pop.append(temp_pop[fitin])
                    newin += 1
                else:
                    fitin += 1
            except IndexError:
                print("newin:", newin, "fitin:", fitin)
        return new_pop, best_value, best_chromosomes

    @staticmethod
    def crossover(population, lengths, p=0.8):
        n = len(population)
        m = n * sum(lengths)
        numbers = np.uint8(m * p)
        if numbers % 2 != 0:
            numbers += 1
        update_pop = np.copy(population)
        index = []
        for i in range(numbers):
            index.append(rd.randint(0, n - 1))
        while len(index) > 0:
            a = index.pop()
            b = index.pop()
            cross_chromo = rd.randint(0, len(lengths) - 1)
            cross_pos = rd.randint(1, lengths[cross_chromo] - 1)

            chromosome_a = update_pop[a][cross_chromo]
            chromosome_b = update_pop[b][cross_chromo]
            temp = chromosome_a[cross_pos:]
            chromosome_a[cross_pos:] = chromosome_b[cross_pos:]
            chromosome_b[cross_pos:] = temp
            update_pop[a][cross_chromo] = chromosome_a
            update_pop[b][cross_chromo] = chromosome_b
        return update_pop

    @staticmethod
    def mutation(population, lengths, p=0.4):
        update_pop = np.copy(population)
        m = len(population)
        n = sum(lengths)
        gen_num = np.uint8(m * n * p)
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
        return update_pop

    def run(self, variables, precision, max_iter=500, population_size=500):
        best_values = []
        best_pop = []
        lengths = self.get_lengths(variables, precision)
        population = self.get_initial_population(lengths, population_size)
        while max_iter > 0:
            population, best_value, best_chromosomes = self.select_new_population(self, population)
            #population = self.get_initial_population(lengths, population_size)
            best_values.append(best_value)
            best_pop.append(best_chromosomes)
            print("iter:", max_iter, "\n", best_value)
            population = self.crossover(population, lengths)
            population = self.mutation(population, lengths)
            max_iter -= 1

        return best_values, best_pop