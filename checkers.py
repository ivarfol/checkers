'''
Program for testing the russian checkers
'''
from random import randint
from config_reader import get_settings

def print_board(board, PvP, inv):
    numb = '12345678'
    if inv == '2':
        colour = '\033[47m'
        colour_op = '\033[40m'
        colour_hide = '\033[37m'
        colour_zero = '\033[30m'
        usual_w = '\u25CF'
        damk_w = '\u25C6'
        usual_b = '\u25CB'
        damk_b = '\u25C7'
    elif inv == '3':
        colour = '\033[40m'
        colour_op = '\033[47m'
        colour_hide = '\033[30m'
        colour_zero = '\033[37m'
        usual_w = '\u25CB'
        damk_w = '\u25C7'
        usual_b = '\u25CF'
        damk_b = '\u25C6'
    elif inv == '1':
        colour = '\033[0m'
        colour_op = '\033[0m'
        colour_hide = '\033[0m'
        colour_zero = '\033[0m'
        usual_w = 'w'
        damk_w = 'm'
        usual_b = 'b'
        damk_b = 'p'
    if PvP:
        print('\n  a b c d e f g h')
        for j in range(8):
            print(numb[j], end=' ')
            for x in range(8):
                if x % 2 == j % 2:
                    print(colour_op, end='')
                else:
                    print(colour, end='')
                if board[j][x] == '_':
                    print(colour_hide, end='')
                elif board[j][x] == '0':
                    print(colour_zero, end='')
                elif inv == '3':
                    print(colour_hide, end='')
                if board[j][x] == 'w':
                    print(usual_w, end=' ')
                elif board[j][x] == 'm':
                    print(damk_w, end=' ')
                elif board[j][x] == 'b':
                    print(usual_b, end=' ')
                elif board[j][x] == 'p':
                    print(damk_b, end=' ')
                else:
                    print(' '.join(board[j][x]), end=' ')
                print('\033[0m', end='')
            print(f'\033[0m{numb[j]}')
        print('  a b c d e f g h')
    else:
        print('\n 01234567')
        for i in range(8):
            print('01234567'[i], end='')
            for x in range(8):
                if x % 2 == i % 2:
                    print(colour_op, end='')
                else:
                    print(colour, end='')
                if board[i][x] == '_':
                    print(colour_hide, end='')
                elif board[i][x] == '0':
                    print(colour_zero, end='')
                elif inv == '3':
                    print(colour_hide, end='')
                print(''.join(board[i][x]), end='')
                print('\033[0m', end='')
            print('\033[0m')
        print('White', colour_list(board, True))
        print('Black', colour_list(board, False))
        
def board_creator(board_colour):
    board_list = []
    temp_list = []
    pvp = binary_choice('Were you playing PvP?', 1)
    board = input('Paste your board:\n')
    col = choice_of_three("What board type do you want to use?\n(if you didn't change anithing choose 2")
    if pvp:
        board = board[20:178]
        board = board.split(' ')
        for i in range(0,64,8):
            temp_list = board[i + int(i / 8):i + int(i / 8) + 8]
            for x in range(8):
                if col == '2':
                    if temp_list[x] == '●':
                        temp_list[x] = 'w'
                    elif temp_list[x] == '○':
                        temp_list[x] = 'b'
                    elif temp_list[x] == '◆':
                        temp_list[x] = 'm'
                    elif temp_list[x] == '◇':
                        temp_list[x] = 'p'
                elif col == '3':
                    if temp_list[x] == '●':
                        temp_list[x] = 'b'
                    elif temp_list[x] == '○':
                        temp_list[x] = 'w'
                    elif temp_list[x] == '◆':
                        temp_list[x] = 'p'
                    elif temp_list[x] == '◇':
                        temp_list[x] = 'm'
            board_list.append(temp_list)
    else:
        board = board[11:]
        for i in range(0,64,8):
            temp = board[i + int(i / 4):i + int(i / 4) + 8]
            temp_list.extend(temp)
            board_list.append(temp_list)
            temp_list = []
    if col != board_colour:
        print_board(board_list, pvp, col)
    print_board(board_list, pvp, board_colour)
    Wh_turn = binary_choice('\nWhose turn was that?\nWhite(1), Black(0)', 2)
    return(board_list, Wh_turn)

