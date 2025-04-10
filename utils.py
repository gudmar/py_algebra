from typing import Optional, List;
from type_definitions import *
WRONG_MATRIX_DIMENTION_ERROR_MESSAGE = "All rows in a matrix have to have the same size"

def is_number(val):
    number_types = ["<class 'int'>", "<class 'float'>", "<class 'complex'>"]
    return any(number_type == '{}'.format(type(val)) for number_type in number_types)

def verifyDimentions(*rows):
    if len(rows) == 0 or len(rows) == 1:
        return True
    for row in rows:
        assert len(row) == len(rows[0]), WRONG_MATRIX_DIMENTION_ERROR_MESSAGE
    return True

def indent_middle_rows(arr: List[str]):
    indention = '  '
    if len(arr) < 2:
        return arr
    new_arr = [ (indention if index > 0 else '') + row for (index, row) in enumerate(arr) ]
    return new_arr
    

def wrap_in_squares(text: str):
    return '[ ' + text + ' ]'

def row_to_str(row: List[float]):
    list_of_strings = [str(element) for element in row]
    joined_list = ', '.join(list_of_strings)
    return wrap_in_squares(joined_list)

def transpose(matrix: List[List[numeric]]):
    return [[row[col_index] for row in matrix] for col_index in range(len(matrix[0]))] if len(matrix) != 0 else []
    # if (len(matrix) == 0): return [] 
    # # nr_cols = len(matrix[0])
    # return [[row[col_index] for row in matrix] for col_index in range(len(matrix[0]))]
    # transposed = []
    # for col_index in range(nr_cols):
    #     transposed_row = []
    #     for row in matrix:
    #         transposed_row.append(row[col_index])
    #     transposed.append(transposed_row)
    # return transposed

def matrix_size(matrix: List[List[numeric]]) -> tuple:
    return (len(matrix[0]), len(matrix)) if len(matrix) != 0 else (0, 0)

def same_shape(matrix_1, matrix_2, message):
    assert matrix_size(matrix_1) == matrix_size(matrix_2), message

def do_with_same_sized_matrixes(matrix_1: matrix_type, matrix_2: matrix_type, operation: matrix_operation_type) -> matrix_type:
    same_shape(matrix_1, matrix_2, 'Matrixes should have the same shapes')
    result = [[ operation(matrix_1_row_item, matrix_2[row_index][col_index]) for (col_index, matrix_1_row_item) in enumerate(row)] for (row_index, row) in enumerate(matrix_1)]
    return result





if __name__ == '__main__':
    print('Testing is_number')
    assert is_number(4) == True, "4 should be a number, but is not: {}".format(type(4))
    assert is_number(5j) == True, "5j should be a number, but is not"
    assert is_number(0.22) == True, '0.22 should be a number, but is not'
    assert is_number([]) == False, '[] should not be a number'
    assert is_number('asfde') == False, 'a string should not be a number'
    assert is_number(None) == False, 'None should not be a number'
    assert is_number(True) == is_number(False) == False, 'A boolean should not be a number'
    assert is_number((3, 4)) == False, 'A tuple should not be a number'
    assert is_number({}) == False, 'A dictionary shold not be a number'

    print('Test verifyDimentions')

    assert verifyDimentions([0,0,0], [0,0,0]), "1) test"
    try:
        assert verifyDimentions([0,0,0], [0,0,0], [1,1]), "2) test"
    except:
        print('Array dimentions are different, and this is expected')
    assert verifyDimentions([0])
    assert verifyDimentions([])

    print('Testing transpose')
    assert transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]], 'Should transpose a 2x3 matrix'
    assert transpose([[7]]) == [[7]], 'Should transpose 1x1 matrix'
    assert transpose([]) == [], 'Should transpose an empty matrix'


    print('All tests passed')
