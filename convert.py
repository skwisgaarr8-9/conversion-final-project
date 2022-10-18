

def temperature(n, s, t):
    '''
    Temperature converts n from one temperature unit s to another temperature unit t.
    Returns a float, rounded to a certain number of decimal points when necessary.
    Available units are celsius(c), fahrenheit(f), and kelvin(k).

        Parameters:
            n (int / float): Any integer or float, positive or negative.
            s (str): A string which corresponds to one of the available units.
            T (str): Another string which corresponds to one of the available units.

        Returns:
            rounded float
    '''

    if s == "c" and t == "f":
        return round(n * (9 / 5) + 32)

    if s == "f" and t == "c":
        return round((n - 32) * (5 / 9))

    if s == "c" and t == "k":
        return round(n + 273.15)

    if s == "k" and t == "c":
        return round(n - 273.15)

    if s == "f" and t == "k":
        return round(temperature(n, "f", "c") + 273.15)

    if s =="k" and t == "f":
        return round((n - 273.15) * (9 /5) + 32)

    return f"Usage: temperature requires 3 arguments in the form of 'degrees, unit, unit'. Available units are 'f, c, k'."

def weight(n, s, t):
    '''
    Weight converts n from one unit of weight s to another t
    Returns a float, rounded to a certain number of decimal points when necessary.
    Available units are pound(lb), kilogram(kg), gram(g), miligram(mg), ounce(oz), and stone(st).

            Parameters:
                n (int / float): Any integer or float, positive or negative.
                s (str): A string which corresponds to one of the available units.
                T (str): Another string which corresponds to one of the available units.

            Returns:
                rounded float, to a certain number of decimal points
    '''

    if not n > 0:
        return f"Usage: weight must not be negative"
    if s == t:
        return n

    #converting pounds to other units
    if s =="lb" and t == "kg":
        return round(n / 2.2046, 2)

    if s == "lb" and t == "oz":
        return round(n * 16, 2)

    if s == "lb" and t =="g":
        return round(n * 453.59237, 2)

    if s == "lb" and t == "mg":
        return round(n * 453592.37, 2)

    if s == "lb" and t == "st":
        return round(n * 0.071429, 2)

    #converting kilograms to other units
    if s == "kg" and t == "lb":
        return round(n * 2.2046, 2)

    if s == "kg" and t == "oz":
        return round(n * 35.274, 2)

    if s == "kg" and t == "g":
        return round(n * 1000, 2)

    if s == "kg" and t == "mg":
        return round(n * 1000000, 2)

    if s == "kg" and t == "st":
        return round(n * 0.1574, 2)

    #converting ounces to other units
    if s == "oz" and t == "lb":
        return round(n / 16, 2)

    if s == "oz" and t == "kg":
        return round(n * 0.02834952, 2)

    if s == "oz" and t == "g":
        return round(n * 28.34952, 2)

    if s == "oz" and t == "mg":
        return round(n * 28349.52, 2)

    if s == "oz" and t == "st":
        return round(n * 0.0044643, 2)

    #converting grams to other units
    if s == "g" and t == "lb":
        return weight(n, "kg", "lb") / 1000

    if s == "g" and t == "kg":
        return n / 1000

    if s == "g" and t == "mg":
        return n * 1000

    if s == "g" and t == "oz":
        return round(weight(n, "kg", "oz") / 1000, 2)

    if s == "g" and t == "st":
        return weight(n, "kg", "st") / 1000

    #converting miligrams to other units
    if s == "mg" and t == "lb":
        return weight(n, "g", "lb") / 1000

    if s == "mg" and t == "kg":
        return n / 1000000

    if s == "mg" and t == "g":
        return n / 1000

    if s == "mg" and t == "oz":
        return weight(n, "g", "oz") / 1000

    if s == "mg" and t == "st":
        return weight(n, "g", "st") / 1000

    #converting stone to other units
    if s == "st" and t == "lb":
        return n * 14

    if s == "st" and t == "kg":
        return round(n / 0.15747, 2)

    if s == "st" and t == "g":
        return weight(n, "st", "kg") * 1000

    if s == "st" and t == "mg":
        return weight(n, "st", "g") * 1000

    if s == "st" and t == "oz":
        return weight(n, "st", "lb") * 16



    return f"Usage: weight requires 3 arguments in the form of 'weight, unit, unit'. Available units are 'lb, kg, g, mg, oz, st'"