def ch_help(col):
    if col == '1':
        colour = '\033[0m'
        colour_op = '\033[0m'
        colour_u = '\033[0m'
        colour_hide = '\033[0m'
        u_wh = 'w'
        u_bl = 'b'
        damk_wh = 'm'
        damk_bl = 'p'
    elif col == '2':
        colour = '\033[0;40m'
        colour_op = '\033[47;37m'
        colour_u = '\033[0m'
        colour_hide = '\033[30m'
        u_wh = '●'
        u_bl = '○'
        damk_wh = '◆'
        damk_bl = '◇'
    else:
        colour = '\033[47;30m'
        colour_op = '\033[40;30m'
        colour_u = '\033[0m'
        colour_hide = '\033[37m'
        u_wh = '○'
        u_bl = '●'
        damk_wh = '◇'
        damk_bl = '◆'
    print('\nHelp')
    choice = choice_of_three('Do you want to continue to\ninputs(1), figures(2), exit(3)')
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
            print(f'dama/king white - {colour}{damk_wh}{colour_u}')
            print(f'dama/king black - {colour}{damk_bl}{colour_u}')
            if binary_choice('Do you want to learn about turn patterns?', 1):
                print('x - marks the possible turns')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u} - usual figures can go diagonally in one')
                print(f'{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_bl} {colour_op}_ {colour_u}│{colour_op}_ {colour}x {colour_op}_ {colour}{u_wh} {colour_op}_ {colour_u}   direction, and attak by jumping over the')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{u_wh} {colour_op}_ {colour}{colour_hide}0 {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{u_bl} {colour_op}_ {colour}{colour_hide}0 {colour_u}   enemy in all four directions')
                print(f'{colour_op}_ {colour}x {colour_op}_ {colour}{u_bl} {colour_op}_ {colour_u}│{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_wh} {colour_op}_ {colour_u}   they can move only one space when not attaking')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x ')
                print()
                print(f'{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_op}_ {colour_u}│{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_op}_ {colour_u} - dama/king figures can go diagonally in all')
                print(f'{colour_op}_ {colour}x {colour_op}_ {colour}{u_bl} {colour_op}_ {colour}{colour_hide}0 {colour_u}│{colour_op}_ {colour}x {colour_op}_ {colour}{u_wh} {colour_op}_ {colour}{colour_hide}0 {colour_u}   directions, and attak by jumping over the')
                print(f'{colour}{colour_hide}0 {colour_op}_ {colour}{damk_wh} {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour_u}│{colour}{colour_hide}0 {colour_op}_ {colour}{damk_bl} {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour_u}   enemy in all directions')
                print(f'{colour_op}_ {colour}x {colour_op}_ {colour}x {colour_op}_ {colour}{colour_hide}0 {colour_u}│{colour_op}_ {colour}x {colour_op}_ {colour}x {colour_op}_ {colour}{colour_hide}0 {colour_u}   the can move as many spaces as there are')
                print(f'{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_bl} {colour_op}_ {colour_u}│{colour}x {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{u_wh} {colour_op}_ {colour_u}   free spaces in diogonal')
                print(f'{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}│{colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}{colour_hide}0 {colour_op}_ {colour}x {colour_u}   they can attak any enemy on the diogonal')
                print(colour_u, end='')
        choice = choice_of_three('Do you want to continue to\ninputs(1), figures(2), exit(3)')
    print('Exit')

def board_undo(board, turn, turn_num):
    turn_num -= 2
    for i in range(len(turn[turn_num]) - 1, -1, -1):
        change = turn[turn_num][i]
        if change:
            if len(change[1]) == 4:
                board[change[1][0]][change[1][1]] = change[0]
                board[change[1][2]][change[1][3]] = '0'
            else:
                board[change[1][0]][change[1][1]] = change[0]
    return(board, turn_num)

def board_redo(board, turn, turn_num):
    for change in turn[turn_num - 1]:
        if change:
            if len(change[1]) == 4:
                board[change[1][2]][change[1][3]] = change[0]
                board[change[1][0]][change[1][1]] = '0'
                if change[0] == 'w' and change[1][2] == 7:
                    board[change[1][2]][change[1][3]] = 'm'
                elif change[0] == 'b' and change[1][2] == 0:
                    board[change[1][2]][change[1][3]] = 'p'
            else:
                board[change[1][0]][change[1][1]] = '0'
    return(board, turn_num)

def ChangeOfTwo(y, x, j):
    if j == 0:
        output = [y + 2, x + 2]
    if j == 1:
        output = [y - 2, x - 2]
    if j == 2:
        output = [y - 2, x + 2]
    if j == 3:
        output = [y + 2, x - 2]
    return(output)

def binary_choice(message, choice_type):
    if choice_type == 1:
        choice = 'y/n'
        choice_set = {'y', 'n'}
    else:
        choice = '1/0'
        choice_set = {'1', '0'}
    choice = input(f'{message}\n{choice}\n')
    while choice not in choice_set:
        choice = input(f'{message}\n{choice}\n')
    if choice == 'y' or choice == '1':
        return(True)
    else:
        return(False)

def choice_of_three(message):
    out = input(f'{message}\n(1/2/3)\n')
    while not out in {'1', '2', '3'}:
        out = input(f'{message}\nInvalid imput\nTry again\n(1/2/3)\n')
    return(out)

def turn_Nf(turn, turn_N):
    if turn_N:
        return(turn != turn_N)
    else:
        return(True)

def RndInput1(board, wh_turn, message, PvP):# chek global variables in functions for IDLE
    if PvP:
        output = input(message)
    else:
        if wh_turn:
            colour_set = {'w', 'm'}
        else:
            colour_set = {'b', 'p'}
        letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        numbers = ('1', '2', '3', '4', '5', '6', '7', '8')
        colour_list = []
        for y in range(8):
            for x in range(8):
                if board[y][x] in colour_set:
                    colour_list.append(f'{letters[x]}{numbers[y]}')
        output = colour_list[randint(0, len(colour_list) - 1)] + letters[randint(0, 7)] + numbers[randint(0, 7)]
    return(output)

def RndInput2(message, PvP):
    if PvP:
        output = input(message)
    else:
        output = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')[randint(0, 7)] + ('1', '2', '3', '4', '5', '6', '7', '8')[randint(0, 7)]
    return(output)

def validation(board, wh_turn, PvP, inv_count, board_colour, start, Ru, tries, length, turn_number): # prevents user from inputting invalid inputs
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8')
    board_turn = [0, 0, 0, 0] # list for coordinats
    turn_N = False
    if start == '':
        turn = RndInput1(board, wh_turn, '\nxy:xy\n', PvP)
        inp_type = '0'
        temp_m = 'invalid input format\ntry again:\n\nxy:xy\n'
    else:
        if Ru:
            inp_type = '1'
            turn = RndInput2(f'\nxy:xy\n{start}', PvP)
            turn = start + turn
            temp_m = 'invalid input format\ntry again:\n\nxy:xy\n' + start
        else:
            inp_type = '3'
            turn = RndInput2(f'\nxy:xy/N\n{start}', PvP)
            turn = start + turn
            turn_N = 'N'
            temp_m = 'invalid input format\ntry again:\n\nxy:xy/N\n' + start
    while len(turn) not in {4, 5} and (not len(turn) >= 1 or turn_Nf(turn[-1], turn_N)) and (not len(turn[len(start):]) == 9 or turn[len(start):] != 'surrender'): # prevents errors if user doesent input anithing
        turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, temp_m, tries)
        if turn[len(start):] == 'help':
            ch_help(board_colour)
            turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, temp_m[32:], tries)
        else:
            turn = start + turn
    if len(turn) == 4:
        temp = -1
    else:
        temp = 0
    while not(not turn_Nf(turn[-1], turn_N) or turn[len(start):] == 'surrender' or (turn[len(start):] == 'undo' and turn_number != 0) or (turn[len(start):] == 'redo' and length > turn_number) or (turn[0] in letters and turn[3 + temp] in letters and turn[1] in numbers and turn[4 + temp] in numbers)):
        if turn[len(start):] == 'help':
            ch_help(board_colour)
            turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, temp_m[32:], tries)
        else:
            turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, temp_m, tries)
            turn = start + turn
        while len(turn) not in {4, 5} and (not len(turn) >= 1 or turn_Nf(turn[-1], turn_N) and (not len(turn[len(start):]) == 9 or turn[len(start):] != 'surrender')): # prevents errors if user doesent input anithing
            turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, temp_m, tries)
            if turn[len(start):] == 'help':
                ch_help(board_colour)
                turn, inv_count = inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, temp_m[32:], tries)
            else:
                turn = start + turn
        if len(turn) == 4:
            temp = -1
        else:
            temp = 0
    if turn[-1] == 'N':
        board_turn = 'N'
    elif turn[len(start):] == 'surrender':
        board_turn = 'surrender'
    elif turn[len(start):] == 'undo':
        board_turn = 'undo'
    elif turn[len(start):] == 'redo':
        board_turn = 'redo'
    else:
        for i in range(8):
            if turn[0] == letters[i]: # writes coordinats down into the list above, so it wuld be easyer to use coordinats later in the program
                board_turn[1] = i
            if turn[3 + temp] == letters[i]:
                board_turn[3] = i
            if turn[1] == numbers[i]:
                board_turn[0] = i
            if turn[4 + temp] == numbers[i]:
                board_turn[2] = i
    return(board_turn, inv_count) # returns the list to player_turn function

