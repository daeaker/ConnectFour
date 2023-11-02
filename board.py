class Board:
    def __init__(self, rows=6, cols=7):
        self.rows = rows
        self.cols = cols
        # True for Player 1, False for Player 2
        self.turn = True
        # 0 for empty, 1 for Player 1, 2 for Player 2
        self.board = [[ 0 for _ in range(cols)] for _ in range(rows)]
        

    """
    dropPiece
    INPUTS:
        column: the column the piece will be dropped into
        piece: the piece being dropped (1 or 2)

    OUTPUTS:
        returns nothing
        updates the board matrix and turn tracker
    """
    def dropPiece(self, column, piece):
        raise NotImplementedError()
    

    """
    undoLastMove
    INPUTS:
        column: the column a piece was last dropped into

    OUTPUTS:
        returns nothing
        removes the top piece from the input column
        updates the turn tracker
    
    """
    def undoLastMove(self, column):
        raise NotImplementedError()
    

    """
    getValidColumns
    INPUTS:
        none
    OUTPUTS
        returns a list of columns with at least 1 empty space
    
    """
    def getValidColumns(self):
        raise NotImplementedError()
    

    """
    isBoardFull
    INPUTS: 
        none
    OUTPUTS:
        returns True if board is full, else False
    """
    def isBoardFull(self):
        raise NotImplementedError()
    
    """
    checkForWin
    INPUTS:
        none
    OUTPUTS:
        returns 1 if Player1 has won
        returns 2 if Player2 has won
        else return 0
    """
    def checkForWin(self):
        raise NotImplementedError()



    """
    print
    INPUTS:
        none
    OUTPUTS:
        prints the board matrix to the terminal
    """
    def print(self):
        raise NotImplementedError()
