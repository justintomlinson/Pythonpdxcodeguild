class DictTTTBoard:
    def __init__(self):
        self._dict_board = {'00' : ' ', '01': ' ', '02': ' ','10': ' ', '11': ' ', '12': ' ','20': ' ', '21': ' ', '22': ' '}



    def place_token(self,x,y,token):
        """

        :param x:
        :param y:
        :param token:
        :return:
        >>> DictTTTBoard().place_token(1,2,'X')
        {'00': ' ', '01': ' ', '02': ' ','10': ' ', '11': ' ', '12': 'X', '20': ' ', '21': ' ', '22': ' '}
        """
        token_in = token
        wip_board =self._dict_board
        key = str(x)+str(y)
        wip_board={key: token_in}

        return wip_board

    def calc_winner(self, wip_board):
        """

        :param wip_board:
        :return:
        >>> DictTTTBoard().calc_winner({'00' : 'X', '01': 'X', '02': 'X','10': ' ', '11': ' ', '12': ' ','20': ' ', '21': ' ', '22': ' '})
        'X'
        >>> DictTTTBoard().calc_winner({'00' : 'X', '01': 'O', '02': 'X','10': 'X', '11': ' ', '12': ' ','20': 'X', '21': ' ', '22': ' '})
        'X'
        >>> DictTTTBoard().calc_winner({'00' : 'X', '01': 'O', '02': 'X','10': 'X', '11': ' ', '12': ' ','20': 'X', '21': ' ', '22': ' '})
        'X'
        >>> DictTTTBoard().calc_winner({'00' : 'O', '01': 'O', '02': 'O','10': 'X', '11': ' ', '12': ' ','20': 'X', '21': ' ', '22': ' '})
        'O'
        >>> DictTTTBoard().calc_winner({'00' : 'X', '01': 'O', '02': 'X','10': 'O', '11': 'X', '12': 'X','20': 'O', '21': 'X', '22': 'O'})
        'Tie'
        """
        value = list(wip_board.values())

        row_z = [value[0], value[1],value[2]]
        row_one = [value[3], value[4], value[5]]
        row_two = [value[6], value[7], value[8]]
        diag1 = [value[0], value[4], value[8]]
        diag2 = [value[6], value[4], value[2]]
        col_z = [value[0], value[3], value[6]]
        col_one = [value[1], value[4], value[7]]
        col_two = [value[2], value[5], value[8]]

        winning = [row_z, row_one, row_two, col_one, col_z,col_two, diag2, diag1]

        for i in winning:
            if set(i) == {'X'}:
                winner = 'X'
            elif set(i) == {'O'}:
                winner = 'O'
            else:
                winner = 'Tie'

            return(winner)

    def __str__(self):
        """

        :return:
        >>> str(DictTTTBoard())
        "''|''|''
         ''|''|''
         ''|''|''|"
        """
        board = []
        values = list(self._dict_board.values())

        board = ([print(x +'|')for x in values])


        return board