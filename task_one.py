import math
startingSize = 11


def sorting_task_a(arr):
    operatedArr = [0] * startingSize
    if startingSize%2 == 0:
        middleOne = math.floor(startingSize/2)-1
        middleTwo = math.floor(startingSize/2)
        operatedArr[middleTwo] = arr[0]  # because it's sorted in ascending order
        operatedArr[middleOne] = arr[1]
        i = 1
        operatedArr[middleOne - i] = arr[2]
        i = 4
        r = range(2, (middleOne+1))
        #  left side
        for x in r:
            operatedArr[middleOne - x] = arr[i]
            i += 2
        # right side
        m = range(1, (middleOne+1))
        i = 3
        for x in m:
            operatedArr[middleTwo + x] = arr[i]
            i += 2
    else:
        middle = math.floor(startingSize/2)  # center = arr.length/2
        operatedArr[middle] = arr[0]  # our array is sorted in descendant order - look there
        # sorting
        i = 1
        operatedArr[middle - i] = arr[i]
        i = 3
        r = 1
        # left side
        while r < middle:
            r += 1
            operatedArr[middle - r] = arr[i]
            i += 2
        i = 2
        r = 1
        # right side
        while r <= middle:
            operatedArr[middle + r] = arr[i]
            r += 1
            i += 2
    return operatedArr


def sorting_task_b(sorted_asc, sorted_desc):
    operated_arr = [0] * startingSize
    # for odd size array
    if startingSize % 2 == 0:
        n = 0
        middle = math.floor(len(operated_arr)/2)
        for x in range(0, middle):
            operated_arr[n] = sorted_desc[x]
            n += 2
        n = 1
        for x in range(0, middle):
            operated_arr[n] = sorted_asc[x]
            n += 2
    else:
        r = 0
        middle = math.floor(len(operated_arr)/2)
        for x in range(0, middle+1):
            operated_arr[r] = sorted_desc[x]
            r += 2
        r = 1
        for x in range(0, middle):
            operated_arr[r] = sorted_asc[x]
            r += 2
    return operated_arr


def sorting_task_c(arr):
    with_even_index = list()
    with_odd_index = list()
    operated_arr = list()
    for x in range(0, len(arr), 2):
        with_odd_index.append(arr[x])
    for x in range(1, len(arr), 2):
        with_even_index.append(arr[x])
    with_even_index.sort()
    with_even_index.reverse()
    with_odd_index.sort()
    operated_arr.extend(with_even_index)
    operated_arr.extend(with_odd_index)
    return operated_arr
