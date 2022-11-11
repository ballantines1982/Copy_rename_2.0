def list_fun(list,a,b):

    if list.index(b) - list.index(a) == 1:
        return True
    return False

print("lista 1 " + str(list_fun([1,2,3,4,5,6], 3, 5)))
print("lista 2 " + str(list_fun([1,2,3,4,5,6], 3, 4)))
print("lista 3 " + str(list_fun([2,4,6,8,10,12], 4, 6)))