def volume(n, s, t):
    '''
    Volume converts n liquid volume from one unit s to another unit t.
    All non metric units are according to USA customary measuring standards.
    Available units are: gallon (gal), quart (qt), pint (pt), cup (cup), fluid ounce (floz)
    liter (l), and milliliter (ml).
    Returns a float, rounded to a certain number of decimal points when necessary.

            Parameters:
                n (int / float): Any integer or float, positive or negative.
                s (str): A string which corresponds to one of the available units.
                T (str): Another string which corresponds to one of the available units.

            Returns:
                rounded float, to a certain number of decimal points
    '''

    #converts gallons to other units
    if s == "gal" and t == "qt":
        return n * 4.0

    if s == "gal" and t == "pt":
        return n * 8.0

    if s == "gal" and t == "cup":
        return n * 16.0

    if s == "gal" and t == "floz":
        return n *128.0

    if s == "gal" and t == "l":
        return round(n * 3.785411784, 3)

    if s == "gal" and t == "ml":
        return round(n * 3785.411784, 3)

    if s == "gal" and t == "gal":
        return n

    #converts quarts to other units
    if s == "qt" and t == "gal":
        return n / 4

    if s == "qt" and t == "pt":
        return n * 2.0

    if s == "qt" and t == "cup":
        return n * 4.0

    if s == "qt" and t == "floz":
        return n * 32.0

    if s == "qt" and t == "l":
        return round(n / 1.057, 3)

    if s == "qt" and t == "ml":
        return n * 946.4

    if s == "qt" and t == "qt":
        return n

    #converts pints to other units
    if s == "pt" and t == "gal":
        return n / 8

    if s == "pt" and t == "qt":
        return n / 2

    if s == "pt" and t == "cup":
        return n * 2.0

    if s == "pt" and t == "floz":
        return n * 16.0

    if s == "pt" and t == "l":
        return round(n / 2.113, 3)

    if s == "pt" and t == "ml":
        return n * 473.2

    if s == "pt" and t == "pt":
        return n

    #convert cups to other units
    if s == "cup" and t == "gal":
        return n / 16

    if s == "cup" and t == "qt":
        return n / 4

    if s == "cup" and t == "pt":
        return n / 2

    if s == "cup" and t == "floz":
        return n * 8.0

    if s == "cup" and t == "l":
        return round(n / 4.227, 3)

    if s == "cup" and t == "ml":
        return n * 236.6

    if s == "cup" and t == "cup":
        return n

    #convert fluid ounces to other units
    if s == "floz" and t == "gal":
        return n /128

    if s == "floz" and t == "qt":
        return n / 32

    if s == "floz" and t == "pt":
        return n / 16

    if s == "floz" and t == "cup":
        return n / 8

    if s == "floz" and t == "l":
        return round(n / 33.814, 3)

    if s == "floz" and t == "ml":
        return n * 29.574

    if s == "floz" and t == "floz":
        return n

    #convert liters to other units
    if s == "l" and t == "gal":
        return round(n / 3.785411784, 3)

    if s == "l" and t == "qt":
        return n * 1.057

    if s == "l" and t == "pt":
        return n * 2.113

    if s == "l" and t == "cup":
        return n * 4.227

    if s == "l" and t == "floz":
        return n * 33.814

    if s == "l" and t == "ml":
        return n * 1000.0

    if s == "l" and t == "l":
        return n

    #conver milliliters to other units
    if s == "ml" and t == "gal":
        return round(n / 3785.411784, 5)

    if s == "ml" and t == "qt":
        return round(n / 946.4, 3)

    if s == "ml" and t == "pt":
        return round(n / 473.2, 3)

    if s == "ml" and t == "cup":
        return round(n / 236.6, 3)

    if s == "ml" and t == "floz":
        return round(n / 29.574, 3)

    if s == "ml" and t == "l":
        return n / 1000

    if s == "ml" and t == "ml":
        return n

    return f"Usage: volume requires three arguments in the form of 'volume, unit, unit'. Available units include: gal, qt, pt, cup, floz, l, ml."

