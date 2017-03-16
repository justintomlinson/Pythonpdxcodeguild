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
        wip_board =self._dict_board
        xy = str(x)+str(y)
        self._dict_board[xy] = token

        return self._dict_board
    def calc_winner(self):
        value_list = list(self._dict_board.values)

        for i in value_list
            if i

        return
    def __str__(self):
        return