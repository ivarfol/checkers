'''
Program for testing the russian checkers
'''
from random import randint
from config_reader import get_settings

def print_board(board, board_colour, shift, border, start):
    '''
    print_board
    can output the board in different colours or without them
    can "shift" the colours of the background
    can output either 8x8 or 10x10 board
    
    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    board_colour : str
        1, 2 or 3
        changes the way board is printed
    shift : bool
        "shifts" the background
    border : int
        8 or 10
        corresponds to the size of the board
    
    Returns
    -------
    None.

    '''
    numb = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')[:border]
    if board_colour == '2':
        colour = '\033[47m'
        colour_op = '\033[40m'
        colour_hide = '\033[37m'
        colour_zero = '\033[30m'
        reset = '\033[0m'
        usual_w = '\u25CF'
        king_w = '\u25C6'
        usual_b = '\u25CB'
        king_b = '\u25C7'
    elif board_colour == '3':
        colour = '\033[40m'
        colour_op = '\033[47m'
        colour_hide = '\033[30m'
        colour_zero = '\033[37m'
        reset = '\033[0m'
        usual_w = '\u25CB'
        king_w = '\u25C7'
        usual_b = '\u25CF'
        king_b = '\u25C6'
    elif board_colour == '1':
        colour = ''
        colour_op = ''
        colour_hide = ''
        colour_zero = ''
        reset = ''
        usual_w = 'w'
        king_w = 'm'
        usual_b = 'b'
        king_b = 'p'
    print('\n  a b c d e f g h i j'[:2 * border + 3])
    for j in range(border):
        if numb[j] != '10':
            print(numb[j], end=' ')
        else:
            print('10', end='')
        for x in range(border):
            if board_p(j, x, shift):
                print(colour_op, end='')
            else:
                print(colour, end='')
            if board[j][x] == '_':
                print(colour_hide, end='')
            elif board[j][x] == '0':
                print(colour_zero, end='')
            elif board_colour == '3':
                print(colour_hide, end='')
            if board[j][x] == 'w':
                print(usual_w, end=' ')
            elif board[j][x] == 'm':
                print(king_w, end=' ')
            elif board[j][x] == 'b':
                print(usual_b, end=' ')
            elif board[j][x] == 'p':
                print(king_b, end=' ')
            else:
                print(' '.join(board[j][x]), end=' ')
            print(reset, end='')
        print(f'{reset}{numb[j]}')
    print('  a b c d e f g h i j'[:2 * border + 1])
    print('white')
    temp_w = gen_turn_list(board, True, border, False, start)[0]
    for cdnt in temp_w:
        print(convert(cdnt), end=' ')
    print('\nblack')
    temp_b = gen_turn_list(board, False, border, False, start)[0]
    for cdnt in temp_b:
        print(convert(cdnt), end=' ')
    print()
      
def board_p(a, b, shift):
    '''
    responsible for "shifting" the background

    Parameters
    ----------
    a : int
        1 - 10
        y coordinate of the current square
    b : int
        1 - 10
        x coordinate of the current square
    shift : bool
        "shifts" the background

    Returns
    -------
    bool
    whether the coordinates are on a diogonal

    '''
    if shift:
        return(a % 2 != b % 2)
    else:
        return(a % 2 == b % 2)
    
def board_creator(board_colour):
    '''
    creates a list that will be used as the board
    based off the input
    can output the board in different colours or without them

    Parameters
    ----------
    board_colour : str
        1, 2 or 3
        changes the way board is printed

    Returns
    -------
    board_lists : list
        list of lists of strings of length 1
        the new board
    Wh_turn : bool
        whether the current turn is for whites
    shift : bool
        whether the background is "shifted"
    border : int
        8 or 10
        corresponds to the size of the board

    '''
    board_list = []
    temp_list = []
    board = input('Paste your board:\n')
    if len(board) == 284 or len(board) == 271:
        border = 10
    else:
        border = 8
    len_temp = len(board)
    if len_temp == 271:
        board = board[21:- 22]
    elif len_temp == 284:
        board = board[24:- 24]
    elif len_temp == 185:
        board = board[18:- 18]
    elif len_temp == 196:
        board = board[21:- 18]
    if board[0] == '_':
        shift = True
    else:
        shift = False
    if border == 10:
        board = board[:-20] + ' ' + board[-20:]
    if ('w' in board) or ('b' in board) or ('m' in board) or ('p' in board):
        colour_temp = '1'
    else:
        colour_temp = choice_of_two("What board type did you use?\n(if the figures are white on black\nsquares choose 1, otherwise choose 2)")
    board = board.split(' ')
    for i in range(0, border**2, border):
        temp_list = board[i + int(i / border):i + int(i / border) + border]
        for x in range(border):
            if colour_temp == '2':
                if temp_list[x] == '●':
                    temp_list[x] = 'w'
                elif temp_list[x] == '○':
                    temp_list[x] = 'b'
                elif temp_list[x] == '◆':
                    temp_list[x] = 'm'
                elif temp_list[x] == '◇':
                    temp_list[x] = 'p'
            elif colour_temp == '3':
                if temp_list[x] == '●':
                    temp_list[x] = 'b'
                elif temp_list[x] == '○':
                    temp_list[x] = 'w'
                elif temp_list[x] == '◆':
                    temp_list[x] = 'p'
                elif temp_list[x] == '◇':
                    temp_list[x] = 'm'
        board_list.append(temp_list)
    if colour_temp != board_colour:
        print_board(board_list, colour_temp, shift, border, [])
    print_board(board_list, board_colour, shift, border, [])
    Wh_turn = choice_of_two('\nWhose turn was that?\nWhite(1), Black(0)')
    return(board_list, Wh_turn, border, shift)

