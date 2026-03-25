#CS2030
#HW1 Problem 8.9
#Game: Play TicTacToe


#Initialize the board
board = [[' ' for _ in range(3)] for _ in range(3)]

#Set the starting player
current_player = 'X'
move_count = 0

while True:
    #Display the board
    print("  ---------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("  ---------")

    #Get player move
    row = int(input(f"Enter a row for player {current_player}: "))
    col = int(input(f"Enter a column for player {current_player}: "))

    #Make the move
    board[row][col] = current_player
    move_count += 1

    #Check win condition
    win = False
    
    #Check rows
    for r in range(3):
        if board[r][0] == current_player and board[r][1] == current_player and board[r][2] == current_player:
            win = True
            break
        
    #Check columns
    for c in range(3):
        if board[0][c] == current_player and board[1][c] == current_player and board[2][c] == current_player:
            win = True
            break
        
    #Check diagonals
    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        win = True
    if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        win = True

    if win:
        # Display the board and declare the winner
        print("  ---------")
        for row in board:
            print("| " + " | ".join(row) + " |")
            print("  ---------")
        print(f"Player {current_player} wins!")
        break

    #Check draw condition
    if move_count == 9:
        # Display the board and declare a draw
        print("  ---------")
        for row in board:
            print("| " + " | ".join(row) + " |")
            print("  ---------")
        print("It's a draw!")
        break

    #Switch player
    current_player = 'O' if current_player == 'X' else 'X'

