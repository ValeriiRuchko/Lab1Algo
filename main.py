import copy
import random
from task_one import *
from task_two import *


if __name__ == '__main__':
    # generate one-dimensional array
    numbers = list()
    i = 0
    while i < startingSize:
        randNum = math.floor(random.random()*100+1)
        numbers.append(randNum)
        i += 1
    print("Our generated array:", numbers)
    const_arr = numbers.copy()
    minValue = min(numbers)
    maxValue = max(numbers)
    print("Minimal value is:", minValue)
    print("Maximum value is:", maxValue)
    # TASK 1
    # ascending order sort
    numbers.sort()
    print("Sorted in ascending order array:", numbers)
    res = sorting_task_a(numbers)
    print("Task A (ascending):", res)
    # descending order sort
    numbers.reverse()
    print("Sorted in descending order array:", numbers)
    res = sorting_task_a(numbers)
    print("Task A (descending):", res)
    # task Б
    numbers.sort()
    asc = numbers.copy()
    numbers.reverse()
    desc = numbers.copy()
    res = sorting_task_b(asc, desc)
    print("Task B:", res)
    # task В
    numbers = const_arr.copy()
    res = sorting_task_c(numbers)
    print("Task C:", res)
    # TASK 2
    # generate two-dimensional array
    matrix = [[math.floor(random.random()*100+1) for x in range(sizeOfMartix)] for y in range(sizeOfMartix)]
    const_matr = copy.deepcopy(matrix)
    print()
    print("Our matrix is:")
    print_matrix(matrix)
    listOfMins = list()
    listOfMaxes = list()
    for x in matrix:
        tempMin = min(x)
        listOfMins.append(tempMin)
        tempMax = max(x)
        listOfMaxes.append(tempMax)
    trueMin = min(listOfMins)
    trueMax = max(listOfMaxes)
    print("Minimal value of matrix is:", trueMin)
    print("Maximum value of matrix is:", trueMax)
    # Task A
    task_a(matrix)
    print("Task A:")
    print_matrix(matrix)
    # Task Б
    matrix = copy.deepcopy(const_matr)
    print("Task B:")
    print_matrix(task_b(matrix))
    # Task В
    matrix = copy.deepcopy(const_matr)
    print("Task C:")
    task_c(matrix)