def inv_input(inv_count, board, PvP, wh_turn, board_colour, inp_type, message, tries):
    inv_count += 1
    turn = ''
    if inv_count == tries:
        print_board(board, PvP, board_colour)
        if wh_turn:
            print('\nWhite turn\n')
        else:
            print('\nBlack turn\n')
        inv_count = 0
    if inp_type == '0':
        turn = RndInput1(board, turn, message, PvP)
    elif inp_type == '1':
        turn = RndInput2(message, PvP)
    else:
        turn = RndInput2(message, PvP)
    return(turn, inv_count)

def usual_attaks(board, board_turn, colour):
    down_right = (board_turn[0] + 2 == board_turn[2] and board_turn[1] + 2 == board_turn[3]) and board[board_turn[0] + 1][board_turn[1] + 1] in colour # describes, when usual figure tries to eat ++
    down_left = (board_turn[0] + 2 == board_turn[2] and board_turn[1] - 2 == board_turn[3]) and board[board_turn[0] + 1][board_turn[1] - 1] in colour # +-
    up_right = (board_turn[0] - 2 == board_turn[2] and board_turn[1] + 2 == board_turn[3]) and board[board_turn[0] - 1][board_turn[1] + 1] in colour # -+
    up_left = (board_turn[0] - 2 == board_turn[2] and board_turn[1] - 2 == board_turn[3]) and board[board_turn[0] - 1][board_turn[1] - 1] in colour # --
    usual_eats = down_right or down_left or up_right or up_left
    return(down_right, down_left, up_right, up_left, usual_eats)

