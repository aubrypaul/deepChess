from sympy import re
from pieces import *

def check_promotion(piece,y):
    """
    Check if a pawn if eligible for promotion on it's next move
    """
    if piece.color == "w":
        row = 1
        incr = -1
    elif piece.color == "b":
        row = 6
        incr = 1
    if type(piece) == Pawn and piece.y == row and y == piece.y + incr:
        return True
    else:
        return False

class Board:
    """
    Board is represented by an 8x8 array. "None" is an empty case
    """
    def __init__(self):
        self.empty = [[None for x in range(8)] for y in range(8)]
        self.black_king = King("b",0,4)
        self.white_king = King("w",7,4)
        self.white_rook_left = Rook("w", 7, 0)
        self.white_rook_right =  Rook("w", 7, 7)
        self.black_rook_left = Rook("b", 0, 0)
        self.black_rook_right = Rook("b", 0, 7)
        self.array = [
            [self.black_rook_left, Knight("b", 0, 1), Bishop("b", 0, 2), Queen("b", 0, 3),
                self.black_king, Bishop("b", 0, 5), Knight("b", 0, 6), self.black_rook_right],
            [Pawn("b", 1, i) for i in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [None for x in range(8)],
            [Pawn("w", 6, i) for i in range(8)],
            [self.white_rook_left, Knight("w", 7, 1), Bishop("w", 7, 2), Queen("w", 7, 3),
                self.white_king, Bishop("w", 7, 5), Knight("w", 7, 6), self.white_rook_right]
        ]
        self.score = 0
        self.pvalue_dict = {King:200, Queen:10, Rook:5, Bishop:3, Pawn:1}

    def special_move(self,piece,y,x,special):
        '''
        Allows castling to be perfomed; it requires the movement of two pieces.
        '''
        color = piece.color 

        if special[0] == "C":
            self.move_piece(piece,y,x)
            piece.moved = True
            if special[1] == "L" and color == "w":
                rook = self.white_rook_left
                i = 3
                j = 7
            elif special[1] == "R" and color == "w":
                i = 5
                j = 7
                rook = self.white_rook_right
            elif special[1] == "L" and color == "b":
                i = 3
                j = 0
                rook = self.black_rook_left
            elif special[1] == "R" and color == "b":
                i = 5
                j = 0
                rook = self.black_rook_right
            rook.moved = True
            self.move_piece(rook,j,i)

    
    def move_piece(self,piece,y,x,special=False,np=False):
        """
        Moves an instance of the piece class to (y,x).
        Special indiates a special move should be handled separately
        np indicates that pawn promotion should not be performed.
        (np = no promotion)
        """
        if not special:
            promotion = check_promotion(piece,y)
            oldX = piece.x
            oldY = piece.y
            piece.x = x
            piece.y = y
            piece.rect.x = x * 60
            piece.rect.y = y * 60
            self.array[oldY][oldX] = None

            if promotion and not np:
                self.array[y][x] = Queen(piece.color,y,x)
                if piece.color == "w":
                    self.score -= 9
                elif piece.color == "b":
                    self.score += 9
                return self.array[y][x], piece
            else:
                self.array[y][x] = piece
                piece.unhighlight()
        else:
            self.special_move(piece,y,x,special)