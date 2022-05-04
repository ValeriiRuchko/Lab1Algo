

def task_4():
    op_arr_1 = {5, 2, 8, 9}
    op_arr_2 = {5, 1, 9, 11}
    print("Op_arr_1:", op_arr_1)
    print("Op_arr_2:", op_arr_2)
    print("Union:")
    print(op_arr_1.union(op_arr_2))
    print("Intersection:")
    print(op_arr_1.intersection(op_arr_2))
    print("Complementary:")
    print(op_arr_1.union(op_arr_2) - op_arr_1)
    print("Difference:")
    print(op_arr_1 - op_arr_2)
    print("Symmetric difference:")
    print(op_arr_1.union(op_arr_2) - op_arr_1.intersection(op_arr_2))