def damka_turn(board, board_turn, colour, colour_t):
    straight11, straight00, straight10, straight01 = False, False, False, False
    fig1, fig0, fig10, fig01, damka_straight, damka_eats1, damka_eats0, damka_eats10, damka_eats01, damka_eats = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    fig_set = {'p', 'b', 'm', 'w'}
    for i in range(1, 8): # assining number of figures on the way of 'damka' figure (figure, whitch got to the opposit end of the board) and describing patterns if movement
        if board_turn[0] + i == 8 or board_turn[1] + i == 8: # prevents calculations from getting over the 'edge' of the board
            break
        if board[board_turn[0] + i][board_turn[1] + i] in fig_set: # top left - bottom right ++
            fig1 +=  1
        if board_turn[0] + i == board_turn[2] and board_turn[1] + i == board_turn[3]:
            straight11 = True
            break

    for j in range(1, 8):
        if board_turn[0] - j == -1 or board_turn[1] - j == -1:
            break
        if board[board_turn[0] - j][board_turn[1] - j] in fig_set: # bottom right - top left --
            fig0 += 1
        if board_turn[0] - j == board_turn[2] and board_turn[1] - j == board_turn[3]:
            straight00 = True
            break

    for z in range(1, 8):
        if board_turn[0] + z == 8 or board_turn[1] - z == -1:
            break
        if board[board_turn[0] + z][board_turn[1] - z] in fig_set: # top right - bottom left +-
            fig10 += 1
        if board_turn[0] + z == board_turn[2] and board_turn[1] - z == board_turn[3]:
            straight10 = True
            break

    for k in range(1, 8):
        if board_turn[0] - k == -1 or board_turn[1] + k == 8:
            break
        if board[board_turn[0] - k][board_turn[1] + k] in fig_set: # bottom left - top right -+
            fig01 += 1
        if board_turn[0] - k == board_turn[2] and board_turn[1] + k == board_turn[3]:
            straight01 = True
            break
    if board[board_turn[0]][board_turn[1]] == colour_t:
        damka_straight1 = fig1 == 0 and straight11 == True # getting information from four patterns above
        damka_straight0 = fig0 == 0 and straight00 == True
        damka_straight10 = fig10 == 0 and straight10 == True
        damka_straight01 = fig01 == 0 and straight01 == True
        damka_straight = damka_straight1 or damka_straight10 or damka_straight0 or damka_straight01

        damka_eats1 = straight11 == True and fig1 == 1 and board[board_turn[2] - 1][board_turn[3] - 1] in colour
        damka_eats0 = straight00 == True and fig0 == 1 and board[board_turn[2] + 1][board_turn[3] + 1] in colour
        damka_eats10 = straight10 == True and fig10 == 1 and board[board_turn[2] - 1][board_turn[3] + 1] in colour
        damka_eats01 = straight01 == True and fig01 == 1 and board[board_turn[2] + 1][board_turn[3] - 1] in colour
        damka_eats = damka_eats1 or damka_eats0 or damka_eats10 or damka_eats01
    return(damka_straight, damka_eats1, damka_eats0, damka_eats10, damka_eats01, damka_eats)

