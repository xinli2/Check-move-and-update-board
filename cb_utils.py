""" File: cb_utils.py
    Author: Xin Li
    Purpose: calculates all moves, all legal moves,
        checks a legal move and updates the board
"""
from moves import *

def legal_move(board,mov):
    """
    This function tells if a given move is legal or not
    board - list of strings
    mov - tuple of integers
    return - True/Fase
    """
    # mov[0] is the starting position of move mov[1]
    # is the peg removed and mov[2] is the final position
    if(board[mov[0]]=='1' and board[mov[1]]=='1' and board[mov[2]]=='0'):
        return True
    else:
        return False

def legal_move_interface(board_str,mov):
    """
    This function converts the string of board
    into a array and calls the above function
    board - string
    mov - tuple of integers
    return - True/Fase
    """
    board=[]
    for x in range(0,len(board_str)):
        board.append(board_str[x])
    return legal_move(board,mov)

def all_legal_moves(size,board):
    """
    This function for a given board returns the legal moves array
    board - list of strings
    size - integer
    return - set of tuples
    """
    legal=set()
    # uses all_move to calculate all moves
    all_move=all_moves(size)
    for x in all_move:
        # calls legal move to check if move is legal if it
        # is legal it appends to the array
        if(legal_move(board,x)):
            legal.add(x)
    return legal

def all_legal_moves_interface(size, board_str):
    """
    This function converts string to list and does same as above
    board_str - string
    size - integer
    return - set of tuples
    """
    board=[]
    for x in range(0,len(board_str)):
        board.append(board_str[x])
    return all_legal_moves(size,board)

def update_board(board,mov):
    """
    This function simply plays a given move on the board
    board - list of strings
    mov - tuple of integers
    return - string
    """
    board[mov[0]]="0"
    board[mov[1]]="0"
    board[mov[2]]="1"
    return board

def update_board_interface(board_str,mov):
    """
    This function converts the string into a board
    then calls above function and returns a string
    board_str - string
    mov - tuple of integers
    return - string
    """
    board=[]
    for x in range(0,len(board_str)):
        board.append(board_str[x])
    list=update_board(board,mov)
    string = ""
    for x in list:
        string+=x
    return string