def ch_help(board_colour):
    '''
    outputs all possible comands; shows how the figures move
    outputs examples in colours corresponding to the ones on of the board

    Parameters
    ----------
    board_colour : str
        1, 2 or 3
        changes the way examples are printed

    Returns
    -------
    None.

    '''
    if board_colour == '1':
        colour = ''
        colour_op = ''
        colour_u = ''
        colour_hide = ''
        u_wh = 'w'
        u_bl = 'b'
        king_wh = 'm'
        king_bl = 'p'
    elif board_colour == '2':
        colour = '\033[0;40m'
        colour_op = '\033[47;37m'
        colour_u = '\033[0m'
        colour_hide = '\033[30m'
        u_wh = '●'
        u_bl = '○'
        king_wh = '◆'
        king_bl = '◇'
    else:
        colour = '\033[47;30m'
        colour_op = '\033[40;30m'
        colour_u = '\033[0m'
        colour_hide = '\033[37m'
        u_wh = '○'
        u_bl = '●'
        king_wh = '◇'
        king_bl = '◆'
    print('\nHelp')
    choice = choice_of_three('Do you want to continue to\ninputs(1), figures(2), exit help(3)')
    while choice != '3':
        if choice == '1':
            print('Input:')
            print('help - for help')
            print('undo - to go one turn back')
            print('redo - to go one turn turn forward if ')
            print('you did not make any new turns')
            print('surrender - to surrender to the enemy and end the game')
        elif choice == '2':
            print('Figures:')
            print(f'usual white - {colour}{u_wh}{colour_u}')
            print(f'usual black - {colour}{u_bl}{colour_u}')
            print(f'dama/king white - {colour}{king_wh}{colour_u}')
            print(f'dama/king black - {colour}{king_bl}{colour_u}')
            if binary_choice('Do you want to learn about turn patterns?'):
                print('x - marks the possible turns')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u} - usual figures can go diagonally in one')
                print(f'{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_bl} {colour_op}_ {colour_u}│{colour_op}_ {colour}x {colour_op}_ {colour}{u_wh} {colour_op}_ {colour_u}   direction, and attak by jumping over the')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{u_wh} {colour_op}_ {colour}{colour_hide}0 {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{u_bl} {colour_op}_ {colour}{colour_hide}0 {colour_u}   enemy in all four directions')
                print(f'{colour_op}_ {colour}x {colour_op}_ {colour}{u_bl} {colour_op}_ {colour_u}│{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_wh} {colour_op}_ {colour_u}   they can move only one space when not attaking')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x ')
                print()
                print(f'{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_op}_ {colour_u}│{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_op}_ {colour_u} - dama/king figures can go diagonally in all')
                print(f'{colour_op}_ {colour}x {colour_op}_ {colour}{u_bl} {colour_op}_ {colour}{colour_hide}0 {colour_u}│{colour_op}_ {colour}x {colour_op}_ {colour}{u_wh} {colour_op}_ {colour}{colour_hide}0 {colour_u}   directions, and attak by jumping over the')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{king_wh} {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{king_bl} {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour_u}   enemy in all directions')
                print(f'{colour_op}_ {colour}x {colour_op}_ {colour}x {colour_op}_ {colour}{colour_hide}0 {colour_u}│{colour_op}_ {colour}x {colour_op}_ {colour}x {colour_op}_ {colour}{colour_hide}0 {colour_u}   the can move as many spaces as there are')
                print(f'{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_bl} {colour_op}_ {colour_u}│{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_wh} {colour_op}_ {colour_u}   free spaces in diogonal')
                print(f'{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}│{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}   they can attak any enemy on the diogonal')
                print(colour_u, end='')
        choice = choice_of_three('Do you want to continue to\ninputs(1), figures(2), exit(3)')
    print('Exit')

def board_undo(board, turns, turn_num):
    '''
    returns the board to the state it was in at the start of the previous turn

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    turns : list
        list of lists of lists consisting of
        a one symbol string and a list with length 2 - 4
        stores the information about turns
    turn_num : int
        number of the current turn

    Returns
    -------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    turn_num : int
        number of the current turn

    '''
    turn_num -= 2
    for i in range(len(turns[turn_num]) - 1, -1, -1):
        change = turns[turn_num][i]
        if change:
            if len(change[1]) == 4:
                board[change[1][0]][change[1][1]] = change[0]
                board[change[1][2]][change[1][3]] = '0'
            else:
                board[change[1][0]][change[1][1]] = change[0]
    return(board, turn_num)

def board_redo(board, turns, turn_num, international, border):
    '''
    if no new turns were made since the user inputed "undo",
    returns the board to the state it was in before "undo"

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    turns : list
        list of lists of lists consistu=ing of
        a one symbolstring and a list with length 2 - 4
        stores the information about turns
    turn_num : int
        number of the current turn
    international : bool
        whether this is the international version
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    turn_num : int
        number of the current turn

    '''
    for change in turns[turn_num - 1]:
        if change:
            if len(change[1]) == 4:
                board[change[1][2]][change[1][3]] = change[0]
                board[change[1][0]][change[1][1]] = '0'
                if change[0] == 'w' and change[1][2] == border - 1 and not international:
                    board[change[1][2]][change[1][3]] = 'm'
                elif change[0] == 'b' and change[1][2] == 0 and not international:
                    board[change[1][2]][change[1][3]] = 'p'
            else:
                board[change[1][0]][change[1][1]] = '0'
    if change and len(change[1]) == 4:
        if change[0] == 'w' and change[1][2] == border - 1 and international:
            board[change[1][2]][change[1][3]] = 'm'
        elif change[0] == 'b' and change[1][2] == 0 and international:
            board[change[1][2]][change[1][3]] = 'p'
    return(board, turn_num)

def binary_choice(message):
    '''
    presents the user with a message;
    lets the user choose between y or n

    Parameters
    ----------
    message : str
        what the user is presented with

    Returns
    -------
    bool
    what was the users choice

    '''
    choice = input(f'{message}\ny/n\n')
    while choice not in {'y', 'n'}:
        choice = input(f'{message}\ny/n\n')
    if choice == 'y':
        return(True)
    else:
        return(False)

def choice_of_two(message):
    '''
    presents the user with a message;
    lets the user choose between 1 or 0
    returns str value corresponding to the "board_colour"

    Parameters
    ----------
    message : str
        what the user is presented with

    Returns
    -------
    str
    what was the users choice

    '''
    choice = input(f'{message}\n1/0\n')
    while choice not in {'1', '2'}:
        choice = input(f'{message}\n1/0\n')
    return(str(int(choice) + 1))

def choice_of_three(message):
    '''
    presents the user with a message;
    lets the user choose between 1 or 2 or 3

    Parameters
    ----------
    message : str
        what the user is presented with

    Returns
    -------
    str
    what was the users choice

    '''
    out = input(f'{message}\n(1/2/3)\n')
    while not out in {'1', '2', '3'}:
        out = input(f'{message}\nInvalid imput\nTry again\n(1/2/3)\n')
    return(out)

def choice_of_four(message):
    '''
    presents the user with a message;
    lets the user choose between 0 or 1 or 2 or 3

    Parameters
    ----------
    message : str
        what the user is presented with

    Returns
    -------
    int
    what was the users choice

    '''
    out = input(f'{message}\n(0/1/2/3)\n')
    while not out in {'0', '1', '2', '3', }:
        out = input(f'{message}\nInvalid imput\nTry again\n(1/2/3)\n')
    return(int(out))

def validation(board, wh_turn, PvP, inv_count, board_colour, jumps, Ru, tries, length, turn_number, shift, border, start):
    '''
    lets through only the results that can be interprited by  the "player_turn"

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    wh_turn : bool
        whether the current turn is for whites
    PvP : bool
        whether it is the computer, or the player that makes the turn
    inv_count : int
        current number of invalid tryes
    board_colour : str
        1, 2 or 3
        changes the way board is printed
    jumps : bool
        whether a consecutive jump is possible
    Ru : bool
        rus. version
    tries : int
        number of invalid tries before the board is re printed
    length : int
        length of the list that stores the information about turns
    turn_number : int
        number of the current turn
    shift : bool
        "shifts" the background
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
    board_turn : list
        list of integers
        coordinates for the  "player_turn" function
    inv_count : int
        current number of invalid tryes

    '''
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')[:border]
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')[:border]
    board_turn = [0, 0, 0, 0]
    turn_N = False
    if not jumps or Ru:
        turn = input('\nxyxy\n')
        temp_m = 'invalid input format\ntry again:\n\nxyxy\n'
    else:
        turn = input('\nxyxy/N\n')
        turn_N = 'N'
        temp_m = 'invalid input format\ntry again:\n\nxyxy/N\n'
    while len(turn) not in {4, 5} and (len(turn) != 1 or turn[-1] != turn_N) and (len(turn) != 9 or turn != 'surrender') and (len(turn) != 3 or turn != 'tie'): # prevents errors if user doesent input anithing
        turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, temp_m, tries, shift, border, start)
        if turn == 'help':
            ch_help(board_colour)
            print_board(board, board_colour, shift, border, start)
            turn, inv_count = inv_input(0, board, PvP, wh_turn, board_colour, temp_m[32:], tries, shift, border, start)
    if len(turn) == 4:
        temp = -1
    else:
        temp = 0
    while not(turn[-1] == turn_N or turn == 'surrender' or (turn == 'undo' and turn_number != 0) or (turn == 'redo' and length > turn_number) or  turn == 'True' or(len(turn) == 4 and turn[0] in letters and turn[2] in letters and turn[1] in numbers and turn[3] in numbers and turn[0] != turn[2] and turn[1] != turn[3]) or (len(turn) == 5 and turn[0] in letters and turn[0] != turn[3] and turn[1] != turn[4] and (turn[3] in letters and turn[1:3] == '10' and turn[4] in numbers) or (turn[2] in letters and turn[1] in numbers and turn[3:5] == '10'))):
        if turn == 'help':
            ch_help(board_colour)
            print_board(board, board_colour, shift, border, start)
            turn, inv_count = inv_input(0, board, PvP, wh_turn, board_colour, temp_m[32:], tries, shift, border, start)
        elif turn == 'tie':
            turn = str(binary_choice('Do you accept?'))
            if turn == 'False':
                turn, inv_count = inv_input(0, board, PvP, wh_turn, board_colour, temp_m[32:], tries, shift, border, start)
        else:
            turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, temp_m, tries, shift, border)
        while len(turn) not in {4, 5} and (len(turn) != 1 or turn[-1] != turn_N) and (len(turn) != 9 or turn != 'surrender') and (len(turn) != 3 or turn != 'tie') and turn != 'True': # prevents errors if user doesent input anithing
            turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, temp_m, tries, shift, border, start)
            if turn == 'help':
                ch_help(board_colour)
                print_board(board, board_colour, shift, border, start)
                turn, inv_count = inv_input(0, board, PvP, wh_turn, board_colour, temp_m[32:], tries, shift, border, start)
        if len(turn) == 4:
            temp = -1
        else:
            temp = 0
    if turn[-1] == 'N':
        board_turn = 'N'
    elif turn == 'surrender':
        board_turn = 'surrender'
    elif turn == 'undo':
        board_turn = 'undo'
    elif turn == 'redo':
        board_turn = 'redo'
    elif turn == 'True':
        board_turn = 'True'
    else:
        turn_t = turn
        turn = []
        fl = False
        for simbol in turn_t:
            if simbol == '1':
                fl = True
                continue
            if fl:
                if simbol == '0':
                    turn.append('10')
                    fl = False
                    continue
                else:
                    turn.append('1')
                fl = False
            turn.append(simbol)
        if fl:
            if simbol == '1':
                turn.append('1')
        if len(turn_t) > len(turn):
            temp = -1
        for i in range(border):
            if turn[0] == letters[i]:
                board_turn[1] = i
            if turn[3 + temp] == letters[i]:
                board_turn[3] = i
            if turn[1] == numbers[i]:
                board_turn[0] = i
            if turn[4 + temp] == numbers[i]:
                board_turn[2] = i
    return(board_turn, inv_count)

