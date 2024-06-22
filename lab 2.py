numbers = ["nm,jm,sh"]


def out_of_scope(nitesh_list):
    nitesh_list.append(100)
    return nitesh_list


l = out_of_scope(numbers)
print(l)
