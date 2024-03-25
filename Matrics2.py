from typing import List, Union
import numpy as np
from Matrics import Matrix
import numbers
import os

class WriterMixin():
    """
    Mixin class that provides a method to save the matrix to a file.
    """
    def save(self, filename: str) -> None:
        """Save the matrix to a file.
        
        Parameters:
            filename (str): The name of the output file.
        Returns:
            None
        """
        # Write the matrix to the file
        with open(f"{filename}.txt", "w") as f:
            f.write(str(self))

class GetSetMixin():
    """
    Mixin class that provides properties to get the rows, columns and data of the matrix and set data of the matrix.
    """
    @property
    def rows(self) -> int:
        """
        The number of rows in the matrix.
        """
        return self._Matrix__rows
    
    @property
    def columns(self) -> int:
        """
        The number of columns in the matrix.
        """
        return self._Matrix__cols

    @property
    def data(self) -> List[List[Union[int, float]]]:
        """
        The data of the matrix as a list of lists.
        """
        return self._data
    
    @data.setter
    def data(self, matrix: List[List[Union[int, float]]] | np.ndarray) -> None:
        """
        Set the data of the matrix.

        Parameters:
            matrix (List[List[Union[int, float]]] | np.ndarray): The new data for the matrix.
        Returns:
            None
        """
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise ValueError("All rows must have the same length.")
        if type(matrix) == np.ndarray:
            self._data =  matrix.tolist()
        else:
            self._data = matrix
        self._Matrix__rows = len(matrix)
        self._Matrix__cols = len(matrix[0])
    
    @columns.setter
    def columns(self, columns_count: int) -> None:
        raise Exception("You are not allowed to set columns number directly. Please set matrix itself.")
    
    @rows.setter
    def rows(self, rows_count: int) -> None:
        raise Exception("You are not allowed to set rows number directly. Please set matrix itself.")

class StrMixin():
    """
    Mixin class that provides a string representation of the matrix.
    """
    def __str__(self):
        res = ""
        for row in self.data:
            res += ("| "+" ".join(str(x).center(4) for x in row) + " |\n")
        return res

class MatrixExtended(np.lib.mixins.NDArrayOperatorsMixin, WriterMixin, StrMixin, GetSetMixin, Matrix):
    # One might also consider adding the built-in list type to this
    # list, to support operations like np.add(array_like, list)
    _HANDLED_TYPES = (np.ndarray, numbers.Number,)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            # Only support operations with instances of _HANDLED_TYPES.
            # Use ArrayLike instead of type(self) for isinstance to
            # allow subclasses that don't override __array_ufunc__ to
            # handle ArrayLike objects.
            if not isinstance(x, self._HANDLED_TYPES + (MatrixExtended,)):
                return NotImplemented

        # Defer to the implementation of the ufunc on unwrapped values.
        inputs = tuple(x.data if isinstance(x, MatrixExtended) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, MatrixExtended) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            # multiple return values
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            # no return value
            return None
        else:
            # one return value
            return type(self)(result)

    def __repr__(self):
        return '%s(%r)' % (type(self).__name__, self.data)

np.random.seed(0)

a = MatrixExtended()
a.data = np.random.randint(0, 10, (10, 10))
b = MatrixExtended()
b.data = np.random.randint(0, 10, (10, 10))

absum = a + b
abmatmul = a @ b
abmul = a * b

absum.save(os.path.join("artifacts", "3.2", "matrix+.txt"))
abmatmul.save(os.path.join("artifacts", "3.2", "matrix@.txt"))
abmul.save(os.path.join("artifacts", "3.2", "matrix_elem_mul.txt"))