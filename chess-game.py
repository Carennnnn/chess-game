#Yuelin Liu
#101154473
    
    
#This funcition provides instruction for this program
#@params    none
#@return    none
def instruction():
    print("This program models a chess game.\n")
    print("You must type what pieces appear on each of eight rows.")
    print("You must use lowercase letters for the white pieces")
    print("and uppercase letters for the black pieces.")
    print("You must use hyphen '-' for an empty space.\n")
    print("You may use following abbreviations:")
    print("k - king")
    print("q - queen")
    print("b - bishop")
    print("n = knight")
    print("r - rook")
    print("p - pawn\n")
    print("The program will tell you which player is winning.\n")
    print("You can enter the number to choose quit the program,")
    print("enter another chessboard or move a piece.\n")



#This function allows the user to type what pieces appear on each row
#and display the chessboard
#@params    none
#@return    all - returns the chessboard that user enters
    
def current_state():
    
    #valid characters in chessboard
    valid = ['k','q','b','n','r','p','K','Q','B','N','R','P','-']
    
    #construct a 2d-list to store the pieces in each row
    all = []
    for each_row in range(8):
        row = []
        row.append(input("What pieces appear on row {}? ".format(each_row+1)))
        
        #if the pieces contain an invalid character
        #or the length of each row is less than or greater than 8
        #ask the user to retype it
        for item in range(len(row)):
            while row[item] not in valid and len(row[item]) != 8:
                row.pop()
                row.append(input("What pieces appear on row {}? ".format(each_row+1)))
        all.append(row)
        
    #display the chessboard
    display_current_state(all)
                
    return all



#This function calculates the score of white chess and black chess
#and report which player is winning
#@params    chessboard - the chessboard that the user enters
#@return    none

def player_score(chessboard):
    
    #put value and corresponding white and black pieces in a list
    value = [0,10,5,3.5,3,1]
    white_score = ['k','q','r','n','b','p']
    black_score = ['K','Q','R','N','B','P']
    
    #calculate score of white and black pieces
    total_b = 0
    total_w = 0
    for row in range(8):
        for item in range(8):
            if chessboard[row][0][item] in white_score:
                for index in range(len(white_score)):
                    if chessboard[row][0][item] == white_score[index]:
                        total_w += value[index]
            elif chessboard[row][0][item] in black_score:
                for index in range(len(black_score)):
                    if chessboard[row][0][item] == black_score[index]:
                        total_b += value[index]
                
    #present the user score
    print('White chess score: ', total_w)
    print('Black chess score: ', total_b)
    
    #present the user who is winning
    if total_w > total_b:
        print("White chess is winning!")
    elif total_w < total_b:
        print("Black chess is winning!")
    else:
        print("Two players have the same score.")



#This function allows user to move the piece to another place
#@params    chessboard - the chessboard that the user enters
#@return    chess_list - chess_list is the chessboard after the repostion
        
def reposition_pieces(chessboard):
    
    #turn the string in each row into list
    chess_list = []
    for row in range(8):
        chess_row=[]
        chess_row = turn_list(chessboard[row][0])
        chess_list.append(chess_row)
        
    #ask the user the position of piece that they want to move
    r = int(input("Which row do you want to move the chess? "))
    c = int(input("Which column do you want to move the chess? "))
    
    #if there is no piece on that position, ask them to retype again
    for row in range(8):
        for item in range(8):
            while chessboard[r-1][0][c-1] == '-':
                print("There is not a piece at that location.")
                r = int(input("Which row do you want to move the chess? "))
                c = int(input("Which column do you want to move the chess? "))
                
    #remove the piece at that position
    remove = chess_list[r-1].pop(c-1)
    chess_list[r-1].insert(c-1,'-')
    
    #ask user for the new position of the piece
    r_new = int(input("What is new row for the chess piece? "))
    c_new = int(input("What is new column for the chess piece? "))
    
    #remove the piece at that position and insert the piece that they want to move
    chess_list[r_new-1].pop(c_new-1)
    chess_list[r_new-1].insert(c_new-1, remove)
    
    #turn the list of each row in to string
    chess_list = turn_string(chess_list)
    
    return chess_list


   
#This function displays the chessboard in a nice format
#@params    chessbpard - the chessboard that the user enters
#@return    none

def display_current_state(chessboard):
    
    for row in chessboard:
        for item in row:
            print(item)



#This function turns the list in each row of chessboard into string
#@params    chess_list - chess_list is the chessboard after the repostion
#@return    whole_list - whole_list is the chessboard that contains the string in each of eight rows
            
def turn_string(chess_list):
    
    whole_list = []
    for r in chess_list:
        string = ""
        list_ = []
        for i in r:
            string += i
        list_.append(string)
        whole_list.append(list_)
        
    return whole_list



#This function turns the string in each row of chessboard into list
#@params    string - the string in each of eight rows of chessboard
#@return    list_e - return the list of each row

def turn_list(string):
    
    list_e = []
    for i in string:
        list_e.append(i)
        
    return list_e



#This function interacts with the user and calls the functions above
#@params    none
#@return    none

def main():
    
    instruction()
    chessboard = current_state()
    score = player_score(chessboard)
    
    #let the user to choose one of the three options, unless the user choose to quit, display them the options again
    while True:
        next = input("What do you want to do next?(Enter the number)\n"
                         "1.quit the program\n"
                         "2.enter another chessboard\n"
                         "3.move a piece\t")

        if next == "1":
            break
        
        elif next == "2":
            chessboard = current_state()
            score = player_score(chessboard)
            
        elif next == "3":
            chessboard = reposition_pieces(chessboard)
            display = display_current_state(chessboard)
            score = player_score(chessboard)
            
        #if the user chooses an unvalid number, ask them the question again
        else:
            next = input("What do you want to do next?\n"
                     "1.quit the program\n"
                     "2.enter another chessboard\n"
                     "3.move a piece\t")

main()
