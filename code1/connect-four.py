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


#def change_move_list(move_2)
#   append piece color to move list
# yellow goes first
move_update = []
y = ['y']
r = ['r']
for i, val in enumerate(move_2):
    if i % 2 == 0:
        move_update.append(val + y )
    else:
        move_update.append(val + r)

print (move_update)

#   return

#def build_board(row, col)

rows = 6
col = 7

game_board = [[]*col for i in range(rows)]
print(game_board)
print(len(game_board))
#   return()

#def add_move_to_board(game_board, move_update)

game_play =[]
for index, list in enumerate(range(len(game_board)- 1,0,-1)):
    for col, color in enumerate(move_update):
        game_board.insert[:color]

print(game_board)





