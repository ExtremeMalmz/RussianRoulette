#Eric Malmström - Starclan studiosroundRunning

import random

import time

from playsound import playsound

def menu_printer(message):
    print('='*50 + '\n' + message + '\n' + '='*50)

def game_instructions():
    menu_printer("Instructions for \"playing\" Russian Roulette")
    print("1) Add players by pressing 2 in the menu")
    print("2) The game then randomly chooses a player to shoot someone")
    print("3) The gun either \"clicks\" or \"fires\"")
    print("4) If it clicks then they live to see another day, if not then not")
    print("5) There is no way to back out of Russian Roulette....")
    print("--- the thread is sleeping for 5 seconds ---")
    time.sleep(5)

def add_player_to_game(playerList):
    menu_printer("Add a player")

    playerName = str(input("Enter the players name to add them to the list: "))

    if playerName in playerList:
        print(f"{playerName} is already in the list, no twins allowed")
    else:
        playerList.append(playerName)

        print("--- --- --- \nPrinting Player List")
        print(playerList)

    return playerList

def choose_player(playerList):
    random.shuffle(playerList)
    selectedPlayer = playerList[0]
    return selectedPlayer

def check_target(target,list):
    if target in list:
        print(f"You aim the gun at {target}")
        return False
    else:
        print("--- --- ---\nYou can not kill what doesn't exist, try again")
        print("Heres a list of players")
        print(list)
        return True

def dead_or_alive(trigger,list):

    randomChoice = random.choice(list)
    list.remove(randomChoice)
    
    if trigger == randomChoice:
        playsound('GunShot.mp3')
        
        print("BOOM")
        list = ["F"]
        return list
    else:
        playsound('GunEmpty.mp3')

        print("click")
        lenLeftInList = len(list)
        print(f"Only {lenLeftInList} bullets left")
        return list
        

def game_start(playerList):
    roundNumber = 1
    menu_printer("The game has started, good luck")

    while True:
        trigger = random.randint(1,6)
        bulletList = [1,2,3,4,5,6]
        roundRunning = True
        
        while roundRunning:
            targetNotChecked = True

            menu_printer(f"Round {roundNumber}")
            
            selectedPlayer = choose_player(playerList)
            print(f"The selected player is {selectedPlayer} \nWho does {selectedPlayer} want to shoot?")
    
            while targetNotChecked:
                selectedTarget = str(input("Enter name:"))
                
                targetNotChecked = check_target(selectedTarget,playerList)
                
            bulletList = dead_or_alive(trigger,bulletList)
            
            if "F" in bulletList:
                print(f"{selectedTarget} died, starting next round")
                playerList.remove(selectedTarget)
            
                roundRunning = False

            roundNumber +=1

        if len(playerList) == 1:
            roundNumber -= 1
            menu_printer("WINNER WINNER CHICKEN DINNER")
            print(f"Congratulations {selectedPlayer} you have won the game on Round {roundNumber}! \nYour prize is to live to see another day")
            playsound('victory.mp3')

            exit()

def main():
    playerList = []

    while True:
        menu_printer("Welcome to russian roulette only one may survive...")

        userInput = str(input("1-Game instructions \n2-Add a player to the game \n3-Play the game\n"))
        match userInput:
            case '1':
                game_instructions()
            case '2':
                playerList = add_player_to_game(playerList)
            case '3': 
                if len(playerList) <= 1:
                    print("You need at least 2 players to play!")
                else:
                    game_start(playerList)
            case _:
                print("Invalid statement, please try again")

main()

