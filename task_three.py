import numpy as np
import numpy.random

sizeOfThreeD = 5


def generate_3d_array():
    three_d_arr = numpy.random.randint(1, 101, (sizeOfThreeD, sizeOfThreeD, sizeOfThreeD))
    return three_d_arr


def task_3():
    operated_arr = generate_3d_array()
    flattend_arr = operated_arr.flatten()
    minimal = min(flattend_arr)
    maximum = max(flattend_arr)
    print("Minimal value is:", minimal)
    print("Maximum value is:", maximum)
    print("Sorted by first axis:")
    res = numpy.sort(operated_arr, 0)
    print(res)
    print("Sorted by second axis:")
    res = numpy.sort(operated_arr, 1)
    print(res)
    print("Sorted by third axis:")
    res = numpy.sort(operated_arr, 2)
    print(res)
