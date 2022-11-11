
def numbers(*args):
    total=1
    for num in args:
        total*=num
    return total

#print(numbers(1,2,3,4,5,6,7,8,9,10))

def dict_test(**kwargs):
    print(len(kwargs))

dict_list = {'peter': 39, 'Sara': 32}

print(dict_test(**dict_list))
