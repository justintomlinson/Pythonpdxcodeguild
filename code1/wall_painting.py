wdth_wall= int(input('What is the width of the wall in feet? >' ))
print('Width = ' + str(wdth_wall) + ' ft')
hgt_wall = int(input('What is the height of the wall in feet? > '))
print('Height =' + str(hgt_wall) + 'ft')
cost_paint_flt = float(input('How much does a gallon of paint cost? >'))
wall_space = int(hgt_wall) * int(wdth_wall)
print ('Wall is '+str(wall_space)+ 'sqft')


if wall_space > 400:
    gallons_paint = wall_space/400
    print("Gallons of paint required = " + str(gallons_paint))

paint_cost = round(float(gallons_paint*cost_paint_flt), 2)
print('It will cost $'+ str(paint_cost))
