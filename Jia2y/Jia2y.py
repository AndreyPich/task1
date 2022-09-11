import time
from typing import Any

# Рекурсивная реализация
def fibonacci_rec(num: int) -> int:
    if num == 0: return 0
    if num == 1: return 1
    return fibonacci_rec(num-1) + fibonacci_rec(num-2)
# Итерационная реализация
def fibonacci_iter(num: int) -> int:
    if num == 0: return 0
    if num == 1: return 1
    fib = 0;
    fib2 = 1;
    for i in range (num-1):
        fib2 = fib2 + fib
        fib = fib2 - fib
    return fib2
# Определитель матрицы
def determinant(matrix: [[int]]) -> int:
    if matrix == 0: return Exception
    if matrix == 1: return matrix[0][0] 
    size = len(matrix)
    if size == 2: return x2(matrix) # если матрица 2х2
    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))
# возвращает определитель квадратной матрицы 2х2
def x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
# минор
def minor(matrix, i, j):
    matr = [row for t, row in enumerate(matrix) if t != i]
    matr = [col for t, col in enumerate(zip(*matr)) if t != j]
    return matr


