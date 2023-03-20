board = [' ' for _ in range(9)]

def print_board():
    print('-------------')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('-------------')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('-------------')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('-------------')

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def get_computer_move(board):
    # Check if computer can win in the next move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_win(board, 'O'):
                return i
            board[i] = ' '
    
    # Check if player can win in the next move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_win(board, 'X'):
                board[i] = 'O'
                return i
            board[i] = ' '

    # Try to take one of the corners
    for i in [0, 2, 6, 8]:
        if board[i] == ' ':
            return i

    # Try to take the center
    if board[4] == ' ':
        return 4

    # Take one of the edges
    for i in [1, 3, 5, 7]:
        if board[i] == ' ':
            return i

def play():
    print_board()
    while True:
        # Player's turn
        player_move = int(input("Enter your move (1-9): ")) - 1
        if board[player_move] == ' ':
            board[player_move] = 'X'
        else:
            print("Invalid move. Try again.")
            continue
        if check_win(board, 'X'):
            print_board()
            print("Congratulations! You win!")
            break
        if ' ' not in board:
            print_board()
            print("It's a tie!")
            break
        # Computer's turn
        computer_move = get_computer_move(board)
        board[computer_move] = 'O'
        if check_win(board, 'O'):
            print_board()
            print("Sorry, you lose.")
            break
        print_board()

if __name__ == '__main__':
    play()
