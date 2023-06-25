import random


def explainRules():
    explain = input('Do you know how to play this game? [y/n]')
    if explain.lower() == 'n':
        print("how to play: enter either t, c, s, or b which stands for tiger, chicken, stick and bug. the tiger eats the chicken, the chicken eats the bug, the bug eats the stick and the stick hits the tiger. you will play against a computer but it isn't impossible to win.")


def getRounds():
    while True:
        rounds = input("How many rounds to win? [1,10] ")
        try:
            roundsValue = int(rounds)
            if roundsValue in range(1, 11):
                return roundsValue
            else:
                print(rounds + " is not a number between 1 and 10, do your maths boi!?")
        except ValueError:
            print("your input isn't a number.")


def getPlayerChoice():
    validLetters = ['t', 'c', 's', 'b']
    while True:
        choice = input(
            "\nChoose one of the followings: T(iger), C(hicken), S(tick) or B(ug):")
        choice = choice.lower()

        if len(choice) > 1 or choice not in validLetters:
            print("Must be one of the following: [t/c/s/b]. try again. ")
        else:
            return choice


def getGameResult(name, player, pc):
    # return -1 if player win, 0 if not compatible, 1 if PC win
    boardNames = {1: 'Stick', 2: 'Tiger', 3: 'Chicken',  4: 'Bug'}
    playerChoice = boardNames.get(player)
    pcChoice = boardNames.get(pc)
    print(name + ': ' + playerChoice + '. Computer: ' + pcChoice)
    higher = player - 1
    if higher == 0:
        higher = 4
    if pc == higher:
        print(name + ' lost this round. sucks right :(')
        return 1
    lower = player + 1
    if lower == 5:
        lower = 1
    if pc == lower:
        print(name + ' won this round. good job')
        return -1

    print("no one win this round")
    return 0
    # print lose / NC / win result to player


def Buchitist():
    board = {'s': 1, 't': 2, 'c': 3, 'b': 4}
    explainRules()
    playerName = input("what's your name?")
    while True:
        playerWin = 0
        pcWin = 0
        rounds = getRounds()

        while (pcWin < rounds and playerWin < rounds):
            # get random pc value from 1 to 4
            pcChoiceValue = random.randint(1, 4)
            
            playerChoice = getPlayerChoice()
            playerChoiceValue = board.get(playerChoice, None)

            result = getGameResult(
                playerName, playerChoiceValue, pcChoiceValue)
            if result == 1:
                pcWin += 1
            elif result == -1:
                playerWin += 1
            print(playerName + ": " + str(playerWin) +
                  ". Computer: " + str(pcWin))
            if playerWin >= rounds:  # player win
                print("Good job! you win " + playerName)
            elif pcWin >= rounds:
                print("Too bad, you lose... " + playerName)

        tryAgain = input("Game over. Do you want to play again? [y/Y]")
        if tryAgain.lower() != 'y':
            break


if __name__ == "__main__":
    Buchitist()
