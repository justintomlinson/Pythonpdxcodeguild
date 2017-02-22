""""This calculates the amount and cost of paint for a wall"""

wdth_wall= int(input('What is the width of the wall in feet? >' ))
print('Width = ' + str(wdth_wall) + ' ft')
hgt_wall = int(input('What is the height of the wall in feet? > '))
print('Height =' + str(hgt_wall) + 'ft')
cost_paint_flt = float(input('How much does a gallon of paint cost? >'))
wall_space = int(hgt_wall) * int(wdth_wall)
print ('Wall is '+str(wall_space)+ 'sqft')

gallons_paint = 0

if wall_space > 0:
    gallons_paint = wall_space/400
    if gallons_paint > int(gallons_paint):
        gallons_paint = int(gallons_paint)+ 1
    print("Gallons of paint required = " + str(gallons_paint))

paint_cost = round(float(gallons_paint)*float(cost_paint_flt), 2)
print('It will cost $'+ str(paint_cost))
