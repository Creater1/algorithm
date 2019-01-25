import numpy as np


class DirectNet:
    def __init__(self, node, edge, weight):
        """
        点、边、权重三个
        :param node:
        :param edge:
        :param weight:
        """
        self.node = node #点
        self.edge = edge #边
        self.weight = weight #权重

    def con_matrix(self):
        """
        构造邻接矩阵
        :return:
        """
        node_number = len(self.node)
        matrix_edge_length = len(self.edge)
        make_matrix = np.zeros((node_number, node_number))
        for i in range(matrix_edge_length):
            x = self.get_position(self.edge[i][0])
            y = self.get_position(self.edge[i][1])
            make_matrix[x, y] = 1
        # print(make_matrix)
        return make_matrix


    def get_position(self, matrix):
        """
        获取顶点的位置
        :param matrix:
        :return:
        """
        index = 0
        for x in self.node:
            if x == matrix:
                index = self.node.index(x)
                break
            else:
                continue
        return index

    def tran_and_convert(self, matrix):
        """
        构建转移矩阵
        :param matrix: 邻接矩阵
        :return:
        """
        edges_number = len(self.edge)
        matrix_length = len(matrix)
        result_convert = [[0] * matrix_length for i in range(matrix_length)]
        for x in range(matrix_length):
            for j in range(matrix_length):
                result_convert[x][j] = matrix[j][x]
        result_convert = np.mat(result_convert)
        return result_convert * (1 / edges_number)



