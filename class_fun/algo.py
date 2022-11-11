import random
from timeit import default_timer as timer

def gen_list(start, stop, entries):
    print("Generating list...")
    lst = []
    while len(lst) <= entries:
        num = random.randint(start, stop)
        if num not in lst:
            lst.append(num)
        
    return sorted(lst)



def bin_search(val, lst):
    turns = 0
    idx0 = 0
    list_length = len(lst)-1
    idxn = list_length
    while idx0 <= idxn:
        turns+=1
        midval = (idx0 + idxn)//2
        #print(f'midval: {midval}')
        if lst[midval] == val:
            return midval, turns
        if val > lst[midval]:
            idx0 = midval + 1
            #print(f'idx0: {idx0}')
            #print("positive", idx0)
        else:
            idxn = midval - 1
            #print(f'idxn: {idxn}')
            #print("negative", idxn)
        if idx0 > idxn:
            return None, turns

# def lin_search(val, lst):
#     for i in range(len(lst)-1):
#         if lst[i] == val:
#             return val
#         else:
#             return None
    

def lin_search(val, lst):
    turns = 0
    for i in range(0, len(lst)):
        turns+=1
        if lst[i] == val:
            return i, turns
        
    return None, turns



lista1 = gen_list(10,5000000,10000)   
#lista2 = gen_list(10,5000000,10000)  

rand_val1 = random.choice(lista1) 
#rand_val2 = random.choice(lista2) 

mini_lst = [1,2,3,4,5,6,7,8,9,10]

start = timer()  
print("\nLin Search")
print(lin_search(rand_val1, lista1))
end = timer()
print(end - start)

start = timer()
print("\nBin Search")  
print(bin_search(rand_val1, lista1))
end = timer()
print(end - start)