def inv_input(inv_count, board, PvP, wh_turn, board_colour, message, tries, shift, border, start):
    '''
    prints the board after x invalid inputs by the user

    Parameters
    ----------
    inv_count : int
        current number of invalid tryes
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    PvP : bool
        whether it is the computer, or the player that makes the turn
    wh_turn : bool
        whether the current turn is for whites
    board_colour : str
        1, 2 or 3
        changes the way board is printed
    message : str
        what the user is presented with
    tries : int
        number of invalid tries before the board is re printed
    shift : bool
        "shifts" the background
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
   turn : str
       the coordinates
   inv_count : int
       current number of invalid tryes

    '''
    inv_count += 1
    turn = ''
    if inv_count == tries and PvP:
        print_board(board, board_colour, shift, border, start)
        if wh_turn:
            print('\nWhite turn\n')
        else:
            print('\nBlack turn\n')
        inv_count = 0
    turn = input(message)
    return(turn, inv_count)

def convert(turn):
    '''
    converts the "board_turn" back into the text form for display

    Parameters
    ----------
    turn : list
        list of integers
        coordinates from the  "player_turn" function

    Returns
    -------
    out : str
        the coordinates

    '''
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
    temp = []
    for i in range(4):
        if i == 1 or i == 3:
            temp.append(letters[turn[i]])
        else:
            temp.append(numbers[turn[i]])
    out = temp[1] + temp[0] + temp[3] + temp[2]
    return(out)

