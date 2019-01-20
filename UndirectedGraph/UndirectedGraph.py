import numpy as np



class MatrixUDG:
    def __init__(self, m_vexs, m_matrix):
        self.m_vexs = m_vexs #顶点
        self.m_matrix = m_matrix #边

    def matrix(self, vexs, matrix):
        vexs_length = len(vexs)
        matrix_length = len(matrix)
        make_matrix = np.zeros((vexs_length, vexs_length))
        for i in range(matrix_length):
            index_value = self.get_position(matrix[i])
            make_matrix[index_value[0], index_value[1]] = 1
        print(make_matrix)




    def get_position(self, matrix):
        index = []
        for x in matrix:
            index.append(self.m_vexs.index(x))
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
    matrix.matrix(matrix.m_vexs, matrix.m_matrix)
