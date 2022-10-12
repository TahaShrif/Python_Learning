import random, pprint, sys, time
theBoard = {"up-R": " ", "up-M": " ", "up-L": " ",
     "mid-R": " ","mid-M": " ","mid-L": " "
    ,"down-R":" ", "down-M":" ", "down-L":" " }
def wintext():
    print("you have won")
    exit()
def PCwintext():
    print("The PC has beaten you")
    exit()
    
def winning():  
    if theBoard["up-R"] == player and theBoard["mid-M"] ==player and theBoard["down-L"]  == player:
        wintext()
    elif theBoard["up-L"] == player and theBoard["mid-M"] ==player and theBoard["down-R"]  == player:
       wintext()
    elif theBoard["up-R"] == player and theBoard["up-M"] ==player and theBoard["up-L"]  == player:
       wintext()
    elif theBoard["mid-R"] == player and theBoard["mid-M"] ==player and theBoard["mid-L"]  == player:
       wintext()
    elif theBoard["down-R"] == player and theBoard["down-M"] ==player and theBoard["down-L"]  == player:
       wintext()
    elif theBoard["up-R"] == player and theBoard["mid-R"] ==player and theBoard["down-R"]  == player:
       wintext()
    elif theBoard["up-M"] == player and theBoard["mid-M"] ==player and theBoard["down-M"]  == player:
       wintext()
    elif theBoard["up-L"] == player and theBoard["mid-L"] ==player and theBoard["down-L"]  == player:
       wintext()
    elif theBoard["up-R"] == PC and theBoard["up-M"] ==PC and theBoard["up-L"]  == PC:
       PCwintext()
    elif theBoard["mid-R"] == PC and theBoard["mid-M"] ==PC and theBoard["mid-L"]  == PC:
       PCwintext()
    elif theBoard["down-R"] == PC and theBoard["down-M"] ==PC and theBoard["down-L"]  == PC:
       PCwintext()
    elif theBoard["up-R"] == PC and theBoard["mid-R"] ==PC and theBoard["down-R"]  == PC:
       PCwintext()
    elif theBoard["up-M"] == PC and theBoard["mid-M"] ==PC and theBoard["down-M"]  == PC:
       PCwintext()
    elif theBoard["up-L"] == PC and theBoard["mid-L"] ==PC and theBoard["down-L"]  == PC:
       PCwintext()
    elif theBoard["up-R"] == PC and theBoard["mid-M"] ==PC and theBoard["down-L"]  == PC:
        PCwintext()
    elif theBoard["up-L"] == PC and theBoard["mid-M"] ==PC and theBoard["down-R"]  == PC:
        PCwintext()



        
#These are both for debugging: diagonalwin()
#These are both for debugging: pprint.pprint(theBoard)
def printBoard(board):
    print(board["up-L"] + "|" + board["up-M"] +"|"+ board["up-R"])
    print("_____")
    print(board["mid-L"] + "|" + board["mid-M"] +"|"+ board["mid-R"])
    print("_____")
    print(board["down-L"] + "|" + board["down-M"] +"|"+ board["down-R"])

def playervalue():
    global player
    player = input("Will you be X or O?")
    while player != "X" and player != "O":
        print("Please, only Enter X or O")
        player = input()
    global PC
    if player == "O":
        PC = "X"
    elif player == "X":
        PC = "O"
playervalue()
            
            # print("##Debugging: PC == " + PC , type(PC))
ComputerTurn = " None "
def pcturn():
    global ComputerTurn
    ComputerTurn = str(random.choice(list(theBoard.keys())))
    if theBoard[ComputerTurn] == " ":
        theBoard[ComputerTurn] = PC
    else:
        pcturn()
# print("Debugging: computer turn: " + ComputerTurn)


def play():
    change = input(("Enter a value from ", list(theBoard.keys())))
    while change not in list(theBoard.keys()):
        print("please Enter only from the following: ")
        play()
    if change in list(theBoard.keys()):
        theBoard[str(change)] = str.upper(player)
        pcturn()

        
        printBoard(theBoard)
        winning()
        if " " not in list(theBoard.values()):
            print("The Game is a tie")
        if " " in list(theBoard.values()):
            play()



play()

