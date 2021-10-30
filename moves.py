"""
    File: moves.py
    Author: Xin Li
    Purpose: Intended for use in the Cracker Barrel puzzle problem.
        The function all_moves(n) returns a set of all legal moves for a
        board with n rows.
"""


def all_moves(n):
    """ all_moves(n) computes all possible moves for a board consisting
        of n rows of pins.
    """
    directions = [(0,-1), (0,1), (1,0), (-1,0), (-1,-1), (1,1)]
    posns = triangle2(n)

    mvs = set()
    for i in range(len(posns)):
        for j in range(i+1):
            for delta_xy in directions:
                (i_mid,j_mid) = newpos((i,j), delta_xy)
                (i_dst,j_dst) = newpos((i_mid, j_mid), delta_xy)
                if legal_pos(i_mid, j_mid, posns) and legal_pos(i_dst, j_dst, posns):
                    move = (posns[i][j], posns[i_mid][j_mid], posns[i_dst][j_dst])
                    mvs.add(move)

    return mvs


def mk_row(n, k):
    if n == 1:
        return [k]
    else:
        return [k] + mk_row(n-1, k+1)

def triangle2(n):
    if n == 0:
        return []
    elif n == 1:
        return [[0]]
    else:
        rest = triangle2(n-1)
        row = mk_row(n, rest[-1][-1]+1)
        return rest + [row]


def newpos(old_pos, chg):
    (x,y) = old_pos
    (delta_x,delta_y) = chg
    return (x+delta_x, y+delta_y)


def legal_pos(x,y,posns):
    return (x >= 0 and y >= 0 and x < len(posns) and y < len(posns[x]))


if __name__ == "__main__":
    print(all_moves(5))
