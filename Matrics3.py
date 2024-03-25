from Matrics import Matrix
import numpy as np
import copy
import os

def write_to_file(name: str, matrix: Matrix) -> None:
    with open(os.path.join("artifacts", "3.3", name), 'w') as f:
        lst = matrix.data
        tmp = list(map(str, lst))
        s = '\n'.join([row for row in tmp])
        f.write(s)

class HashMixIn():
    def __hash__(self) -> int:
        """
        Return sum of hashes of matrix elements.
        hash(int) returns the value itself -> 2 different int matrices with equal element sum will 
        have same hash -> collision
        """
        # Складываем значения hash() для каждого элемента матрицы
        hash_value = 0
        for row in self.data:
            for item in row:
                hash_value += hash(item)
        
        return hash_value

class MatrixWithHash(HashMixIn, Matrix):
    # Кэширование произведения матриц
    is_cache = True
    cache = {}

    def __matmul__(self, a):
        result = super().__matmul__(a)
        if self.is_cache:

            hash_value1 = hash(self)
            hash_value2 = hash(a)
            
            key = (hash_value1, hash_value2)
            if key in self.cache:
                return MatrixWithHash(self.cache[key].data)
            self.cache[key] = result
        return MatrixWithHash(result.data)



a = MatrixWithHash([[1, 2],[3, 4]])
b = MatrixWithHash([[10, 11], [12, 13]])
c = MatrixWithHash([[4, 2],[1, 3]])
d = copy.copy(b)
ab = a @ b

# Отключаем кэширование чтобы получить правильный результат
# Если оставить True, получим ab == cd и hash(ab) == hash(cd)
MatrixWithHash.is_cache = False

cd = c @ d

for filename, matrix in zip(("A", "B", "C", "D", "AB", "CD"), (a, b, c, d, ab, cd)):
    write_to_file(filename + ".txt", matrix)

with open(os.path.join("artifacts", "3.3",'hash.txt'), 'w') as f:
    f.write(f"AB hash = {str(hash(ab))}\n")
    f.write(f"CD hash = {str(hash(cd))}\n")

