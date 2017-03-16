
class ListTTTBoard:
    def __init__(self):
        self._list_board = [[0,0,0],[0,0,0],[0,0,0]]



    def place_token(self,x,y,token):
        """

        :param x:
        :param y:
        :param token:
        :return:
        >>> ListTTTBoard().place_token(1,2,'X')
        [[0, 0, 0], [0, 0, 'X'], [0, 0, 0]]
        """
        wip_board = self._list_board
        wip_board[x][y]= token



        return wip_board
    def calc_win(self,wip_board):
        """

        :param wip_board:
        :return:


        """


        #for i in range(3):
       #      if wip_board[0][i] == wip_board[1][i] == wip_board[2][i]:



    def __str__(self):
        """Prints the game board for tic tac toe

        :param wip_board:
        :return:
        >>> str(ListTTTBoard())
        "0|0|0|
         0|0|0|
         0|0|0|"
        """
        #
        for i in range(3):
            for j in range(3):
                board = print((str(self._list_board[i])[j]+'|'))


        return str(board)


