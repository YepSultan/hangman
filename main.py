import random

class levelSelection:
    def levelEasy():
        wordlist = ['Cake', 'Coffee', 'Tea', 'China', 'Korea', 'South']
        randWord = random.choice(wordlist)
        index = random.randrange(len(randWord))
        result = randWord[:index] + "_" + randWord[index + 1:]
        print(f"Your Word: ---| {result} |---") 
        userInput = input("Answer: ")
        if userInput == randWord:
            print("Correct!!!")
        else:
            while userInput != randWord:
                print("Try Again")
                print(f"Your Word: ---| {result} |---") 
                userInput = input("Answer: ")
                if userInput == randWord:
                    print("Correct!!!")
                    break

    def levelMedium():
        wordlist = ['Cake', 'Coffee', 'Tea', 'China', 'Korea', 'South']
        randWord = random.choice(wordlist)
        index = random.randrange(len(randWord))
        result = randWord[:index] + "_" + randWord[index + 3:]
        print(f"Your Word: ---| {result} |---") 
        userInput = input("Answer: ")
        if userInput == randWord:
            print("Correct!!!")
        else:
            while userInput != randWord:
                print("Try Again")
                print(f"Your Word: ---| {result} |---") 
                userInput = input("Answer: ")
                if userInput == randWord:
                    print("Correct!!!")
                    break

    def levelHard():
        wordlist = ['Cake', 'Coffee', 'Tea', 'China', 'Korea', 'South']
        randWord = random.choice(wordlist)
        index = random.randrange(len(randWord))
        result = randWord[:index] + "_" + randWord[index + 4:]
        print(f"Your Word: ---| {result} |---") 
        userInput = input("Answer: ")
        if userInput == randWord:
            print("Correct!!!")
        else:
            while userInput != randWord:
                print("Try Again")
                print(f"Your Word: ---| {result} |---") 
                userInput = input("Answer: ")
                if userInput == randWord:
                    print("Correct!!!")
                    break

class hangman:
    def play():
        print("-- Guess the word --")
        lvls = ['Easy', 'Medium', 'Hard']
        print(lvls)
        usr_answ = input('Choose difficulty: ')
        match usr_answ:
            case 0:
                levelSelection.levelEasy()
            case 1:
                levelSelection.levelMedium()
            case 2:
                levelSelection.levelHard()
            


        

            

hangman.play()






