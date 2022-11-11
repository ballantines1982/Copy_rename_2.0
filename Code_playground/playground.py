import time
import os


dir = r'C:\Python Projekt'
data = os.listdir(dir)

def rjust(list):
    lenList = []
    for i in list:
        x = len(i)
        lenList.append(x)
        lenList.sort()
    largest_file = lenList[-1]
    return largest_file
    

def oneline(arg):
    for item in arg:
        line = 'Files: ' + item.rjust(rjust(data))
        print(line, end='')
        print('\b' * len(line), end='', flush=True)
        time.sleep(0.07)   
    print('\nDone')
    print('Press enter to exit..')
    input()

maps = 0
exten = []
for files in data:
    x = os.path.splitext(files)
    y = x[0]+x[1]
    if x[1] == '':
        maps+=1
        continue
    else:
        print(y)
print(f"{str(maps)} maps where ignored")
oneline(data)