def usual_straight(wh_t, board_turn):
    '''
    checks if the coordinates correspond to a valid turn without jumps
    does not check for obstructions

    Parameters
    ----------
    wh_t : bool
        whether the current turn is for whites
    board_turn : list
        list of integers
        coordinates from the  "player_turn" function

    Returns
    -------
    None.

    '''
    if wh_t:
        temp_first = board_turn[0] + 1
    else:
        temp_first = board_turn[0] - 1
    return(temp_first == board_turn[2] and board_turn[1] + 1 == board_turn[3]) or (temp_first == board_turn[2] and board_turn[1] - 1 == board_turn[3])

def usual_attaks(board, board_turn, colour):
    '''
    checks if the coordinates correspond to a valid attak
    does not check for obstructions

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    board_turn : list
        list of integers
        coordinates from the  "player_turn" function
    colour : set
        figures that the enemy can have

    Returns
    -------
    usual_attak : bool
        is the figure attaking

    '''
    down_right = (board_turn[0] + 2 == board_turn[2] and board_turn[1] + 2 == board_turn[3]) and board[board_turn[0] + 1][board_turn[1] + 1] in colour # describes, when usual figure tries to eat ++
    down_left = (board_turn[0] + 2 == board_turn[2] and board_turn[1] - 2 == board_turn[3]) and board[board_turn[0] + 1][board_turn[1] - 1] in colour # +-
    up_right = (board_turn[0] - 2 == board_turn[2] and board_turn[1] + 2 == board_turn[3]) and board[board_turn[0] - 1][board_turn[1] + 1] in colour # -+
    up_left = (board_turn[0] - 2 == board_turn[2] and board_turn[1] - 2 == board_turn[3]) and board[board_turn[0] - 1][board_turn[1] - 1] in colour # --
    usual_attak = down_right or down_left or up_right or up_left
    return(usual_attak)

def king_turn(board, board_turn, colour, colour_t, border, international):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
   board_turn : list
       list of integers
       coordinates from the  "player_turn" function
    colour : set
        figures that the enemy can have
    colour_t : set
        figures that the enemy can have
    border : int
        8 or 10
        corresponds to the size of the board
    international : bool
        whether this is the international version

    Returns
    -------
    king_straight : bool
        is the cong moving in a straight line
    king_attaks : bool
        is the king attaking
    out : list
        lists consisting of
        a one symbol string and a list with length 2 - 4
        stores the information about the turn

    '''
    straight11, straight00, straight10, straight01 = False, False, False, False
    fig1, fig0, fig10, fig01, king_straight, king_attaks1, king_attaks0, king_attaks10, king_attaks01, king_attaks = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    fig_set = {'p', 'b', 'm', 'w'}
    attak_list = [[], [], [], []]
    fig_l = [False, False, False, False]
    out = []
    if board_turn[0] < board_turn[2]:
        if board_turn[1] < board_turn[3]:
            for i in range(1, border): # assining number of figures on the way of 'king' figure (figure, whitch got to the opposit end of the board) and describing patterns if movement
                if board_turn[0] + i == border or board_turn[1] + i == border: # prevents calculations from getting over the 'edge' of the board
                    break
                if board[board_turn[0] + i][board_turn[1] + i] in fig_set: # top left - bottom right ++
                    fig1 +=  1
                    if board[board_turn[0] + i][board_turn[1] + i] in colour:
                        fig_l[0] = True
                        attak_list[0].append(board[board_turn[0] + i][board_turn[1] + i])
                        attak_list[0].append([board_turn[0] + i, board_turn[1] + i])
                if board_turn[0] + i == board_turn[2] and board_turn[1] + i == board_turn[3]:
                    straight11 = True
                    break
        else:
            for z in range(1, border):
                if board_turn[0] + z == border or board_turn[1] - z == -1:
                    break
                if board[board_turn[0] + z][board_turn[1] - z] in fig_set: # top right - bottom left +-
                    fig10 += 1
                    if board[board_turn[0] + z][board_turn[1] - z] in colour:
                        fig_l[2] = True
                        attak_list[2].append(board[board_turn[0] + z][board_turn[1] - z])
                        attak_list[2].append([board_turn[0] + z, board_turn[1] - z])
                if board_turn[0] + z == board_turn[2] and board_turn[1] - z == board_turn[3]:
                    straight10 = True
                    break
    else:
        if board_turn[1] > board_turn[3]:
            for j in range(1, border):
                if board_turn[0] - j == -1 or board_turn[1] - j == -1:
                    break
                if board[board_turn[0] - j][board_turn[1] - j] in fig_set: # bottom right - top left --
                    fig0 += 1
                    if board[board_turn[0] - j][board_turn[1] - j] in colour:
                        fig_l[1] = True
                        attak_list[1].append(board[board_turn[0] - j][board_turn[1] - j])
                        attak_list[1].append([board_turn[0] - j, board_turn[1] - j])
                if board_turn[0] - j == board_turn[2] and board_turn[1] - j == board_turn[3]:
                    straight00 = True
                    break
        else:
            for k in range(1, border):
                if board_turn[0] - k == -1 or board_turn[1] + k == border:
                    break
                if board[board_turn[0] - k][board_turn[1] + k] in fig_set: # bottom left - top right -+
                    fig01 += 1
                    if board[board_turn[0] - k][board_turn[1] + k] in colour:
                        fig_l[3] = True
                        attak_list[3].append(board[board_turn[0] - k][board_turn[1] + k])
                        attak_list[3].append([board_turn[0] - k, board_turn[1] + k])
                if board_turn[0] - k == board_turn[2] and board_turn[1] + k == board_turn[3]:
                    straight01 = True
                    break
    if board[board_turn[0]][board_turn[1]] == colour_t:
        king_straight1 = fig1 == 0 and straight11  # getting information from four patterns above
        king_straight0 = fig0 == 0 and straight00
        king_straight10 = fig10 == 0 and straight10
        king_straight01 = fig01 == 0 and straight01
        king_straight = king_straight1 or king_straight10 or king_straight0 or king_straight01
        
        if international:
            king_attaks1 = straight11 and fig1 == 1 and fig_l[0]
            king_attaks0 = straight00 and fig0 == 1 and fig_l[1]
            king_attaks10 = straight10 and fig10 == 1 and fig_l[2]
            king_attaks01 = straight01 and fig01 == 1 and fig_l[3]
        else:
            king_attaks1 = straight11 and fig1 == 1 and board[board_turn[2] - 1][board_turn[3] - 1] in colour
            king_attaks0 = straight00 and fig0 == 1 and board[board_turn[2] + 1][board_turn[3] + 1] in colour
            king_attaks10 = straight10 and fig10 == 1 and board[board_turn[2] - 1][board_turn[3] + 1] in colour
            king_attaks01 = straight01 and fig01 == 1 and board[board_turn[2] + 1][board_turn[3] - 1] in colour
            
        if king_attaks1:
            out = attak_list[0]
        elif king_attaks0:
            out = attak_list[1]
        elif king_attaks10:
            out = attak_list[2]
        elif king_attaks01:
            out = attak_list[3]

        king_attaks = king_attaks1 or king_attaks0 or king_attaks10 or king_attaks01
    return(king_straight, king_attaks, out)

def turn_validation(board, board_turn, wh_t, list_attaks, val, border, international):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    board_turn : list
        list of integers
        coordinates from the  "player_turn" function
    wh_t : bool
        whether the current turn is for whites
    list_attaks : list
        list of lists of lists of 4 integers
        all possible coordinates for attaks
    val : bool
        can the board be changed
    border : int
        8 or 10
        corresponds to the size of the board
    international : bool
        whether this is the international version

    Returns
    -------
    None.

    '''
    if wh_t:
        colour = {'p','b'}
        colour_t = 'm'
    else:
        colour = {'m', 'w'}
        colour_t = 'p'
    attak = True
    usual_sraight = usual_straight(wh_t, board_turn) # describes 'straight' movement on board
    usual_attak = usual_attaks(board, board_turn, colour)
    king_straight, king_attaks = king_turn(board, board_turn, colour, colour_t, border, international)[:-1]
    if list_attaks != []:
        if not board_turn in list_attaks:
            attak = False
    return(attak and (usual_sraight or usual_attak or king_straight or king_attaks))

