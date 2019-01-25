import numpy as np



class MatrixUDG:
    def __init__(self, m_vexs, m_matrix):
        self.m_vexs = m_vexs #顶点
        self.matrix_edge = m_matrix #边

    def matrix(self, vexs):
        vexs_length = len(vexs)
        matrix_edge_length = len(self.matrix_edge)
        make_matrix = np.zeros((vexs_length, vexs_length))
        for i in range(matrix_edge_length):
            print(self.matrix_edge[i])
            x = self.get_position(self.matrix_edge[i][0])
            y = self.get_position(self.matrix_edge[i][1])
            make_matrix[x, y] = 1
        print(make_matrix)

    def get_position(self, matrix):
        index = 0
        for x in self.m_vexs:
            if x == matrix:
                index = self.m_vexs.index(x)
        return index



if __name__ == '__main__':
    vexs = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'F'],
            ['B', 'C'],
            ['C', 'D'],
            ['E', 'G'],
            ['F', 'G']]
    matrix = MatrixUDG(vexs, edges)
    matrix.matrix(matrix.m_vexs)
