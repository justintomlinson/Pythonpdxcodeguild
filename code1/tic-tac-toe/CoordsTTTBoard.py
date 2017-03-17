class CoordsTTTBoard:
    def __init__(self):
        self._coords_board=[]

    def place_token(self,x,y,token):
        """

        :param x:
        :param y:
        :param token:
        :return:
        >>> CoordsTTTBoard().place_token(1,2,'X')
        [(1, 2, 'X')]
        """

        input= (x, y, token)
        wip_board = self._coords_board
        wip_board.append(input)

        return wip_board

    def calc_winner(self):

        return


    def __str__(self, wip_board):
        """

        :param wip_board:
        :return:
        >>> str(CoordsTTTBoard())
        "''|''|''
         ''|''|''
         ''|''|''|"
        """
        print(wip_board[2]+"|"+ wip_board[5]+"|" + wip_board[8])
        print(wip_board[11]+"|"+ wip_board[14]+"|" + wip_board[17])
        print(wip_board[20]+"|"+ wip_board[23]+"|" + wip_board[26])

