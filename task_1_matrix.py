# Создайте класс Матрица. 
# Добавьте методы для: вывода на печать, 
# сравнения, сложения, *умножения матриц

from os import system
system('cls')
import numpy as np

class Matrix:
    def __init__(self, row1: list, row2: list, row3: list) -> None:
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

    def matrix_create(self):
        return np.array([self.row1, self.row2, self.row3])

    def __add__(self, other):
        return self.matrix_create() + other.matrix_create()
    
    def __mul__(self, other):
        return self.matrix_create().dot(other.matrix_create())
    
    def __eq__(self, other) -> bool:
        if np.array_equal(self.matrix_create(), other.matrix_create()):
            return True
        return False
    
    def __gt__(self, other) -> bool:
        return self.matrix_create() > other.matrix_create()
    
    def __lt__(self, other) -> bool:
        return self.matrix_create() < other.matrix_create()
    
    def __str__(self):
        return f'Экземпляр класса Matrix, имеет вид: \n{self.matrix_create()}'
    
    def __repr__(self):
        return f'Matrix[{self.row1}, {self.row2}, {self.row3}]'

matr1 = Matrix([1, 2, 3], [10, 20, 30], [100, 200, 300])
matr2 = Matrix([4, 5, 6], [40, 50, 60], [400, 500, 600])

print(matr1)
print(matr2)

print(repr(matr1))
print(repr(matr2))

print(f'Сумма двух матриц:\n{matr1 + matr2}')
print(f'Произведение двух матриц:\n{matr1 * matr2}')

print(f'Результат сравнения на эквивалентность: {matr1 == matr2}')
print(matr1 > matr2)
print(matr1 < matr2)