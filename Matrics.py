import numpy as np
import os
from typing import List, Union

class Matrix():
    def __init__(self, data: List[List[Union[int, float]]] | np.ndarray = None) -> None:
        if data is None:
            self.data = [[]]
            self.__rows = 0
            self.__cols = 0
        else:
            if not all(len(row) == len(data[0]) for row in data):
                raise ValueError("All rows must have the same length.")
            if type(data) == np.ndarray:
                self.data =  data.tolist()
            else:
                self.data = data
            self.__rows = len(data)
            self.__cols = len(data[0])

    def __add__(self, a):
        if self._Matrix__rows != a._Matrix__rows or self._Matrix__cols != a._Matrix__cols:
            raise ValueError("Matrices have incorrect dimensions for addition.")
        return Matrix([[self.data[i][j] + a.data[i][j] for j in range(self._Matrix__cols)] for i in range(self._Matrix__rows)])

    def __matmul__(self, a):
        if self._Matrix__cols != a._Matrix__rows:
            raise ValueError("Matrices have incorrect dimensions for matrix multiplication.")
        result = [[0 for _ in range(a._Matrix__cols)] for _ in range(self._Matrix__rows)]
        for i in range(self._Matrix__rows):
            for j in range(a._Matrix__cols):
                for k in range(a._Matrix__rows):
                    result[i][j] += self.data[i][k] * a.data[k][j]
        return Matrix(result)

    def __mul__(self, a):
        if not isinstance(a, (Matrix)):
            raise TypeError("The second operand must be a Matrix.")
        if isinstance(a, Matrix):
            if self._Matrix__rows != a._Matrix__rows or self._Matrix__cols != a._Matrix__cols:
                raise ValueError("Matrices have incorrect dimensions for addition.")
            return Matrix([[self.data[i][j] * a.data[i][j] for j in range(self._Matrix__cols)] for i in range(self._Matrix__rows)])

        return Matrix([[self.data[i][j] * a for j in range(self._Matrix__cols)] for i in range(self._Matrix__rows)])

np.random.seed(0)
a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

with open(os.path.join("artifacts", "3.1", "matrix@.txt"), 'w') as f:
    lst = (a @ b).data
    tmp = list(map(str, lst))
    s = '\n'.join([row for row in tmp])
    f.write(s)
with open(os.path.join("artifacts", "3.1", "matrix+.txt"), 'w') as f:
    lst = (a + b).data
    tmp = list(map(str, lst))
    s = '\n'.join([row for row in tmp])
    f.write(s)
with open(os.path.join("artifacts", "3.1", "matrix_elem_mul.txt"), 'w') as f:
    lst = (a * b).data
    tmp = list(map(str, lst))
    s = '\n'.join([row for row in tmp])
    f.write(s)