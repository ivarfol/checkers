#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 15:07:30 2024

@author: iaroslav
"""
# 0123456700_0_0_0_1_0_0_0_020_0_0_0_3_0_0_0_040_0_£_0_5_b_0_0_060_0_0_0_7_0_0_0_0
#board = '0123456700_0_0_0_1_0_0_0_020_0_0_0_3_0_0_0_040_0_£_0_5_b_0_0_060_0_0_0_7_0_0_0_0'
# 0123456700_0_0_0_1_0_0_0_020_0_0_0_3_0_0_0_040_0_0_0_5_b_0_0_060_£_0_0_7_0_0_0_0
# 0123456700_0_0_0_1_0_0_0_020_0_0_0_3_w_0_0_040_b_b_b_5_b_0_0_06b_b_b_b_7_b_0_0_b
#jump
#  a b c d e f g h1 w _ w _ w _ w _ 12 _ w _ w _ w _ w 23 w _ w _ w _ w _ 34 _ 0 _ 0 _ 0 _ 0 45 0 _ 0 _ 0 _ 0 _ 56 _ b _ b _ b _ b 67 b _ b _ b _ b _ 78 _ b _ b _ b _ b 8  a b c d e f g h
# 1 w _ w _ w _ w _ 1
def main():
    l_board = []
    l_temp = []
    pvp = valRuPvP('Were you playing PvP?')
    board = input()
    if pvp:
        board = board[17:165]
        board = board.split(' ')
        for i in range(0,64,8):
            l_temp = board[i + int(i / 8):i + int(i / 8) + 8]
            l_board.append(l_temp)
    else:
        board = board[9:]
        for i in range(0,64,8):
            temp = board[i + int(i / 8):i + int(i / 8) + 8]
            l_temp.extend(temp)
            l_board.append(l_temp)
            l_temp = []
    print_board(l_board, pvp)
    print(l_board)

def valRuPvP(messenge):
    RuPvP = input(f'{messenge}\ny/n\n')
    while not RuPvP in ('y', 'n'):
        RuPvP = input(f'{messenge}\ny/n\n')
    if RuPvP == 'y':
        return(True)
    else:
        return(False)

def print_board(board, PvP):  # prints the playing board with coordinats on top and left
    if PvP:
        print('\n  a b c d e f g h')
        for j in range(8):
            print('12345678'[j] + ' ' + ' '.join(board[j]) + ' ' + '12345678'[j])
        print('  a b c d e f g h')
    else:
        print('\n 01234567')
        for i in range(8):
            print('01234567'[i] + ''.join(board[i]))
        
if __name__ == '__main__':
    main()