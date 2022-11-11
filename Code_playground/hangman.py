import random


print("Hangman")
print("-------")
print("Du har 3 liv")

wordList = ['peter', 'ellen', 'sara', 'alice', 'richard', 'jennie', 'martin', 'arvid', 'ludwig', 'ullabritt', 'maya', 'elsebeth', 'gert', 'jimmy']

randword = random.choice(wordList)


emptyWord = []
for i in range(len(randword)):
    emptyWord.append('_')
userWord = []
print(emptyWord)
counter = 0
while True:
    userGuess = input("Gissa en bokstav: ").lower()
    if userGuess in randword:
        positions = [pos for pos, char in enumerate(randword) if char == userGuess]
        print(userGuess + ' finns med!')
        
        for pos in positions:
            emptyWord.pop(pos)
            emptyWord.insert(pos, userGuess)
    else:
        print(userGuess + ' är fel')
        counter+=1

    if '_' not in emptyWord:
        print("Du klarade det!!")
        print(emptyWord)
        break
    elif counter >= 3:
        print("Game Over!")
        break 


    print(emptyWord)