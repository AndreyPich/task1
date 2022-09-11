import time
from typing import Any
import copy


def fibonacci_rec(num: int) -> int:
    if num == 1:
        return 0
    if num == 2:
        return 1
    if num > 2:
        return fibonacci_rec(num - 1) + fibonacci_rec(num - 2)


def fibonacci_iter(num: int) -> int:
    if num == 1:
        return 0
    if num == 2:
        return 1
    fib = 0
    fib2 = 1
    for i in range(num - 2):
        fib2 = fib2 + fib
        fib = fib2 - fib
    return fib2


def determinant(matrix: [[int]]) -> int:
    if len(matrix) == 0: raise Exception
    if not checkmatrix(matrix): raise Exception
    if len(matrix) == 1: return matrix[0][0]
    size = len(matrix)
    if size == 2: return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    return det_minor(matrix)


def checkmatrix(matrix: [[int]]):
    for x in range(len(matrix)):
        if len(matrix) != len(matrix[x]):
            return False
    return True


def zero_line(matrix: [[int]]) -> int:
    max_count = 0
    line_number = 0
    for i in range(len(matrix)):
        count = 0
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                count += 1
        if count > max_count:
            max_count = max(max_count, count)
            line_number = i
    return line_number


def det_minor(matrix: [[int]]):
    sum=0
    line=zero_line(matrix)
    for x in range(len(matrix)):
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        new_matr = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matr[line][i]=None
                new_matr[j][x]=None
        for i in range(len(matrix)):
            new_matr[i] = list(filter(None, new_matr[i]))
        new_matr.pop(line)
        sum += ((-1) ** (x + line) * matrix[line][x] * det_minor(new_matr))
    return sum


def print_exec_time(func: callable(object), **kwargs: dict[str: Any]) -> None:
    start_time = time.time()
    func(**kwargs)
    print(f'duration: {time.time() - start_time} seconds')


def main():
    for num in [10, 20, 30, 35]:
        print_exec_time(lambda x: print(x, fibonacci_rec(x)), x=num)

    matrix = [[1, 2],
              [3, 4]]
    print(f'determinant: {determinant(matrix)}')


if __name__ == '__main__':
    main()
