#!/usr/bin/env python3
import random
def get_try_count():
    while True:
        tries = input("How many incorrect attempts do yo want? [1-25] ")
        try:
            triesValue = int(tries)
            
            if triesValue in range(1,26):
               return triesValue
            else:
                print(tries+ " is not a number between 1 and 25, do your maths boi!?")
        except ValueError:
             print("your input isn't a number.")
    

def get_level():
    while True:
        level = input("What level word do you want? [2-7] ")
        try:
            levelValues = int(level)
            
            if levelValues in range(2,8):
               return levelValues
            else:
                print(level+ " is not a number between 2 and 7, do your maths boi!?")
        except ValueError:
            print("your input isn't a number.")
            
def get_minlen():
    while True:
        minlen = input("What minimum word length do yo want? [4-10] ")
        try:
            minlenValues = int(minlen)
            
            if minlenValues in range(4,11):
               return minlenValues
            else:
                print(minlen+ " is not a number between 4 and 10, do your maths boi!?")
        except ValueError:
            print("your input isn't a number.")
            
 
def get_random_word(level, minlen):
    words= []
    filename = "wordlist_" + str(level) + ".txt"
    try:
        file = open(filename, 'r')
        for line in file:
            word = line.strip().lower()
            if len(word) >= minlen:
                words.append(word)
        randomIndex = random.randint(0, len(words))
        return words[randomIndex]
    except IOError:
        print("can't find the file " + filename)
        return "blahahahah"

def display_info(word, tries):
    validLetters = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    incorrect_guesses = []
    wordLen = len(word)
    guessFlags = [False] *wordLen
    ret = False
    while True:
        maskedWord = []
        for i in range(0,wordLen):
            if guessFlags[i] == False:
                maskedWord +='*'
            else:
                maskedWord += word[i]
        displayWord = ''.join(maskedWord)
        print("\nWord: " + displayWord)
        print("Attempts remaining: " + str(tries))
        print("Previous incorrect guesses: " + ' '.join(incorrect_guesses))
        guess = input("Choose the next letter: ")
        if len(guess) > 1:
            print("must be single letter. try again")
        elif guess not in validLetters:
            print("must be a valid letter. try again")
        elif guess not in word:
            if (guess in incorrect_guesses):
                print("you already guessed it. try again")
            else:
                incorrect_guesses.append(guess)
                tries -= 1
                if tries == 0:
                    print('Too bad. You lost! the word was: ' +word)
                    tryAgain = input("Try again?[y/Y]")
                    if tryAgain.lower() == 'y':
                       ret = True
                    break
                else:
                    continue
        else:
            count = 0
            for i in range(0,wordLen):
                if word[i] == guess:
                    guessFlags[i] = True
                if guessFlags[i] == True:
                    count += 1
            if count == wordLen:
                print('Congratulation! the word was: ' +word)
                tryAgain = input("You won! try again?[y/Y]")
                print()
                if tryAgain.lower() == 'y':
                    ret = True
                break
    return  ret              
          
def hangman():
    print("Welcome to hangman game, made by ME")
    while True:
        tries = get_try_count()
        print("Current input attempts is: " + str(tries))
        level = get_level()
        print("Current input level is: " +str(level))
        minlen = get_minlen()
        print("Current input minimum word length is: " +str(minlen))
        word = get_random_word(level, minlen)
        try_Again = display_info(word, tries)
        if try_Again == False:
            break
    
        
if __name__ == "__main__":
    hangman()