def turn_validation(board, board_turn, wh_t, l_attak, val): #prevents user from imputting wrong coordinats the right way
    if wh_t:
        colour = {'p','b'}
        colour_t = 'm'
        temp_first = board_turn[0] + 1
        damka_border = 7
    else:
        colour = {'m', 'w'}
        colour_t = 'p'
        temp_first = board_turn[0] - 1
        damka_border = 0
    attak = True
    turn = []
    usual_sraight = (temp_first == board_turn[2] and board_turn[1] + 1 == board_turn[3]) or (temp_first == board_turn[2] and board_turn[1] - 1 == board_turn[3]) # describes 'straight' movement on board
    down_right, down_left, up_right, up_left, usual_eats = usual_attaks(board, board_turn, colour)
    damka_straight, damka_eats1, damka_eats0, damka_eats10, damka_eats01, damka_eats = damka_turn(board, board_turn, colour, colour_t) 
    if l_attak != []:
        if not board_turn in l_attak:
            attak = False
    
    if val == True:
        turn = [[board[board_turn[0]][board_turn[1]], board_turn[:]], []]
        board[board_turn[2]][board_turn[3]] = board[board_turn[0]][board_turn[1]]
        if board_turn[2] == damka_border:
            board[board_turn[2]][board_turn[3]] = colour_t
        if usual_eats == True or damka_eats == True:
            if down_right == True or damka_eats1 == True:
                turn[1] = [board[board_turn[2] - 1][board_turn[3] - 1], [board_turn[2] - 1] + [board_turn[3] - 1]]
                board[board_turn[2] - 1][board_turn[3] - 1] = '0'
            elif down_left == True or damka_eats10 == True:
                turn[1] = [board[board_turn[2] - 1][board_turn[3] + 1], [board_turn[2] - 1] + [board_turn[3] + 1]]
                board[board_turn[2] - 1][board_turn[3] + 1] = '0'
            elif up_right == True or damka_eats01 == True:
                turn[1] = [board[board_turn[2] + 1][board_turn[3] - 1], [board_turn[2] + 1] + [board_turn[3] - 1]]
                board[board_turn[2] + 1][board_turn[3] - 1] = '0'
            elif up_left == True or damka_eats0 == True:
                turn[1] = [board[board_turn[2] + 1][board_turn[3] + 1], [board_turn[2] + 1] + [board_turn[3] + 1]]
                board[board_turn[2] + 1][board_turn[3] + 1] = '0'
    return(attak and (usual_sraight or usual_eats or damka_straight or damka_eats), turn)

