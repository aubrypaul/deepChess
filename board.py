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
        
