from texttable import Texttable
import unittest
from unittest import TestCase

class Board:
    def __init__(self):
        self.data = [[" "," "," "],[" "," "," "],[" "," "," "]]

    def readFromFile(self, fname):

        with open(fname, 'r') as f:
            lines = f.readlines()
            i = 0
            for line in lines:
                for j in range(3):
                    if line[j] == "+":
                        self.data[i][j] = " "
                    elif line[j] == "X":
                        self.data[i][j] = "X"
                    elif line[j] == "O":
                        self.data[i][j] = "O"
                i += 1

    def writeToFile(self,fname):

        with open(fname, "w") as f:
            for line in self.data:
                for item in line:
                    if item == " ":
                        f.write("+")
                    else:
                        f.write(item)
                f.write("\n")

    def __str__(self):
        self.table = Texttable()
        self.table.add_rows(self.data,[])
        return self.table.draw()

    def move(self,x,y, piece):
        """
        :param x: integer
        :param y: integer
        :param piece: char x or o
        :return: true if the move is possible, false otherwise
        """
        if 0<= x <=2 and 0<= y <= 2:
            if self.data[x][y] == " ":
                self.data[x][y] = piece
                return True
            else:
                return False
        else:
            return False

    def iswon(self, piece):
        """
        :param piece: char o or x
        :return: true if the game is won by that piece, false otherwise
        """
        for i in range(3):
            if(self.data[i][0] == piece and self.data[i][1] == piece and self.data[i][2] == piece):
                return True
            if(self.data[0][i] == piece and self.data[1][i] == piece and self.data[2][i] == piece):
                return True
        if(self.data[0][0] == piece and self.data[1][1] == piece and self.data[2][2] == piece):
            return True
        if (self.data[0][2] == piece and self.data[1][1] == piece and self.data[2][0] == piece):
            return True

        return False

    def placementfinished(self):
        """
        :return: true if the placement has finished
        """
        s = 0
        for i in range(3):
            for j in range(3):
                if self.data[i][j] != " ":
                    s += 1
                    if s == 8:
                        return True
        return False

    def movemovement(self, x, y, piece):
        """
        :param piece: char o or x
        :return: true if the move is valid
        """
        # if 0<= x <=2 and 0<= y <= 2:
        #     if self.data[x][y] == piece:
        #         if i - 1 >= 0 and j - 1 >= 0:
        #             if board.data[i - 1][j - 1] == " ":
        #                 board.move(i, j, self.piece)
        #                 board.move(i - 1, j - 1, " ")
        #                 return True
        #         if i - 1 >= 0 and j + 1 <= 2:
        #             if board.data[i - 1][j + 1] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i - 1, j + 1, " ")
        #                 return True
        #         if i + 1 <= 2 and j - 1 >= 0:
        #             if board.data[i + 1][j - 1] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i + 1, j - 1, " ")
        #                 return True
        #         if i + 1 <= 2 and j + 1 <= 2:
        #             if board.data[i + 1][j + 1] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i + 1, j + 1, " ")
        #                 return True
        #         if j + 1 <= 2:
        #             if board.data[i][j + 1] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i, j + 1, " ")
        #                 return True
        #
        #         if i + 1 <= 2:
        #             if board.data[i + 1][j] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i + 1, j, " ")
        #                 return True
        #
        #         if i - 1 >= 0:
        #             if board.data[i - 1][j] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i - 1, j, " ")
        #                 return True
        #
        #         if j - 1 >= 0:
        #             if board.data[i][j - 1] == self.piece:
        #                 board.move(i, j, self.piece)
        #                 board.move(i, j - 1, " ")
        #                 return True


        return False


class Player:

    def __init__(self, piece):
        self.piece = piece

    def getPiece(self):
        return self.piece

class AI:
    def __init__(self, piece):
        self.piece = piece

    def getPiece(self):
        return self.piece

    def checkforconnections(self, board, piece):
        """
        :param board: a state of the board
        :param piece: char o or x
        :return: true if there are any connections of 2 pieces positioned adjacently
        """
        for i in range(3):
            if board.data[i][0] == board.data[i][1] == piece and board.data[i][2] == " ":
                return i,2
            if board.data[i][2] == board.data[i][1] == piece and board.data[i][0] == " ":
                return i,0
            if board.data[0][i] == board.data[1][i] == piece and board.data[2][i] == " ":
                return 2,i
            if board.data[2][i] == board.data[1][i] == piece and board.data[0][i] == " ":
                return 0,i

        if board.data[0][0] == board.data[1][1] == piece and board.data[2][2] == " ":
            return 2,2
        if board.data[2][2] == board.data[1][1] == piece and board.data[0][0] == " ":
            return 0,0
        if board.data[0][2] == board.data[1][1] == piece and board.data[2][0] == " ":
            return 2,0
        if board.data[2][0] == board.data[1][1] == piece and board.data[0][2] == " ":
            return 0,2

        return False

    def move(self, board):
        """
        :param board: state of the board
        :return: a move on the table
        """
        if self.checkforconnections(board, "X") == False:
            for i in range(3):
                for j in range(3):
                    if(board.data[i][j] == " "):
                        board.move(i, j, self.piece)
                        return True
        else:
            i = self.checkforconnections(board, "X")[0]
            j = self.checkforconnections(board, "X")[1]
            board.move(i, j, self.piece)
            return True

    def movemovement(self, board):
        """
        :param board: a state of the board
        :return: a move when the movement phase began
        """
        for i in range(3):
            for j in range(3):
                if(board.data[i][j] == " "):
                    if i-1 >= 0 and j-1 >= 0:
                        if board.data[i-1][j-1] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i-1, j-1, " ")
                            return True
                    if i-1 >= 0 and j+1 <= 2:
                        if board.data[i-1][j+1] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i-1, j+1, " ")
                            return True
                    if i+1 <= 2 and j-1 >= 0:
                        if board.data[i+1][j-1] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i+1, j-1, " ")
                            return True
                    if i+1 <= 2 and j+1 <= 2:
                        if board.data[i+1][j+1] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i+1, j+1, " ")
                            return True
                    if j+1 <= 2:
                        if board.data[i][j+1] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i, j+1, " ")
                            return True

                    if i+1 <= 2:
                        if board.data[i+1][j] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i+1, j, " ")
                            return True

                    if i-1 >= 0:
                        if board.data[i-1][j] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i-1, j, " ")
                            return True

                    if j-1 >= 0:
                        if board.data[i][j-1] == self.piece:
                            board.move(i , j, self.piece)
                            board.move(i, j-1, " ")
                            return True


class Tests(TestCase):
    def testboard(self):
        b = Board()
        assert b.move(1, 2, "X") == True
        assert b.move(3, 3, "X") == False
        assert b.iswon("O") == False
        print(b)
        b.move(1, 1, "X")
        b.move(1, 0, "X")
        assert b.move(1, 0, "X") == False
        assert b.iswon("X") == True
        assert b.placementfinished() == False

    def testAI(self):
        b = Board()
        b.move(1, 2, "X")
        b.move(1, 1, "X")
        b.move(1, 0, "X")
        ai = AI("O")
        assert ai.move(b) == True
        assert ai.checkforconnections(b,"O") == False
        assert ai.checkforconnections(b,"X") != False
        assert ai.checkforconnections(b, "X") == (1,2)


if __name__ == '__main__':
    unittest.main()