def in_list(list_1, board, colour, border):
    '''
    

    Parameters
    ----------
    list_1 : list
        list of lists of lists of 4 integers
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    colour : tuple
        figures corresponding to the turn colour
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
    flag : bool
        do any of the elements of the list trigger "acceptable_jump"

    '''
    flag = False
    for value in list_1:
        if acceptable_jump(value, board, colour, border):
            flag = True
    return(flag)

def gen_list(list_1, board, colour, border):
    temp_l = []
    for value in list_1:
        if acceptable_jump(value, board, colour, border):
            temp_l += [value]
    return(temp_l)

def colour_list(board, wh_turn, border, international):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    wh_turn : bool
        whether the current turn is for whites
    border : int
        8 or 10
        corresponds to the size of the board
    international : bool
        whether this is the international version

    Returns
    -------
    list_attaks : list
        list of lists of lists of 4 integers
        all possible coordinates for attaks

    '''
    fig_list, list_attaks, king_list, temp = [], [], [], []
    if wh_turn:
        col_usual = {'w'}
        col_king = 'm'
        col_enemy = {'p', 'b'}
    else:
        col_usual = {'b'}
        col_king = 'p'
        col_enemy = {'m', 'w'}
    for y in range(border):
        for x in range(border):
            if board[y][x] in col_usual: # add for m
                fig_list.append([y, x])       
            elif board[y][x] in col_king:
                king_list.append([y, x])
    for position in fig_list:
        for j in range(4):
            change_temp = ChangeOfTwo(position[0], position[1], j)
            temp = position + change_temp
            if change_temp[0] >= 0 and change_temp[1] <= border - 1 and change_temp[0] <= border - 1 and change_temp[1] >= 0 and board[change_temp[0]][change_temp[1]] == '0' and usual_attaks(board, temp, col_enemy):
                list_attaks.append(temp)
    for king in king_list:
        for y in range(border):
            for x in range(border):
                if board[y][x] == '0' and abs(king[0] - y) == abs(king[1] - x):
                    temp = king + [y, x]
                    if king_turn(board, temp, col_enemy, col_king, border, international)[1]:
                        list_attaks.append(temp)
    return(list_attaks)

def ChangeOfTwo(y, x, j):
    '''
    

    Parameters
    ----------
    y : int
        y coordinat
    x : int
        x coordinat
    j : int
        direction 0 - 3

    Returns
    -------
    None.

    '''
    if j == 0:
        output = [y + 2, x + 2]
    if j == 1:
        output = [y - 2, x - 2]
    if j == 2:
        output = [y - 2, x + 2]
    if j == 3:
        output = [y + 2, x - 2]
    return(output)

def acceptable_jump(board_turn, board, colours, border):
    '''
    

    Parameters
    ----------
    board_turn : list
        list of integers
        coordinates from the  "player_turn" function
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    colour : tuple
        figures corresponding to the turn colour
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
    acceptable : list
    list of lists with two integers
    second pair of coordinates for consecutive jumps

    '''
    acceptable = []
    if colours == ('m', 'w'):
        colour = {'p', 'b'}
    else:
        colour = {'m', 'w'}
    if board_turn[2] + 2 < border and board_turn[3] + 2 < border and board[board_turn[2] + 2][board_turn[3] + 2] == '0' and board[board_turn[2] + 1][board_turn[3] + 1] in colour and not (board_turn[0] > board_turn[2] and board_turn[1] > board_turn[3]): # top left - bottom right ++
        acceptable.append([board_turn[2] + 2, board_turn[3] + 2])
    if board_turn[2] - 2 > -1 and board_turn[3] - 2 > -1 and board[board_turn[2] - 2][board_turn[3] - 2] == '0' and board[board_turn[2] - 1][board_turn[3] - 1] in colour and not (board_turn[0] < board_turn[2] and board_turn[1] < board_turn[3]): # bottom right - top left --
        acceptable.append([board_turn[2] - 2, board_turn[3] - 2])
    if board_turn[2] + 2 < border and board_turn[3] - 2 > -1 and board[board_turn[2] + 2][board_turn[3] - 2] == '0' and board[board_turn[2] + 1][board_turn[3] - 1] in colour and not (board_turn[0] > board_turn[2] and board_turn[1] < board_turn[3]): # top right - bottom left +-
        acceptable.append([board_turn[2] + 2, board_turn[3] - 2])
    if board_turn[2] - 2 > -1 and board_turn[3] + 2 < border and board[board_turn[2] - 2][board_turn[3] + 2] == '0' and board[board_turn[2] - 1][board_turn[3] + 1] in colour and not (board_turn[0] < board_turn[2] and board_turn[1] > board_turn[3]): # bottom left - top right -+
        acceptable.append([board_turn[2] - 2, board_turn[3] + 2])
    return(acceptable)

def player_turn(board, wh_turn, Ru, PvP, board_colour, tries, length, turn_number, shift, border, international):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    wh_turn : bool
        whether the current turn is for whites
    Ru : bool
        rus. version
    PvP : bool
        whether it is the computer, or the player that makes the turn
    board_colour : str
        1, 2 or 3
        changes the way board is printed
    tries : int
        number of invalid tries before the board is re printed
    length : int
        length of the list that stores the information about turns
    turn_number : int
        number of the current turn
    shift : bool
        "shifts" the background
    border : int
        8 or 10
        corresponds to the size of the board
    international : bool
        whether this is the international version

    Returns
    -------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    board_turn : list or str
        list of integers
        coordinates from the  "player_turn" function
        or a command
    turn : list
        list of lists consisting of
        a one symbol string and a list with length 2 - 4
        stores the information about the turn
        

    '''
    C_l = []
    if international:
        C_l_temp = colour_list(board, wh_turn, border, True)
    C_l_jump = colour_list(board, wh_turn, border, False)
    turn = []
    if wh_turn: # white
        col = ('m', 'w')
    else:
        col = ('p', 'b')
    if Ru:
        if international:
            if in_list(C_l_jump, board, col, border):
                C_l = gen_list(C_l_jump, board, col, border)
            else:
                C_l = C_l_temp
        else:
            C_l = C_l_jump
    board_turn, inv_count = validation(board, wh_turn, PvP, 0, board_colour, False, Ru, tries, length, turn_number, shift, border, [])
    while board_turn != 'surrender' and board_turn != 'undo' and board_turn != 'redo' and board_turn != 'True' and not(board[board_turn[0]][board_turn[1]] in col and board[board_turn[2]][board_turn[3]] == '0' and turn_validation(board, board_turn, wh_turn, C_l, False, border, international)):
        if PvP:
            inv_count += 1
            if inv_count == tries:
                print_board(board, board_colour, shift, border, [])
                if wh_turn:
                    print('\nWhite turn\n')
                else:
                    print('\nBlack turn\n')
                inv_count = 0
            print('invalid turn\ntry again:')
        board_turn, inv_count = validation(board, wh_turn, PvP, inv_count, board_colour, False, Ru, tries, length, turn_number, shift, border, [])
    if board_turn != 'surrender' and board_turn != 'undo' and board_turn != 'redo' and board_turn != 'True':
        turn = val_turn(board, board_turn, international, wh_turn, border)
        board[board_turn[0]][board_turn[1]] = '0'
        if board_turn in C_l_jump:
            print_board(board, board_colour, shift, border, board_turn[-2:])
        else:
            print_board(board, board_colour, shift, border, [])
        if not(PvP):
            print(convert(board_turn))
        if board_turn in C_l_jump:
            acceptable = acceptable_jump(board_turn, board, col, border)
            while acceptable:
                temp = [board_turn[2], board_turn[3]]
                board_turn, inv_count = validation(board, wh_turn, PvP, inv_count, board_colour, True, Ru, tries, length, turn_number, shift, border, board_turn[-2:])
                while board_turn != 'N' and board_turn != 'surrender' and board_turn != 'undo' and board_turn != 'redo' and board_turn != 'True' and (board_turn[:2] != temp or board_turn[2:] not in acceptable):
                    if PvP:
                        inv_count += 1
                        if inv_count == tries:
                            print_board(board, board_colour, shift, border, board_turn[-2:])
                            if wh_turn:
                                print('\nWhite turn\n')
                            else:
                                print('\nBlack turn\n')
                            inv_count = 0
                        print('invalid turn\ntry again:')
                    board_turn, inv_count = validation(board, wh_turn, PvP, inv_count, board_colour, True, Ru, tries, length, turn_number, shift, border, board_turn[-2:])
                if board_turn == 'N':
                    print_board(board, board_colour, shift, border, [])
                    break
                elif board_turn == 'surrender' or board_turn == 'undo' or board_turn == 'redo' or board_turn == 'True':
                    break
                turn.extend(val_turn(board, board_turn, international, wh_turn, border))
                board[board_turn[0]][board_turn[1]] = '0'
                acceptable = acceptable_jump(board_turn, board, col, border)
                if acceptable:
                    print_board(board, board_colour, shift, border, board_turn[-2:])
                else:
                    print_board(board, board_colour, shift, border, [])
                if not PvP:
                    print(convert(board_turn))
        if international:
            if board_turn[2] == border -1 and wh_turn and board[board_turn[2]][board_turn[3]] == col[1]:
                board[board_turn[2]][board_turn[3]] = 'm'
                print_board(board, board_colour, shift, border, [])
            elif board_turn[2] == 0 and not wh_turn:
                board[board_turn[2]][board_turn[3]] = 'p'
                print_board(board, board_colour, shift, border, [])
    return(board, board_turn, turn)

