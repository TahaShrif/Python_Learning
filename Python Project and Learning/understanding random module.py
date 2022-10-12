import random 
theBoard = {"up-R": " ", "up-M": " ", "up-L": " ",
     "mid-R": " ","mid-M": " ","mid-L": " "
    ,"down-R":" ", "down-M":" ", "down-L":" " }

ComputerTurn = str(random.choice(list(theBoard.keys())))
print(ComputerTurn)
print(type(ComputerTurn))