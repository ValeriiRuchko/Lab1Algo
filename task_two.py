import math
import numpy as np
sizeOfMartix = 5  # size of our two-dimensional matrix


def print_matrix(matr):
    for x in matr:
        for y in x:
            print(y, end=' ')
        print()


def task_a(matr):
    for x in matr:
        x.sort()
    return matr


def task_b(matr):
    temp = list()
    operated_arr = [[0 for x in range(sizeOfMartix)] for y in range(sizeOfMartix)]
    for x in range(0, sizeOfMartix):
        for y in range(0, sizeOfMartix):
            temp.append(matr[y][x])
        temp.sort()
        r = 0
        for n in temp:
            operated_arr[r][x] = n
            r += 1
        temp.clear()
    return operated_arr


def task_c(matr):
    temp = list()
    for x in range(0, sizeOfMartix):
        for y in range(0, sizeOfMartix):
            temp.append(matr[x][y])
    temp.sort()
    operated_arr = [[0 for x in range(sizeOfMartix)] for y in range(sizeOfMartix)]

    return operated_arr
