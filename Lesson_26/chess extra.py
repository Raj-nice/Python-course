thechessBoard =  {"1": " " , "2": " " , "3": " " , "4": " " , "5": " " , "6": " " , "7": " " , "8": " " ,
"9": " " , "10": " " , "11": " " , "12": " " , "13": " " , "14": " " , "15": " " , "16": " " ,
"17": " " , "18": " " , "19": " " , "20": " " , "21": " " , "22": " " , "23": " " , "24": " " ,
"25": " " , "26": " " , "27": " " , "28": " " , "29": " " , "30": " " , "31": " " , "32": " " ,
"33": " " , "34": " " , "35": " " , "36": " " , "37": " " , "38": " " , "39": " " , "40": " " ,
"41": " " , "42": " " , "43": " " , "44": " " , "45": " " , "46": " " , "47": " " , "48": " " ,
"49": " " , "50": " " , "51": " " , "52": " " , "53": " " , "54": " " , "55": " " , "56": " " ,
"57": " " , "58": " " , "59": " " , "60": " " , "61": " " , "62": " " , "63": " " , "64": " " }


def printChessBoard(board):

    for row in range (8):
        line = []
        for col in range (8):
            square_index = str(row * 8 + col + 1)
            line.append(board[square_index])
        print("\033[37m | ".join(line))
        
        if row < 7:
            print("\033[37m--+---+---+---+---+---+---+---")
       
#       ko.append(board+ ["8"])
#        for k in range (1, 1):
#            board[k] = board[str(k + 8)]
#            break

thechessBoard["1"] = "R"
thechessBoard["2"] = "N"
thechessBoard["3"] = "B"
thechessBoard["4"] = "Q"
thechessBoard["5"] = "K"
thechessBoard["6"] = "B"
thechessBoard["7"] = "N"
thechessBoard["8"] = "R"
for i in range(9, 17):
    thechessBoard[str(i)] = "P"
thechessBoard["64"] = "\033[38;5;94mR"
thechessBoard["63"] = "\033[38;5;94mN"
thechessBoard["62"] = "\033[38;5;94mB"
thechessBoard["61"] = "\033[38;5;94mQ"
thechessBoard["60"] = "\033[38;5;94mK"
thechessBoard["59"] = "\033[38;5;94mB"
thechessBoard["58"] = "\033[38;5;94mN"
thechessBoard["57"] = "\033[38;5;94mR"
for i in range(49, 57):
    thechessBoard[str(i)] = "\033[38;5;94mP"

def game():
    turn = "white"
    while True:
        printChessBoard(thechessBoard)
        print("It's " + turn + "'s turn.")
        move = input("Enter your move (e.g., e2 e4): ")
        if move == "quit":
            break
        # Process the move
        # Switch turns
        turn = "black" if turn == "white" else "white"


printChessBoard(thechessBoard)