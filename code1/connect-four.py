""""Connect Four """

RED = 'r'
YELLOW  = 'y'

#def import_move_file()
with open('connect-four-moves.txt') as input_data:
    move_list = input_data.readlines()

move_2 = []

for index, value in enumerate(move_list):
    move_2.append(value.strip('\n'))
    for x, elem in enumerate(move_2):
     move_2[x].split(' ')

print(move_2)
#   return


#def change_move_list(move_list)
#   append piece color to move list
# yellow goes first
move_update = []

for i, val in enumerate(move_2):
    if i % 2 == 0:
        move_update.append(val +'y')
    else:
        move_update.append(val + 'r')


print (move_update)

#   return





#def build_board(row, col)

#def add_move_to_board
