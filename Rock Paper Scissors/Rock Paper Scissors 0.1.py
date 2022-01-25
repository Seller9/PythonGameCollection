from random import *
from time import sleep

while True:
    playerChoice = False
    while playerChoice == False:
        choiceIn = input("Player: Rock, Paper or Scissors?\n").strip().lower().replace('rock','r').replace('paper','p').replace('scissors','s')
        if choiceIn in 'rps':
            playerChoice = choiceIn
        else:
            print('Please type "Rock", "Paper", "Scissors" or the first letter of your choice.\n')

    print("\nBot: Rock, Paper or Scissors?")
    botChoice = choice(['Rock', 'Paper', 'Scissors'])
    time = 0.25+uniform(-0.15, 2)
    sleep(time)
    print(botChoice)
    botChoice = botChoice.lower().replace('rock','r').replace('paper','p').replace('scissors','s')
    
    print('')
    if playerChoice == botChoice:
        print('You tied...')
    elif (playerChoice == 'r' and botChoice == 'p') or (playerChoice == 'p' and botChoice == 's') or (playerChoice == 's' and botChoice == 'r'):
        print('You lose :(')
    elif (playerChoice == 'r' and botChoice == 's') or (playerChoice == 'p' and botChoice == 'r') or (playerChoice == 's' and botChoice == 'p'):
        print('You win!')

    print('\n\n')
