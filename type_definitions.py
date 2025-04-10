from typing import Union, List, Callable

numeric = Union[int, float, complex]

matrix_type = List[List[numeric]]

matrix_operation_type = Callable[[numeric, numeric], numeric]
