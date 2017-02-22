orig_dist = float(input("Enter a distance > "))
orig_unit = input("Enter units (mi, km, ft and m) >")
target_unit = input("Enter target units (mi, km, ft, and m) >")
target_dist = 0

miles_km = 1.60934
miles_m = 160934
miles_ft = 5280
km_m = 1000
m_ft = 3.28084
km_ft = m_ft*km_m

if orig_unit == "mi":
    if target_unit == "km":
        target_dist = orig_dist*miles_km
    elif target_unit == "m":
        target_dist = orig_dist*miles_m
    else:
        target_unit == "ft"
        target_dist = orig_dist*miles_ft

if orig_unit == "km":
    if target_unit == "mi":
        target_dist = orig_dist/miles_km
    elif target_unit == "m":
        target_dist = orig_dist*km_m
    else:
        target_unit == "ft"
        target_dist = orig_dist*km_ft

if orig_unit == "m":
    if target_unit == "mi":
        target_dist = orig_dist/miles_m
    elif target_unit == "km":
        target_dist = orig_dist/km_m
    else:
        target_unit == "ft"
        target_dist = orig_dist*(km_ft/km_m)

if orig_unit == "ft":
    if target_unit == "mi":
        target_dist = orig_dist/miles_ft
    elif target_unit == "km":
        target_dist = orig_dist/km_ft
    else:
        target_unit == "m"
        target_dist = orig_dist/m_ft
print(str(orig_dist)+ " "+ str(orig_unit)+ " is " +  str(target_dist)+" " + str(target_unit))