def computer_turn(board, wh_turn, international, board_colour, shift, border):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    wh_turn : bool
        whether the current turn is for whites
    international : bool
        whether this is the international version
    board_colour : str
        1, 2 or 3
        changes the way board is printed
    shift : bool
        "shifts" the background
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    board_turn : list or str
        list of integers
        coordinates from the  "player_turn" function
        or a command
    turn : list
        list of lists consisting of
        a one symbol string and a list with length 2 - 4
        stores the information about the turn

    '''
    if wh_turn:
        col = 'w'
    else:
        col = 'b'
    temp = gen_turn_list(board, wh_turn, border, False, [])
    board_turn = temp[0][randint(0, len(temp[0]) - 1)]
    turn = val_turn(board, board_turn, international, wh_turn, border)
    print(convert(board_turn))
    print_board(board, board_colour, shift, border, [])
    if temp[1]:
        temp = gen_turn_list(board, wh_turn, border, False, board_turn[-2:])
    while temp[1]:
        board_turn = temp[0][randint(0, len(temp[0]) - 1)]
        turn = val_turn(board, board_turn, international, wh_turn, border)
        print(convert(board_turn))
        print_board(board, board_colour, shift, border, board_turn[-2:])
        temp = gen_turn_list(board, wh_turn, border, False, board_turn[-2:])
    if international:
        if board_turn[2] == border -1 and wh_turn and board[board_turn[2]][board_turn[3]] == col:
            board[board_turn[2]][board_turn[3]] = 'm'
            print_board(board, board_colour, shift, border, [])
        elif board_turn[2] == 0 and not wh_turn and board[board_turn[2]][board_turn[3]] == col:
            board[board_turn[2]][board_turn[3]] = 'p'
            print_board(board, board_colour, shift, border, [])
    return(board, board_turn, turn)
    
def val_turn(board, board_turn, international, wh_turn, border):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    board_turn : list
        list of integers
    international : bool
        whether this is the international version
    wh_turn : bool
        whether the current turn is for whites
    border : int
        8 or 10
        corresponds to the size of the board

    Returns
    -------
    turn : list
        list consisting of
        a one symbol string and a list with length 2 - 4
        stores the information about the turn

    '''
    if wh_turn:
        col_enemy = {'b', 'p'}
        colour_t = 'm'
        king_border = border - 1
    else:
        col_enemy = {'w', 'm'}
        colour_t = 'p'
        king_border = 0
    turn = [[board[board_turn[0]][board_turn[1]], board_turn[:]]]
    if abs(board_turn[0] - board_turn[2]) == 2 or (abs(board_turn[0] - board_turn[2]) > 2 and not international):
        turn += ['']
        if board_turn[0] < board_turn[2] and board_turn[1] < board_turn[3]:
            turn[1] = [board[board_turn[2] - 1][board_turn[3] - 1], [board_turn[2] - 1] + [board_turn[3] - 1]]
            board[board_turn[2] - 1][board_turn[3] - 1] = '0'
        elif board_turn[0] < board_turn[2] and board_turn[1] > board_turn[3]:
            turn[1] = [board[board_turn[2] - 1][board_turn[3] + 1], [board_turn[2] - 1] + [board_turn[3] + 1]]
            board[board_turn[2] - 1][board_turn[3] + 1] = '0'
        elif board_turn[0] > board_turn[2] and board_turn[1] < board_turn[3]:
            turn[1] = [board[board_turn[2] + 1][board_turn[3] - 1], [board_turn[2] + 1] + [board_turn[3] - 1]]
            board[board_turn[2] + 1][board_turn[3] - 1] = '0'
        elif board_turn[0] > board_turn[2] and board_turn[1] > board_turn[3]:
            turn[1] = [board[board_turn[2] + 1][board_turn[3] + 1], [board_turn[2] + 1] + [board_turn[3] + 1]]
            board[board_turn[2] + 1][board_turn[3] + 1] = '0'
    elif international and abs(board_turn[0] - board_turn[2]) > 2:
        turn += ['']
        for i in range(board_turn[0], board_turn[2]):
            j = board_turn[1] + i
            if board[i][j] in col_enemy:
                turn[1] = [board[i][j], [i] + [j]]
                board[i][j] = '0'
                break
    board[board_turn[2]][board_turn[3]] = board[board_turn[0]][board_turn[1]]
    board[board_turn[0]][board_turn[1]] = '0'
    if board_turn[2] == king_border and not international:
        board[board_turn[2]][board_turn[3]] = colour_t
    return(turn)

