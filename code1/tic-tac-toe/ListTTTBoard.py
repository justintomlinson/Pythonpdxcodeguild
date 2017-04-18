'''This module establishes a tic tac toe game board using lists '''
class ListTTTBoard:
    def __init__(self):
        self._list_board = [['','',''],['','',''],['','','']]



    def place_token(self,x,y,token):
        """

        :param x:
        :param y:
        :param token:
        :return:
        >>> ListTTTBoard().place_token(1,2,'X')
        [['', '', ''], ['', '', 'X'], ['', '', '']]
        """
        wip_board = self._list_board
        wip_board[x][y]= token



        return wip_board

    def calc_win(self, wip_board):
        """

        :param:
        :return:
        >>> ListTTTBoard().calc_win([['X','',''],['','X',''],['','','X']])
        'X'
        >>> ListTTTBoard().calc_win([['O','',''],['','O',''],['','','O']])
        'O'
        >>> ListTTTBoard().calc_win([['X','X','X'],['','O',''],['','X','']])
        'X'
        >>> ListTTTBoard().calc_win([['X','O','X'],['','O',''],['','X','']])
        'Tie'
        """
        winner = None
        diag1 = [wip_board[0][0],wip_board[1][1],wip_board[2][2]]
        diag2 = [wip_board[0][2],wip_board[1][1],wip_board[2][0]]

        for i in range(3):
            if set(wip_board[i])== {'X'}:
                winner = 'X'
            elif set(wip_board[i]) == {'O'}:
                winner = 'O'
            else:
                if set(diag1)== {'X'}or set(diag2)== {'X'}:
                    winner = 'X'
                elif set(diag1)=={'O'} or set(diag2) =={'O'}:
                    winner = 'O'
                else:
                    winner = 'Tie'

        return(winner)


    def __str__(self, wip_board):
        """Prints the game board for tic tac toe

        :param
        :return:
        >>> str(ListTTTBoard())
        "''|''|''
         ''|''|''
         ''|''|''|"
        """
        for i in range(3):
            for j in range(3):
                print(wip_board[i][j], end ='')
                if j != 2:
                 print ("|", end = '')
            print ('')

        #board = [[i for i in range(3)]for j in range(3)]

        return


