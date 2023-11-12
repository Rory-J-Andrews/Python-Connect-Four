import random

welcome = """
Welcome to Connect Four!
--------------------------------------
"""

board = (['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'],
         ['*', '*', '*', '*', '*', '*', '*'])

def main(board):
    board = board
    print(welcome)
    p1name = str(input("Player 1, what is your name?: "))
    p2name = str(input("Player 2, what is your name?: "))
    print("")

    print("Let's see who should go first:")
    p1coin = getCoinInput(p1name)
    p2coin = getCoinInput(p2name)
    coinwinner = random.randint(0, 1)
    if coinwinner == 0:
        print("The coin came up Heads!")
    elif coinwinner == 1:
        print("The coin came up Tails!")
    order = returnPlayerOrder(p1name, p2name, p1coin, p2coin, coinwinner)
    p1 = order[0]
    p2 = order[1]
    print("")

    for rounds in range(0, 22):
        displayBoard(board)

        if rounds == 21:
            print("")
            print("Somehow, there was a tie.")
            print("")
            print("Thank you for playing!")
            break

        if checkBoardWin(board, 1) == True:
            print("")
            print(p2 + " won!")
            print("")
            print("Thank you for playing!")
            break

        print("")
        p1input = getColumnInput(board, p1)
        board = updateBoard(board, p1input, 0)
        print("")
        displayBoard(board)

        if checkBoardWin(board, 0) == True:
            print("")
            print(p1 + " won!")
            print("")
            print("Thank you for playing!")
            break

        print("")
        p2input = getColumnInput(board, p2)
        board = updateBoard(board, p2input, 1)
        print("")

def getCoinInput(name):
    coin = str(input(name + ", choose Heads or Tails: "))
    while True:
        if coin == "Heads" or coin == "heads" or coin == "0":
            return 0
            break
        elif coin == "Tails" or coin == "tails" or coin == "1":
            return 1
            break
        else:
            coin = str(input("Please choose between Heads or Tails: "))
            continue

def returnPlayerOrder(p1name, p2name, p1coin, p2coin, coinwinner):
    if coinwinner == p1coin:
        print(p1name + " gets to go first.")
        return [p1name, p2name]
    elif coinwinner == p2coin:
        print(p2name + " gets to go first.")
        return [p2name, p1name]

def displayBoard(board):
    length = len(board[1])
    for x in range(1, length + 1):
        print(x, end=" ")
    for y in board:
        print("")
        for x in y:
            print(x, end=" ")
    print("")

def checkBoardWin(board, player):
    x_coord = 0
    y_coord = 0
    if player == 0:
        token = 'X'
    elif player == 1:
        token = 'O'
    for y in board:
        for x in y:
            if x == token:
                for dir in range(0, 5):
                    Win = checkSpotWin(board, x_coord, y_coord, dir, token)
                    if Win == True:
                        return True
            x_coord = x_coord + 1
        x_coord = 0
        y_coord = y_coord + 1
    return False

def checkSpotWin(board, x, y, dir, token):
    # East
    if dir == 0:
        for tokens in range(1, 4):
            x_check = x + tokens
            if x_check > 6:
                return False
            else:
                if not board[y][x_check] == token:
                    return False
                elif board[y][x_check] == token and tokens == 3:
                    return True
    # South-east
    elif dir == 1:
        for tokens in range(1, 4):
            x_check = x + tokens
            y_check = y + tokens
            if x_check > 6 or y_check > 5:
                return False
            else:
                if not board[y_check][x] == token:
                    return False
                elif board[y_check][x_check] == token and tokens == 3:
                    return True
    # South
    elif dir == 2:
        for tokens in range(1, 4):
            y_check = y + tokens
            if y_check > 5:
                return False
            else:
                if not board[y_check][x] == token:
                    return False
                elif board[y_check][x] == token and tokens == 3:
                    return True
    # South-west
    elif dir == 3:
        for tokens in range(1, 4):
            x_check = x - tokens
            y_check = y + tokens
            if y_check > 5 or x_check < 0:
                return False
            else:
                if not board[y_check][x_check] == token:
                    return False
                elif board[y_check][x_check] == token and tokens == 3:
                    return True
    # West
    elif dir == 4:
        for tokens in range(1, 4):
            x_check = x - tokens
            if x_check < 0:
                return False
            else:
                if not board[y][x_check] == token:
                    return False
                elif board[y][x_check] == token and tokens == 3:
                    return True

def getColumnInput(board, name):
    column = input(name + ", choose the column you wish to drop your token in: ")
    while True:
        try:
            column = int(column)
            if column > 0 and column < 8:
                if board[0][column - 1] == 'X' or board[0][column - 1] == 'O':
                    column = input("Please choose a column that is not full: ")
                else:
                    return column
            else:
                column = input("Please enter a number between 1 and 7: ")
        except:
            column = input("Please enter a number between 1 and 7: ")

def updateBoard(board, column, order):
    if order == 0:
        token = 'X'
    if order == 1:
        token = 'O'
    x = column - 1
    y_coord = 5
    for y in range(0, 6):
        if board[y_coord][x] == '*':
            board[y_coord][x] = token
            return board
        y_coord = y_coord - 1


main(board)