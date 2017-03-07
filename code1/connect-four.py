""""Connect Four """

RED = 'r'
YELLOW  = 'y'

#def import_move_file()
with open('connect-four-moves.txt') as input_data:
    move_list = input_data.readlines()

move_2 = []

for index, value in enumerate(move_list):
    move_2.append(value.strip('\n').split())
    for x, elem in enumerate(move_2):
     ','.join(elem)

#print(move_2)
#   return


#def add_color_to_move_list(move_2):
#     """Appends red and yellow to the list of moves. Yellow goes first in this scenario
#
#     :param move_2:
#     :return:
#     """
# move_update = []
# y = ['y']
# r = ['r']
# for i, val in enumerate(move_2):
#     if i % 2 == 0:
#         move_update.append(val + y )
#     else:
#         move_update.append(val + r)
#
#   return(move_update)

#def build_board(row_num, col_num):
    # """ Creates an empty list of list to represent an empty board game
    #
    # :param row_num:
    # :param col_num:
    # :return:
    # """

row_num = 6
col_num = 7

game_board = [[] * col_num for i in range(row_num)]

#   return()

#def add_move_to_board(game_board, move_update):
    # """ Appends piece color to game board based on position from the moves list
    #
    # :param game_board:
    # :param move_update:
    # :returvern:
    # """
for col in reversed(range(col_num)):
    for position in move_2:
        game_board.append[position]
        if len(game_board[col]) < row_num:
            col= col-1

#        if (check_if_row_full(game_board, col_num, row_num)):
#        if len(game_board[col])<= row_num:
#            game_board[row].append(color[1])
print(game_board)

#print(game_board)

# def check_if_row_full(game_board, row_num, col_num):
#
#     if len(game_board[col_num])> row_num:
#         return True
#     else:
#         return False






