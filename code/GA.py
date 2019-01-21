import random
import math
import pandas as pd
import numpy as np



class GA():
    def __init__(self, length, count):
        #染色体的数目
        self.length = length
        self.count = count
        #随机生成初始化种群
        self.population = self.gen_population(length, count)


    #产生
    def gen_population(self, length, count):
        """
        获取初始种群（一个含有count个长度为length的染色体的列表）
        """
        # return [self.gen_chromosome(length) for i in range(count)]
        chromosome = []
        for i in range(count):
            gene = 0
            for j in range(length):
                gene |= (1 << j) * random.randint(0, 1)
            chromosome.append(gene)
        return chromosome

    # def gen_population(self, length, count):
    #     """
    #     获取初始种群（一个含有count个长度为length的染色体的列表）
    #     """
    #     return [self.gen_chromosome(length) for i in range(count)]


    def gen_chromosome(self, length):
        """
        随机生成长度为length的染色体，每个基因的取值是0或1
        这里用一个bit表示一个基因
        """
        chromosome = 0
        for i in range(length):
            chromosome |= (1 << i) * random.randint(0, 1)
        return chromosome

    def decode(self, chromosome):
        """
        解码染色体，将二进制转化为属于[0, 9]的实数
        """
        #list乘以某个数：方法1
        # chromosome = [(i * 9.0)/(2**self.length - 1) for i in chromosome]
        # list乘以某个数：方法2
        chromosome = pd.Series(chromosome)
        chromosome = (chromosome * 9.0 / (2**self.length-1)).tolist()
        # chromosome = (chromosome * 10).tolist()
        return chromosome

    #适应度函数
    def fitness(self, chromosome):
        solution = []
        # print(chromosome)
        chromosomes = self.decode(chromosome)
        for x in chromosomes:
            answer = x + 10 * math.sin(5 * x) + 7 * math.cos(4 * x)
            solution.append(answer)
        return solution

    #进化
    def evolve(self, retain_rate, random_select_rate, solution):
        """
        进化
        对当前一代种群依次进行选择、交叉并生成新一代种群，然后对新一代种群进行变异
        """
        parents = self.selection(retain_rate, random_select_rate, solution)
        # print(parents, len(parents))
        self.crossover(parents)
        self.mutation(0.5)

    def selection(self, retain_rate, random_select_rate, solution):
        """
        选择
        先对适应度从大到小排序，选出存活的染色体
        再进行随机选择，选出适应度虽然小，但是幸存下来的个体
        """
        #对适应度从大到小排序
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        test =  sorted(graded, reverse=True)
        graded = [x[1] for x in test]
        # 选择适应度强的函数
        retain_length = int(len(graded)*retain_rate)
        parents = solution[:retain_length]
        for solution in solution[retain_length:]:
            if random.random() < random_select_rate:
                parents.append(solution)
        return parents

    #交叉编译
    def crossover(self, parents):
        """
        染色体的交叉、繁殖，生成新一代的种群
        """
        # 新出生的孩子，最终会被加入存活下来的父母之中，形成新一代的种群。
        children = []
        # 需要繁殖的孩子的量
        target_count = len(self.population) - len(parents)
        # 开始根据需要的量进行繁殖
        while len(children) < target_count:
            male = random.randint(0, len(parents)-1)
            female = random.randint(0, len(parents)-1)
            if male != female:
                # 随机选取交叉点
                cross_pos = random.randint(0, self.length)
                # 生成掩码，方便位操作
                mask = 0
                for i in range(cross_pos):
                    mask |= (1 << i)
                male = parents[male]
                female = parents[female]
                # 孩子将获得父亲在交叉点前的基因和母亲在交叉点后（包括交叉点）的基因
                gen_parants = ((male & mask) | (female & ~mask))
                length = ((1 << self.length) - 1)
                #保证产生一个0-7之间的数据
                child = gen_parants & length
                children.append(child)
        # 经过繁殖后，孩子和父母的数量与原始种群数量相等，在这里可以更新种群。
        self.population = parents + children

    def mutation(self, rate):
        """
         变异
         对种群中的所有个体，随机改变某个个体中的某个基因
         """
        # print(self.population)
        for i in range(len(self.population)):
            if random.random() < rate:
                j = random.randint(0, self.length - 1)
                population = self.population[i]
                population ^= 1 << j


    # 将str转化为int
    def con_str_int(self, str):
        data = map(eval, str)
        return data

    def result(self):
        """
        获得当前代的最优值，这里取的是函数取最大值时x的值。
        """
        # print(self.population)
        # graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [(self.fitness(chromosome), chromosome) for chromosome in self.population]
        graded = [x[1] for x in sorted(graded, reverse=True)]
        # print(graded)
        return ga.decode(graded[0])

    #将十进制小数转化为二进制数
    def dec_to_bin(self,x):
        x = x - int(x)
        bins = []
        while x:
            if len(bins) >= 4:
                break
            x = x * 2
            bins.append(1 if x >= 1. else 0)
            if x >= 1:
                x = x - int(x)
            else:
                x = x
        print(bins)


if __name__ == '__main__':
    retain_rate = 0.2
    random_select_rate = 0.5
     # 编译比例
    mutation_rate = 0.01
    ga = GA(3,20)
    # 转化为[0-9]之间的数据
    chromosome = ga.gen_population(ga.length, ga.count)
    for x in range(100):
        ga.evolve(retain_rate, random_select_rate, chromosome)
    print(ga.result())

# #     测试dec_to_bin函数
#     ga.dec_to_bin(0.4)








