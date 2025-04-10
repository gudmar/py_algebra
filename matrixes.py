from utils import *
from typing import List, Union, Type

class Matrix:
    def __init__(self, *rows):
        verifyDimentions(rows)
        self.data = []
        for row in rows:
            if len(row) > 0: self.data.append(row)

    def row_to_str(self, index):
        str_elements = [str(element) for element in self.data[index]]
        return str_elements

    def __str__(self) -> str:
        rows = [row_to_str(row) for row in self.data]
        indentet_rows = indent_middle_rows(rows)
        content = ',\n'.join(indentet_rows);
        return wrap_in_squares(content)

    def get_size(self):
        return matrix_size(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()

    def transpose(self):
        self.data = transpose(self.data)
        return self.data

    def transposed(self):
        return transpose(self.data)

    def __add__(self, other):
        operation = lambda a, b: a + b
        result = do_with_same_sized_matrixes(self.data, other.data, operation)
        return Matrix(*result)

    def __mul__(self, other: Union[float, 'Matrix']) -> 'Matrix':
        operation = lambda a, b: a * b
        result = do_with_same_sized_matrixes(self.data, other.data, operation)
        return Matrix(*result)

    def __div__(self, other: Union[float, 'Matrix']) -> 'Matrix':
        operation = lambda a, b: a / b
        result = do_with_same_sized_matrixes(self.data, other.data, operation)
        return Matrix(*result)

    def __sub__(self, other):
        operation = lambda a, b: a - b
        result = do_with_same_sized_matrixes(self.data, other.data, operation)
        return Matrix(*result)

    def __mod__(self, other):
        operation = lambda a, b: a % b
        result = do_with_same_sized_matrixes(self.data, other.data, operation)
        return Matrix(*result)






if __name__ == "__main__":

    unit_arr = Matrix([1, 0, 0], [0, 1, 0], [0, 0, 1])

    print('...testing get_size')
    arr_3_2 = Matrix([1,2,3], [4,5,6])
    arr_0_0 = Matrix([])
    arr_0_2 = Matrix([], [])
    arr_empty = Matrix()
    assert arr_3_2.get_size() == (3, 2), "arr_3_2.get_size() received {}".format(arr_3_2.get_size())
    assert arr_0_0.get_size() == arr_empty.get_size() == (0, 0), "arr_empty is {} while arr_0_0 is {}".format(arr_empty.get_size(), arr_0_0.get_size())
    assert arr_0_2.get_size() == (0, 0), "arr_0_2 is {}".format(arr_0_2.get_size())
    print('get_size tests passed')

    print('...testing __add__')
    add_arr_A = Matrix([1,2,3], [4,5,6])
    add_arr_B = Matrix([3,2,1], [6,5,4])
    addition_A_B = Matrix([4,4,4], [10, 10, 10])
    result_A_B = add_arr_A + add_arr_B
    assert result_A_B.data == addition_A_B.data, "Matrixes A and B not added properly"
    try:
        add_wrong_dim_A = Matrix([1,2,3], [4,5,6])
        add_wrong_dim_B = Matrix([1,2] [3,4], [5,6])
        result = add_wrong_dim_A + add_wrong_dim_B
    except:
        print('...wrong dimention array addition passed')

    print('__add__ tests passed')

    print('\n____________________________')
    print('All tests of matrixes passed')
    
