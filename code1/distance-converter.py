"""This program converts between a set unit of distance"""

def convert_to_meters (orig_dist,orig_unit):
    miles_m = orig_dist*1609.34
    km_m = orig_dist*1000
    ft_m = orig_dist*3.28084
    in_m = orig_dist*0.254
    cm_m = orig_dist/100

    if orig_unit == "ft":
        meter_dist = ft_m
    elif orig_unit == "mi":
        meter_dist = miles_m
    elif orig_unit == "km":
        meter_dist = km_m
    elif orig_unit == "in":
        meter_dist = in_m
    elif orig_unit == "cm":
        meter_dist = cm_m
    else:
        meter_dist = orig_dist
    return meter_dist

def convert_from_meter(target_unit, meter_dist):

    m_miles = meter_dist/1609.34
    m_km = meter_dist/1000
    m_ft = 3.28084/meter_dist
    m_in = meter_dist/0.254
    m_cm = meter_dist*100
    convert_dist = 0
    if target_unit == "mi":
        convert_dist = m_miles
    elif target_unit == "km":
        convert_dist = m_km
    elif target_unit == "ft":
        convert_dist = m_ft
    elif target_unit == "in":
        convert_dist = m_in
    elif target_unit == "cm":
        convert_dist = m_cm
    else:
        convert_dist = meter_dist
    return (convert_dist)

def main ():
    orig_dist = float(input("Enter a distance > "))
    orig_unit = input("Enter units (mi, km, ft, in, cm and m) >")
    target_unit = input("Enter target units (mi, km, ft, in, cm and m) >")

    meter_dist = convert_to_meters(orig_dist, orig_unit)
    convert_dist = convert_from_meter(target_unit,meter_dist)
    print(str(orig_dist)+ str(orig_unit) + " is " + str(convert_dist)+ str(target_unit))
   # print ("%g %s is %g %s" %(orig_dist, orig_unit, convert_dist, target_unit))
if __name__ == '__main__':
    main()
