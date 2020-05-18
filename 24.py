import random
import re
import time


def get_rules():
    rules = input("Do you know how to play the game 24? [y/Y] ")
    if rules.lower() != 'y':
        print("In 24, there are four numbers from 1 through to 13.\n" +
              "You need to try and get the number 24 using all of the numbers.\n" +
              "You can only add, subtract, multiply or divide.\n" +
              "Not all of the number groups can form 24, so you can press N for a new game.\n" +
              "If you made a mistake you can press R to redo the current number group.\n" +
              "Challenge yourself and have fun!"
              )


def getNewNumbers():
    numbers = []
    for i in range(0, 4):
        numbers.append(random.randint(1, 13))
    return numbers


def doMath(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return abs(n1 - n2)
    elif op == '*' or op == 'x':
        return n1 * n2
    else:
        if n1 < n2:
            t = n1
            n1 = n2
            n2 = t
        if n1 % n2 == 0:
            return int(n1 / n2)
        else:
            return -1
    return -1


def getNewTarget(n1, n2, r, numbers):
    temp = []
    temp.append(r)
    found1 = -1
    for i in range(0, len(numbers)):
        if n1 == numbers[i]:
            found1 = i
            break

    found2 = -1
    for i in range(0, len(numbers)):
        if n2 == numbers[i]:
            if found1 == i:
                continue
            found2 = i
            break
    for i in range(0, len(numbers)):
        if(i != found1 and i != found2):
            temp.append(numbers[i])

    return temp


def exist(n1, n2, numbers):
    found = -1
    for i in range(0, len(numbers)):
        if n1 == numbers[i]:
            found = i
            break
    if found == -1:
        return False

    found2 = -1
    for i in range(0, len(numbers)):
        if n2 == numbers[i]:
            if found == i:
                continue
            found2 = i
            break
    return found2 != -1


def printStat(guessRight, totalGuess, streak, start):
    print("Correct/Total: " + str(guessRight) + "/" +
          str(totalGuess) + " Streak: " + str(streak))
    duration = int(time.time() - start)
    min = int(duration / 60)
    sec = int(duration % 60)
    print("Duration: " + 
          ("" if min == 0 else str(min) + " minutes ") +
          ("" if sec == 0 else str(sec) + " seconds"))


def play24():
    get_rules()
    guessRight = 0
    totalGuess = 0
    streak = 0
    newGame = True
    numbers = []
    regenerate = False
    gameStart = time.time()
    while newGame == True:
        result = 0
        start = time.time()
        if len(numbers) == 0 or regenerate == True:
            numbers = getNewNumbers()
        target = numbers
        skip = False
        # The numbers are : a b c d. Enter R(edo), P(ass) or math operation with two numbers to continue
        while len(target) != 1:
            userInput = input("\n--------------- #" + str(totalGuess+1)+" ---------------" +
                              "\nThe numbers are: " + " ".join(map(str, target)) +
                              ".\nEnter R(redo), N(New game), Q(quit)\n" +
                              "Or + - * / with two numbers:").lower()
            if userInput == 'q':
                newGame = False
                skip = True
                break

            elif userInput == 'n':
                skip = True
                regenerate = True
                totalGuess += 1
                streak = 0
                printStat(guessRight, totalGuess, streak, start)
                break

            elif userInput == 'r':
                skip = True
                regenerate = False
                break

            else:
                z = re.match(r'(\d{1,2})([\+\-\*x\/])(\d{1,2})', userInput)
                if z:
                    n1 = int(z.group(1))
                    op = z.group(2)
                    n2 = int(z.group(3))

                    if exist(n1, n2, target):
                        r = doMath(n1, n2, op)
                        if r == -1:
                            print(userInput + ": incorrect math. please try again")
                            continue
                        result = r
                        target = getNewTarget(n1, n2, r, target)
                        continue
                    else:
                        print(userInput + ":invalid input. Both numbers must exist in the list above. please try again")
                        continue

                else:
                    print(userInput + ":invalid input. Both numbers must exist in the list above. please try again")
                    continue

        if skip == False:
            totalGuess += 1
            if(result != 24):
                print("Your final result is " +
                      str(result) + ". sorry, you failed!")
                streak = 0
            else:
                print("congratulations. you won!")
                guessRight += 1
                streak += 1
            printStat(guessRight, totalGuess, streak, start)
            regenerate = True

    # print out statistics
    printStat(guessRight, totalGuess, streak, gameStart)


if __name__ == "__main__":
    play24()
