class ObjectOne():
    class_var = 'Original'
    def __init__(self):
        self.inheritance_var = 1


class ObejctTwo():
    def changeClassVar():
        ObjectOne.class_var = 'Changed'

        
if __name__ == '__main__':
    one = ObjectOne
    print(one.class_var)
    two = ObejctTwo
    two.changeClassVar()
    print(one.class_var)
