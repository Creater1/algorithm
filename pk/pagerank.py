import numpy as np
import pk.DirectNet as DN
import random
#
# def __init__(self, node_name, node_value, wight):
#         self.node_name = node_name
#         self.node_value = node_value
#         self.weight = wight

def pageRank(matrix, cvt_matrix, d, r):
    """
    :param matrix: 邻接矩阵
    :param convert_matrx: 转移矩阵
    :param d: 参数
    :param r 阻尼因子
    :return:
    """
    matrix_length = len(matrix)
    # 每一行相加
    axix_plus = np.sum(matrix, axis=1)
    node_and_pr = 0
    normal = 2
    New_P = []
    e = []
    for i in range(matrix_length):
        e.append(1)
        New_P.append([random.random()])
    c = [[(1 - d) * i * 1 / matrix_length] for i in e]
    print(cvt_matrix)
    while normal > r:
        d = New_P
        cvt_result = matrix_multi(cvt_matrix, np.array(New_P))
        New_P = matrix_add(cvt_result, np.array(c))
        normal = 0
        # 求解矩阵一阶范数
        for i in range(matrix_length):
            normal += abs(New_P[i][0] - d[i][0])
    print(New_P)

def  matrix_add(cvt_result, r):
    return cvt_result + r


def matrix_multi(cvt_matrix, New_P):
    result = cvt_matrix * New_P
    return result





if __name__ == '__main__':
    node = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'F'],
            ['B', 'C'],
            ['C', 'D'],
            ['E', 'G'],
            ['F', 'G'],
            ['C', 'A']]
    weigth = [1,2,3,4,5,6,7]
    matrix = DN.DirectNet(node, edges, weigth)
    adjacent_matrix = matrix.con_matrix()
    convert_matrix = matrix.tran_and_convert(adjacent_matrix)
    pageRank(adjacent_matrix, convert_matrix, 0.25, 0.0001)