def length(n, s, t):
    '''
    Length converts n from unit s to unit t.
    Available units include inches(in), feet(ft), yards(yd), miles(mi), centimeters(cm), meters(m), and kilometers(km).
    Returns a float, rounded to a certain number of decimal points when necessary.

            Parameters:
                n (int / float): Any integer or float, positive or negative.
                s (str): A string which corresponds to one of the available units.
                T (str): Another string which corresponds to one of the available units.

            Returns:
                rounded float, to a certain number of decimal points

    '''

    #converts inches to other units
    if s == "in" and t == "ft":
        return round(n / 12, 3)

    if s == "in" and t == "yd":
        return round(n / 36, 3)

    if s == "in" and t == "mi":
        return round(n / 63360, 5)

    if s == "in" and t == "cm":
        return round(n / .39370, 3)

    if s == "in" and t == "m":
        return round(n / 39.37, 3)

    if s == "in" and t == "km":
        return round(n / 39370, 5)

    if s == "in" and t == "in":
        return n

    #converts feet to other units
    if s == "ft" and t == "in":
        return n * 12.0

    if s == "ft" and t == "yd":
        return round(n / 3, 3)

    if s == "ft" and t == "mi":
        return round(n / 5280, 4)

    if s == "ft" and t == "cm":
        return n * 30.48

    if s == "ft" and t == "m":
        return round(n/ 3.2808, 3)

    if s == "ft" and t == "km":
        return round(n / 3280.8, 4)

    if s == "ft" and t == "ft":
        return n

    #converts yards to other units
    if s == "yd" and t == "in":
        return n * 36.0

    if s == "yd" and t == "ft":
        return n * 3.0

    if s == "yd" and t == "mi":
        return round(n / 1760, 4)

    if s == "yd" and t == "cm":
        return n * 91.44

    if s == "yd" and t == "m":
        return round(n / 1.0936, 3)

    if s == "yd" and t == "km":
        return round(n / 1093.6, 4)

    if s == "yd" and t == "yd":
        return n

    #converts miles to other units
    if s == "mi" and t == "in":
        return n * 63360.0

    if s == "mi" and t == "ft":
        return n * 5280.0

    if s == "mi" and t == "yd":
        return n * 1760.0

    if s == "mi" and t == "cm":
        return round(n / 0.0000062137, 3)

    if s == "mi" and t == "m":
        return round(n / 0.00062137, 3)

    if s == "mi" and t == "km":
        return round(n / 0.62137, 3)

    if s == "mi" and t == "mi":
        return n

    #converts centimeters to other units
    if s == "cm" and t == "in":
        return n * .39370

    if s == "cm" and t == "ft":
        return round(n / 30.48, 3)

    if s == "cm" and t == "yd":
        return round(n / 91.44, 3)

    if s == "cm" and t == "mi":
        return round(n * 0.0000062137, 5)

    if s == "cm" and t == "m":
        return n / 100

    if s == "cm" and t == "km":
        return n / 100000

    if s == "cm" and t == "cm":
        return n

    #converts meters to other units
    if s == "m" and t == "in":
        return n * 39.37

    if s == "m" and t == "ft":
        return round(n * 3.2808, 3)

    if s == "m" and t == "yd":
        return round(n * 1.0936, 3)

    if s == "m" and t == "mi":
        return n * 0.00062137

    if s == "m" and t == "cm":
        return n * 100

    if s == "m" and t == "km":
        return n / 1000

    if s == "m" and t == "m":
        return n

    #converts kilometers to other units
    if s == "km" and t == "in":
        return n * 39370.0

    if s == "km" and t == "ft":
        return n * 3280.8

    if s == "km" and t == "yd":
        return n * 1093.6

    if s == "km" and t == "mi":
        return n * 0.62137

    if s == "km" and t == "cm":
        return n * 100000.0

    if s == "km" and t == "m":
        return n * 1000.0

    if s == "km" and t == "km":
        return n

    return f"Usage: length requires 3 arguments in the form of 'length, unit, unit'. Available units are in, ft, yd, mi, cm, m, km."


def speed(n, s, t):
    '''
    Speed converts n speed from unit s to unit t.
    Available units are miles per hour(mph), kilometers per hour (kmh), and meters per second (ms).
    Returns a float, rounded to a certain number of decimal points when necessary.

            Parameters:
                n (int / float): Any integer or float, positive or negative.
                s (str): A string which corresponds to one of the available units.
                T (str): Another string which corresponds to one of the available units.

            Returns:
                rounded float, to a certain number of decimal points
    '''

    #converts mph to other units
    if s == "mph" and t == "kmh":
        return round(n * 1.60934, 3)

    if s == "mph" and t == "ms":
        return round(n / 2.237, 3)

    if s == "mph" and t == "mph":
        return n

    #converts kilometers per hour to other units
    if s == "kmh" and t == "mph":
        return round(n / 1.60934, 3)

    if s == "kmh" and t == "ms":
        return round(n / 3.6, 3)

    if s == "kmh" and t == "kmh":
        return n

    #converts meters per second to other units
    if s == "ms" and t == "mph":
        return round(n * 2.237, 3)

    if s == "ms" and t == "kmh":
        return n * 3.6

    if s == "ms" and t == "ms":
        return n

    return f"Usage: speed requires 3 arguments in the form of 'speed, unit, unit'. Available units are mph, kmh, ms."