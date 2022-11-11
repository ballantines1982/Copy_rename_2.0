from getkey import getkey, keys
import os

def clear_scr():
    """Rensar terminalen"""
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def main():        

    menyOptions = ["First\t", "Second\t", "Third\t", "Quit\t"]
    selectedOption = 0

    while True:
        clear_scr()
        if selectedOption == 0:
            print(menyOptions[0] + "<--")
            print(menyOptions[1])
            print(menyOptions[2])
            print(menyOptions[3])
        elif selectedOption == 1:
            print(menyOptions[0])
            print(menyOptions[1] + "<--")
            print(menyOptions[2])
            print(menyOptions[3])
        elif selectedOption == 2:
            print(menyOptions[0])
            print(menyOptions[1])
            print(menyOptions[2] + "<--")
            print(menyOptions[3])
        elif selectedOption == 3:
            print(menyOptions[0])
            print(menyOptions[1])
            print(menyOptions[2])
            print(menyOptions[3] + "<--")

        keyPressed = getkey()
        if keyPressed == keys.DOWN and selectedOption +1 != len(menyOptions):
            selectedOption += 1
        elif keyPressed == keys.UP and not (selectedOption == 0):
            selectedOption -= 1
        elif keyPressed == keys.ENTER:
            if selectedOption == 0:
                print("\nFirst Choise")
                input("Press Enter to continue...")
            elif selectedOption == 1:
                print("\nSecond Choise")
                input("Press Enter to continue...")
            elif selectedOption == 2:
                print("\nThird Choise")
                input("Press Enter to continue...")
            elif selectedOption == 3:
                print("\nTerminate program!")
                break
            
if __name__ == "__main__":
    main()