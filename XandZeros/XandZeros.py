import random

row0=["😐","😐","😐"]
row1=["😐","😐","😐"]
row2=["😐","😐","😐"]

board = [row0,row1,row2]
#boardString = f"{row1}\n{row2}\n{row3}"
boardString = f"{board[0]}\n{board[1]}\n{board[2]}"
print(boardString);
count=0
winner="no one"


def computer_plays(count):
    #print("computer_plays called")
    playing_turn =True
    while playing_turn and count < 9:
        position_x = random.randint(0, 2)
        position_y = random.randint(0, 2)
        play_position = board[position_x][position_y]
        #print("play_position: "+str(position_x)+str(position_y))
        if not play_position.__eq__("😐"):
            continue
        else:
            print("computer plays...."+ str(position_x)+str(position_y))
            board[position_x][position_y]='O'
            count += 1
            #boardString = f"{board[0]}\n{board[1]}\n{board[2]}"
            #print("comp played: "+boardString)
        playing_turn=False
    return count

def decide_winner(check_result):
    if check_result.__eq__("X"):
        return "X"
    elif check_result.__eq__("O"):
        return "O"
    else:
        return "no one"


#[r][c]
def check_winner(board):
    if board[0][0].__eq__(board[0][1]) and board[0][0].__eq__(board[0][2]):  #0th row
        return decide_winner(board[0][0])
    elif board[1][0].__eq__(board[1][1]) and board[1][0].__eq__(board[1][2]): #1st row
        return decide_winner(board[1][0])
    elif board[2][0].__eq__(board[2][1]) and board[2][0].__eq__(board[2][2]): #2nd row
        return decide_winner(board[2][0])
    elif board[0][0].__eq__(board[1][0]) and board[0][0].__eq__(board[2][0]): #0th column
        return decide_winner(board[0][0])
    elif board[0][1].__eq__(board[1][1]) and board[0][1].__eq__(board[2][1]): #1st column
        return decide_winner(board[0][1])
    elif board[0][2].__eq__(board[1][2]) and board[0][2].__eq__(board[2][2]): #2nd column
        return decide_winner(board[0][2])
    elif board[0][0].__eq__(board[1][1]) and board[0][0].__eq__(board[2][2]): #right to left diagonal
        return decide_winner(board[0][0])
    elif board[0][2].__eq__(board[0][1]) and board[0][2].__eq__(board[2][0]): #left to right diagonal
        return decide_winner(board[0][2])
    else:
        return "no one"

#check_winner_result = check_winner(board).__eq__("no winner")
#print("check_winner_result "+check_winner_result)

while count < 9 and winner.__eq__("no one"):
    position = input("where do you want to place your mark<xy>: ")
    print(position)
    # you can access individual letters in a string(position) like a list. So treat a string like a list
    value=board[int(position[0])][int(position[1])]
    #if value.__eq__("X") or  value.__eq__("O"):
    if not value.__eq__("😐"):
        print("already taken")
        continue
    else:
        board[int(position[0])][int(position[1])] = 'X'
        count += 1
    #print("count before comp turn: "+str(count))
    #winner = check_winner(board)
    count=computer_plays(count)
    winner = check_winner(board)
    #print("count after comp turn: " + str(count))

    boardString = f"{board[0]}\n{board[1]}\n{board[2]}"
    print(boardString)

print(f"{winner} wins!")