def colour_list(board, turn):
    fig_list, list_eats, damka_list, temp = [], [], [], []
    if turn:
        col_usual = {'w'}
        col_damka = 'm'
        col_enemy = {'p', 'b'}
    else:
        col_usual = {'b'}
        col_damka = 'p'
        col_enemy = {'m', 'w'}
    for y in range(8):
        for x in range(8):
            if board[y][x] in col_usual: # add for m
                fig_list.append([y, x])       
            elif board[y][x] in col_damka:
                damka_list.append([y, x])
    for position in fig_list:
        for j in range(4):
            change_temp = ChangeOfTwo(position[0], position[1], j)
            temp = position + change_temp
            if change_temp[0] >= 0 and change_temp[1] <= 7 and change_temp[0] <= 7 and change_temp[1] >= 0 and board[change_temp[0]][change_temp[1]] == '0' and usual_attaks(board, temp, col_enemy)[4]:
                list_eats.append(temp)
    for damka in damka_list:
        for y in range(8):
            for x in range(8):
                if board[y][x] == '0':
                    temp = damka + [y, x]
                    if damka_turn(board, temp, col_enemy, col_damka)[5]:
                        list_eats.append(temp)
    return(list_eats)

def acceptable_jump(board_turn, board, colour):
    acceptable = []
    if colour == ('m', 'w'):
        colour = {'p', 'b'}
    else:
        colour = {'m', 'w'}
    if board_turn[2] + 2 < 8 and board_turn[3] + 2 < 8 and board[board_turn[2] + 2][board_turn[3] + 2] == '0' and board[board_turn[2] + 1][board_turn[3] + 1] in colour: # top left - bottom right ++
        acceptable.append([board_turn[2] + 2, board_turn[3] + 2])
    if board_turn[2] - 2 > -1 and board_turn[3] - 2 > -1 and board[board_turn[2] - 2][board_turn[3] - 2] == '0' and board[board_turn[2] - 1][board_turn[3] - 1] in colour: # bottom right - top left --
        acceptable.append([board_turn[2] - 2, board_turn[3] - 2])
    if board_turn[2] + 2 < 8 and board_turn[3] - 2 > -1 and board[board_turn[2] + 2][board_turn[3] - 2] == '0' and board[board_turn[2] + 1][board_turn[3] - 1] in colour: # top right - bottom left +-
        acceptable.append([board_turn[2] + 2, board_turn[3] - 2])
    if board_turn[2] - 2 > -1 and board_turn[3] + 2 < 8 and board[board_turn[2] - 2][board_turn[3] + 2] == '0' and board[board_turn[2] - 1][board_turn[3] + 1] in colour: # bottom left - top right -+
        acceptable.append([board_turn[2] - 2, board_turn[3] + 2])
    return(acceptable)

def player_turn(board, wh_tur, Ru, PvP, board_colour, tries, length, turn_number): # makes a move, checks if it is valid
    C_l = []
    C_l_temp = colour_list(board, wh_tur)
    turn = []
    if Ru:
        C_l = C_l_temp
    if wh_tur: # white
        col = ('m', 'w')
    else:
        col = ('p', 'b')
    board_turn, inv_count = validation(board, wh_tur, PvP, 0, board_colour, '', Ru, tries, length, turn_number)
    while board_turn != 'surrender' and board_turn != 'undo' and board_turn != 'redo' and not(board[board_turn[0]][board_turn[1]] in col and board[board_turn[2]][board_turn[3]] == '0' and turn_validation(board, board_turn, wh_tur, C_l, False)[0]):
        if PvP:
            inv_count += 1
            if inv_count == tries:
                print_board(board, PvP, board_colour)
                if wh_tur:
                    print('\nWhite turn\n')
                else:
                    print('\nBlack turn\n')
                inv_count = 0
            print('invalid turn\ntry again:')
        board_turn, inv_count = validation(board, wh_tur, PvP, inv_count, board_colour, '', Ru, tries, length, turn_number)
    if board_turn != 'surrender' and board_turn != 'undo' and board_turn != 'redo':
        turn = turn_validation(board, board_turn, wh_tur, C_l, True)[1]
        board[board_turn[0]][board_turn[1]] = '0'
        print_board(board, PvP, board_colour)
        if not(PvP):
            print(*board_turn)
        if board_turn in C_l_temp:
            acceptable = acceptable_jump(board_turn, board, col)
            while acceptable:
                temp = 'abcdefgh'[board_turn[3]] + '12345678'[board_turn[2]]
                board_turn, inv_count = validation(board, wh_tur, PvP, inv_count, board_colour, temp, Ru, tries, length, turn_number)
                while board_turn != 'N' and board_turn != 'surrender' and board_turn != 'undo' and board_turn != 'redo' and (not board_turn[-2:] in acceptable):
                    if PvP:
                        inv_count += 1
                        if inv_count == tries:
                            print_board(board, PvP, board_colour)
                            if wh_tur:
                                print('\nWhite turn\n')
                            else:
                                print('\nBlack turn\n')
                            inv_count = 0
                        print('invalid turn\ntry again:')
                    board_turn, inv_count = validation(board, wh_tur, PvP, inv_count, board_colour, temp, Ru, tries, length, turn_number)
                if board_turn == 'N':
                    print_board(board, PvP, board_colour)
                    break
                elif board_turn == 'surrender' or board_turn == 'undo' or board_turn == 'redo':
                    break
                turn.extend(turn_validation(board, board_turn, wh_tur, [], True)[1])
                board[board_turn[0]][board_turn[1]] = '0'
                print_board(board, PvP, board_colour)
                if not(PvP):
                    print(*board_turn)
                acceptable = acceptable_jump(board_turn, board, col)
    return(board, board_turn, turn)

