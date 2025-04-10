from typing import Optional, List;
from matrixes import Matrix

class Algebra:
    @staticmethod
    def zero_matrix(width: int, height=None):
        def row():
            return [0 for _ in range(width)]
        arr = [row() for _ in range(height or width)]
        matrix = Matrix(*arr)
        return matrix

    @staticmethod
    def one_matrix(width: int, height=None):
        arr_row = lambda: [1 for _ in range(width)];
        arr = [arr_row() for _ in range(height or width)]
        matrix = Matrix(*arr)
        return matrix

    @staticmethod
    def identity_matrix(size: int):
        arr_row = lambda row_index: [1 if col_index == row_index else 0 for col_index in range(size)]
        arr = [arr_row(index) for index in range(size)]
        matrix = Matrix(*arr)
        return matrix

    @staticmethod
    def matrix_from_list_of_lists(matrix: List[List[float]]):
        result = Matrix(*matrix)
        return result


if __name__ == '__main__':
    assert Algebra.zero_matrix(3, 2).__str__() == '[ [ 0, 0, 0 ],\n  [ 0, 0, 0 ] ]', 'Failed to create a zero_matrix array'
    assert Algebra.zero_matrix(3).__str__() == '[ [ 0, 0, 0 ],\n  [ 0, 0, 0 ],\n  [ 0, 0, 0 ] ]', 'Failed to create a zero_matrix array when height is not given'

    assert Algebra.one_matrix(2, 3).__str__() == '[ [ 1, 1 ],\n  [ 1, 1 ],\n  [ 1, 1 ] ]', 'Failed to create a ones matrix array'
    assert Algebra.one_matrix(2).__str__() == '[ [ 1, 1 ],\n  [ 1, 1 ] ]' , 'Failed to create a no heigh array'

    assert Algebra.identity_matrix(4).__str__() == '[ [ 1, 0, 0, 0 ],\n  [ 0, 1, 0, 0 ],\n  [ 0, 0, 1, 0 ],\n  [ 0, 0, 0, 1 ] ]', 'Failed to create an identity matrix'

    assert Algebra.matrix_from_list_of_lists([[1, 2]]).__str__() == '[ [ 1, 2 ] ]', 'Failed to create a matrix from single row matrix'

    print('All tests passed')