def read_board(board, wh_turn, border, international):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    wh_turn : bool
        whether the current turn is for whites
    border : int
        8 or 10
        corresponds to the size of the board
    international : bool
        whether this is the international version

    Returns
    -------
    flag : bool
    is the game impossible to continue

    '''
    flag = True
    c_list = []
    turn_possible = True
    u_set = {'w', 'b'}
    if wh_turn:
        c_set = {'w', 'm'}
        enemy_set = {'b', 'p'}
        colour_t = 'm'
    else:
        c_set = {'b', 'p'}
        enemy_set = {'w', 'm'}
        colour_t = 'p'
    for y in range(border):
        for x in range(border):
            if board[y][x] in c_set:
                c_list.append([y, x])
    for figure in c_list:
        for y in range(border):
            for x in range(border):
                if board[y][x] == '0' and abs(figure[0] - y) == abs(figure[1] - x):
                    if board[figure[0]][figure[1]] in u_set:
                        if abs(figure[0] - y) == 1:
                            temp = figure + [y, x]
                            if usual_straight(wh_turn, temp):
                                turn_possible = False
                                break
                        elif abs(figure[0] - y) == 2:
                            temp = figure + [y, x]
                            if usual_attaks(board, temp, enemy_set):
                                turn_possible = False
                                break
                    else:
                        temp = figure + [y, x]
                        l_temp = king_turn(board, temp, enemy_set, colour_t, border, international)
                        if l_temp[0] or l_temp[1]:
                            turn_possible = False
                            break
                
            if not turn_possible:
                break
        if not turn_possible:
            break
    if turn_possible:
        flag = False
        if wh_turn:
            print('\nBlacks win')
        else:
            print('\nWhites win')
    return(flag)

def l_gen(border, figure, wh_turn, enemy_set, colour_t, board, international, u_set, attak_u, attak_k, straight_u, straight_k, attak_k_1):
    for y in range(border):
        for x in range(border):
            if board[y][x] == '0' and abs(figure[0] - y) == abs(figure[1] - x):
                if board[figure[0]][figure[1]] in u_set:
                    if abs(figure[0] - y) == 1:
                        temp = figure + [y, x]
                        if usual_straight(wh_turn, temp):
                            straight_u.append(temp)
                    elif abs(figure[0] - y) == 2:
                        temp = figure + [y, x]
                        if usual_attaks(board, temp, enemy_set):
                            attak_u.append(temp)
                else:
                    temp = figure + [y, x]
                    l_temp = king_turn(board, temp, enemy_set, colour_t, border, international)
                    if not international:
                        l_temp_1 = king_turn(board, temp, enemy_set, colour_t, border, False)
                    if l_temp_1[1]:
                        attak_k_1.append(temp)
                    elif l_temp[0]:
                        straight_k.append(temp)
                    elif l_temp[1]:
                        attak_k.append(temp)
    return(straight_u, attak_u, attak_k_1, straight_k, attak_k)

def gen_turn_list(board, wh_turn, border, international, start):
    '''
    

    Parameters
    ----------
    board : list
        list of lists of strings of length 1
        stores the current state of the board
    wh_turn : bool
        whether the current turn is for whites
    border : int
        8 or 10
        corresponds to the size of the board
    international : bool
        whether this is the international version

    Returns
    -------
    temp_final : list
    list of lists with all possible turns for a colour

    '''
    c_list = []
    u_set = {'w', 'b'}
    attak_u = []
    attak_k = []
    attak_k_1 = []
    straight_u = []
    straight_k = []
    if wh_turn:
        c_set = {'w', 'm'}
        c_tup = ('m', 'w')
        enemy_set = {'b', 'p'}
        colour_t = 'm'
    else:
        c_set = {'b', 'p'}
        c_tup = ('b', 'p')
        enemy_set = {'w', 'm'}
        colour_t = 'p'
    if not start:
        for y in range(border):
            for x in range(border):
                if board[y][x] in c_set:
                    c_list.append([y, x])
        for figure in c_list:
            straight_u, attak_u, attak_k_1, straight_k, attak_k = l_gen(border, figure, wh_turn, enemy_set, colour_t, board, international, u_set, attak_u, attak_k, straight_u, straight_k, attak_k_1)
    else:
        straight_u, attak_u, attak_k_1, straight_k, attak_k = l_gen(border, start, wh_turn, enemy_set, colour_t, board, international, u_set, attak_u, attak_k, straight_u, straight_k, attak_k_1)
    if attak_u or attak_k or attak_k_1:
        temp_final = gen_list(attak_k_1 + attak_u, board, c_tup, border)
        if not temp_final:
            temp_final = attak_u + attak_k + attak_k_1
        return(temp_final, True)
    else:
        temp_final = straight_u + straight_k
        return(temp_final, False)

def main():
    Ru = True
    config = get_settings()
    if config.board_colour_ask == 'yes':
        board_colour = choice_of_three('What board type do you want to use?')
    else:
        board_colour = str(config.board_colour)
    if config.Board_creator == 'yes':
        new_board = binary_choice('Do you want to paste your own board?')
    else:
        new_board = False
    if new_board:
        board, White_turn, border, shift = board_creator(board_colour)
        if border == 10:
            international = True
        else:
            international = False
    else:
        if config.game_type == 2:
            international = True
            border = 10
            board = [['_', 'w', '_', 'w', '_', 'w', '_', 'w', '_', 'w'],
                     ['w', '_', 'w', '_', 'w', '_', 'w', '_', 'w', '_'],
                     ['_', 'w', '_', 'w', '_', 'w', '_', 'w', '_', 'w'],
                     ['w', '_', 'w', '_', 'w', '_', 'w', '_', 'w', '_'],
                     ['_', '0', '_', '0', '_', '0', '_', '0', '_', '0'],
                     ['0', '_', '0', '_', '0', '_', '0', '_', '0', '_'],
                     ['_', 'b', '_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                     ['b', '_', 'b', '_', 'b', '_', 'b', '_', 'b', '_'],
                     ['_', 'b', '_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                     ['b', '_', 'b', '_', 'b', '_', 'b', '_', 'b', '_']]
            shift = True
                
        else:
            border = 8
            international = False
            if config.shift == 'no':
                board = [['w', '_', 'w', '_', 'w', '_', 'w', '_'],
                         ['_', 'w', '_', 'w', '_', 'w', '_', 'w'],
                         ['w', '_', 'w', '_', 'w', '_', 'w', '_'],
                         ['_', '0', '_', '0', '_', '0', '_', '0'],
                         ['0', '_', '0', '_', '0', '_', '0', '_'],
                         ['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                         ['b', '_', 'b', '_', 'b', '_', 'b', '_'],
                         ['_', 'b', '_', 'b', '_', 'b', '_', 'b']]
                shift = False
            else:
                board = [['_', 'w', '_', 'w', '_', 'w', '_', 'w'],
                         ['w', '_', 'w', '_', 'w', '_', 'w', '_'],
                         ['_', 'w', '_', 'w', '_', 'w', '_', 'w'],
                         ['0', '_', '0', '_', '0', '_', '0', '_'],
                         ['_', '0', '_', '0', '_', '0', '_', '0'],
                         ['b', '_', 'b', '_', 'b', '_', 'b', '_'],
                         ['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                         ['b', '_', 'b', '_', 'b', '_', 'b', '_']]
                board = [['_', '0', '_', '0', '_', '0', '_', '0'],
                         ['0', '_', '0', '_', '0', '_', '0', '_'],
                         ['_', 'b', '_', '0', '_', '0', '_', 'm'],
                         ['0', '_', 'm', '_', '0', '_', '0', '_'],
                         ['_', '0', '_', 'b', '_', 'b', '_', 'm'],
                         ['b', '_', 'b', '_', '0', '_', 'b', '_'],
                         ['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                         ['b', '_', 'b', '_', 'b', '_', '0', '_']]
                shift = True
        White_turn = True
    if config.hint == 'yes':
        ch_help(board_colour)
    if config.question_test == 'yes':
        pve = choice_of_four('What combination do you want to play?')
    else:
        pve = config.pve
    if pve == 0 or pve == 1:
        PvP = True
    elif pve == 2 or pve == 3:
        PvP = False
    tries = config.num_of_tries
    print_board(board, board_colour, shift, border, [])
    turn_num = 0
    turns = []
    while read_board(board, White_turn, border, international):
        turn_num += 1
        print(f'\nTurn {turn_num}')
        if White_turn:
            print('White turn')
        else:
            print('Black turn')
        if PvP:
            board, board_turn, turn_temp = player_turn(board, White_turn, Ru, PvP, board_colour, tries, len(turns), turn_num - 1, shift, border, international)
        else:
            board, board_turn, turn_temp = computer_turn(board, White_turn, international, board_colour, shift, border)
        if turn_temp:
            turns[:] = turns[:turn_num - 1]
            turns.append(turn_temp)
            turn_flag = True
            for trn in range(len(turns) - 1, len(turns) - 21, -1):
                if turn_num < 20:
                    turn_flag = False
                    break
                elif turns[trn][0][0] in {'w', 'b'}:
                    turn_flag = False
                    break
            if turn_flag:
                print('Tie')
                break
        if board_turn == 'surrender':
            if White_turn:
                print('\nBlacks win')
            else:
                print('\nWhites win')
            break
        elif board_turn == 'True':
            print('\nTie accepted')
            break
        elif board_turn == 'undo':
            board, turn_num = board_undo(board, turns, turn_num)
            if (pve == 2 and turn_num > 1) or (pve == 1 and turn_num > 0):
                turn_num += 1
                board, turn_num = board_undo(board, turns, turn_num)
            print_board(board, board_colour, shift, border, [])
        elif board_turn == 'redo':
            board, turn_num = board_redo(board, turns, turn_num, international, border)
            if pve != 0:
                turn_num += 1
                board, turn_num = board_redo(board, turns, turn_num, international, border)
            print_board(board, board_colour, shift, border, [])
        if turn_num % 2 == 1:
            White_turn = False
            if pve == 1:
                PvP = False
            elif pve == 2:
                PvP = True
        else:
            White_turn = True
            if pve == 1:
                PvP = True
            elif pve == 2:
                PvP = False

if __name__ == '__main__':
    main()