def read_board(board, wh_turn): # looks for all of the figures on board, counts them stops the game (while loop) if there are no more figures on one side
    flag = True
    c_list = []
    turn_possible = True
    if wh_turn:
        c_set = {'w', 'm'}
    else:
        c_set = {'b', 'p'}
    for y in range(8):
        for x in range(8):
            if board[y][x] in c_set:
                c_list.append([y, x])
    for figure in c_list:
        for y in range(8):
            for x in range(8):
                if board[y][x] == '0':
                    temp = figure + [y, x]
                    if turn_validation(board, temp, wh_turn, [], False)[0]:
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

def main():
    config = get_settings()
    if config.board_colour_ask == 'yes':
        board_colour = choice_of_three('What board type do you want to use?')
    else:
        board_colour = str(config.board_colour)
    if config.Board_creator == 'yes':
        new_board = binary_choice('Do you want to paste your own board?', 1)
    else:
        new_board = False
    if new_board:
        board, White_turn = board_creator(board_colour)
    else:
        board = [['w', '_', 'w', '_', 'w', '_', 'w', '_'],
                 ['_', 'w', '_', 'w', '_', 'w', '_', 'w'],
                 ['w', '_', 'w', '_', 'w', '_', 'w', '_'],
                 ['_', '0', '_', '0', '_', '0', '_', '0'],
                 ['0', '_', '0', '_', '0', '_', '0', '_'],
                 ['_', 'b', '_', 'b', '_', 'b', '_', 'b'],
                 ['b', '_', 'b', '_', 'b', '_', 'b', '_'],
                 ['_', 'b', '_', 'b', '_', 'b', '_', 'b']]
        White_turn = True
    if config.Rus_question == 'yes':
        ru = binary_choice('Do you want to play russian checkers?', 1)
    else:
        if config.Rus == 'yes':
            ru = True
        elif config.Rus == 'no':
            ru = False
    if config.question_test == 'yes':
        pvp = binary_choice('Do you want to play the game yourself?', 1)
    else:
        if config.pvp =='yes':
            pvp = True
        elif config.pvp == 'no':
            pvp = False
    if config.hint == 'yes':
        ch_help(board_colour)
    tries = config.num_of_tries
    print_board(board, pvp, board_colour)
    turn_num = 0
    turn = []
    while read_board(board, White_turn):
        turn_num += 1
        print(f'\nTurn {turn_num}')
        if White_turn:
            print('White turn')
        else:
            print('Black turn')
        board, board_turn, turn_temp = player_turn(board, White_turn, ru, pvp, board_colour, tries, len(turn), turn_num - 1)
        if turn_temp:
            turn[:] = turn[:turn_num - 1]
            turn.append(turn_temp)
        if board_turn == 'surrender':
            if White_turn:
                print('\nBlacks win')
            else:
                print('\nWhites win')
            break
        elif board_turn == 'undo':
            board, turn_num = board_undo(board, turn, turn_num)
            print_board(board, pvp, board_colour)
        elif board_turn == 'redo':
            board, turn_num = board_redo(board, turn, turn_num)
            print_board(board, pvp, board_colour)
        if turn_num % 2 == 1:
            White_turn = False
        else:
            White_turn = True

if __name__ == '__main__':
    main()