import random

def insert_letter(board, mark, pos, available):
    board[pos] = mark
    available[pos] = ' '

def space_free(board,pos):
    return board[pos] == ' '

def print_board(b, a): # b = board , a = available 
    print('Here is the board\n\n')
    print('          '+a[7] +'|'+ a[8] +'|'+ a[9]+'        '+b[7]+'|'+b[8]+'|'+b[9])
    print('          '+'-----        -----')
    print('          '+a[4] +'|'+ a[5] +'|'+ a[6]+'        '+b[4]+'|'+b[5]+'|'+b[6])
    print('          '+'-----        -----')
    print('          '+a[1] +'|'+ a[2] +'|'+ a[3]+'        '+b[1]+'|'+b[2]+'|'+b[3]+'\n')


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[1] == board[2] == board[3] == mark) or
    (board[8] == board[5] == board[2] == mark) or
    (board[9] == board[6] == board[3] == mark) or
    (board[7] == board[4] == board[1] == mark) or
    (board[7] == board[5] == board[3] == mark) or
    (board[9] == board[5] == board[1] == mark))

def player_move(board, marker, available):
    position = 0
    while position not in list(range(1,10)) or not space_free(board, position):
        try:
            position = int(input(f'Where do you place your mark {marker}? (1-9) '))
        except ValueError:
            print('Please enter a number between 1 and 9')
            continue
    print(f'You placed an {marker} in position {position}')
    insert_letter(board, marker, position, available)

def ai_move(board,ai,human):
    possible_moves = [i for i, letter in enumerate(board) if letter == ' ' and i != 0]
    move = 0
    
    for letter in [ai,human]:
        for possible in possible_moves:
            board_copy = board[:] # lists are mutable and to avoid altering the board we make a copy
            board_copy[possible] = letter
            if win_check(board_copy, letter):
                move = possible
                return move
    
    open_corners = [x for x in possible_moves if x in [1,3,7,9]]
    if len(open_corners) > 0:
        move = random.choice(open_corners)
        return move

    if 5 in possible_moves:
        move = 5
        return move
    
    edges_open = [x for x in possible_moves if x in [2,4,6,8]]
    if len(edges_open) > 0:
        move = random.choice(edges_open)
    
    return move
    

def select_random(possible_moves):
    length = len(possible_moves)
    rand_index = random.randrange(0, length)
    return possible_moves[rand_index]

def full_board(board):
    return ' ' not in board[1:]


def main():
    board = [' ' for _ in range(10)]
    available = [str(x) for x in range(10)] # available postions that are shown to the user
    print('Welcome to Tic Tac Toe!')
    toggle = random.choice((1,-1))
    players = [0, 'X', 'O']
    human = players[toggle]
    ai = players[toggle *-1]
    print(f'Your mark is {human} human and you will go first!')

    while not full_board(board):
        print_board(board,available)
        
        if not (win_check(board, ai)):
           player_move(board,human, available)
        else:
            print(f'Sorry {ai}\'s won this time!')
            break
           
        if not (win_check(board, human)):
            
            move = ai_move(board, ai, human)
            if move == 0:
               print_board(board,available)
               print('Tie game!')
            else:
                insert_letter(board, ai, move, available)
                print(f'Computer placed an \'{ai}\' in position {move}')
                
            
        else:
            print_board(board, available)
            print('You won this game! Great job!')
            break


while True:
    main()
    if input('Do you want to play again? (Y/N)').upper().startswith('Y'):
        continue
    else:
        break

