import datetime as dt
import os

def clear_scr():
    os.system('CLS')
    
class Leverantor():
    def __init__(self, name, weekday, time):
        self.name = name
        self.weekday = weekday
        self.time = time
        self.done = False
        
        
class run():
    while True:
        now = dt.datetime.now()
        today = dt.date.today() 
        eight = dt.time(20,0,0)

        fristads = dt.datetime.combine(today, eight)

        diff = fristads - now

        print(diff)
        clear_scr()


if __name__ == '__main__':
    go = run()