import re
import requests
from tabulate import tabulate
import convert

UNITS = {
        "temperature": ["c", "f", "k"],
        "weight": ["lb", "kg", "g", "mg", "st"],
        "volume": ["gal", "qt", "pt", "cup", "floz", "l", "ml"],
        "length": ["ft", "in", "yd", "mi", "cm", "m", "km"],
        "speed": ["mph", "kmh", "ms"],
        "currency": ["aed",
                     "afn",
                     "all",
                     "amd",
                     "ang",
                     "aoa",
                     "ars",
                     "aud",
                     "awg",
                     "azn",
                     "bam",
                     "bbd",
                     "bdt",
                     "bgn",
                     "bhd",
                     "bif",
                     "bmd",
                     "bnd",
                     "bob",
                     "brl",
                     "bsd",
                     "btn",
                     "bwp",
                     "byn",
                     "bzd",
                     "cad",
                     "cdf",
                     "chf",
                     "clp",
                     "cny",
                     "cop",
                     "crc",
                     "cup",
                     "cve",
                     "czk",
                     "djf",
                     "dkk",
                     "dop",
                     "dzd",
                     "egp",
                     "ern",
                     "etb",
                     "eur",
                     "fjd",
                     "fkp",
                     "fok",
                     "gbp",
                     "gel",
                     "ggp",
                     "ghs",
                     "gip",
                     "gmd",
                     "gnf",
                     "gtq",
                     "gyd",
                     "hkd",
                     "hnl",
                     "hrk",
                     "htg",
                     "huf",
                     "idr",
                     "ils",
                     "imp",
                     "inr",
                     "iqd",
                     "irr",
                     "isk",
                     "jep",
                     "jmd",
                     "jod",
                     "jpy",
                     "kes",
                     "kgs",
                     "khr",
                     "kid",
                     "kmf",
                     "krw",
                     "kwd",
                     "kyd",
                     "kzt",
                     "lak",
                     "lbp",
                     "lkr",
                     "lrd",
                     "lsl",
                     "lyd",
                     "mad",
                     "mdl",
                     "mga",
                     "mkd",
                     "mmk",
                     "mnt",
                     "mop",
                     "mru",
                     "mur",
                     "mvr",
                     "mwk",
                     "mxn",
                     "myr",
                     "mzn",
                     "nad",
                     "ngn",
                     "nio",
                     "nok",
                     "npr",
                     "nzd",
                     "omr",
                     "pab",
                     "pen",
                     "pgk",
                     "php",
                     "pkr",
                     "pln",
                     "pyg",
                     "qar",
                     "ron",
                     "rsd",
                     "rub",
                     "rwf",
                     "sar",
                     "sbd",
                     "scr",
                     "sdg",
                     "sek",
                     "sgd",
                     "shp",
                     "sle",
                     "sos",
                     "srd",
                     "ssp",
                     "stn",
                     "syp",
                     "szl",
                     "thb",
                     "tjs",
                     "tmt",
                     "tnd",
                     "top",
                     "try",
                     "ttd",
                     "tvd",
                     "twd",
                     "tzs",
                     "uah",
                     "ugx",
                     "usd",
                     "uyu",
                     "uzs",
                     "ves",
                     "vnd",
                     "vuv",
                     "wst",
                     "xaf",
                     "xcd",
                     "xdr",
                     "xof",
                     "xpf",
                     "yer",
                     "zar",
                     "zmw",
                     "zwl", ]
        }


def main():
    #start infinite loop to get user input
    while True:
        try:
            #get user input
            user_input = prompt()
            #if input is help, print msgs
            if user_input.lower().strip() == "help":
                print("----------")
                print("For optimal usage, please use the format 'NUMBER SYMBOL to SYMBOL'. Capital letters are not required.")
                print("----------")
                print("E.G. '10 mph to kmh'")
                print("----------")
                print("To see a list of available symbols, press type SYMBOLS. Otherwise type EXIT")
                #get input from help msgs
                msg = input(">>")
                #if user types symbols, write symbols
                if msg.lower().strip() == "symbols":
                    print(tabulate(UNITS, headers="keys", tablefmt="psql"))
                continue
            #if user's input is not help, call parse on input
            else:
                user_input = parse(user_input.strip())
                #break out of while loop
                break
        #if value error, print messages, reprompt for input
        except ValueError:
            print("Usage: proper input should be formatted as NUMBER UNIT to UNIT.")
            print("If unsure, please type help.")
            pass
    #print return value of calling conversion on user's input
    print(conversion(user_input))



def prompt():
    '''
    Prints a welcome message to the user, informs them of the help message, prompts for input.
    Returns the string of user's input
    '''
    print("----------")
    print("Welcome to the conversion program! You can convert American measurement units to Metric units and vice versa.")
    print("----------")
    print("What would you like to do first? If you know what you want to convert, go ahead and type it. If you need help, just type help.")
    return input(">>")


def parse(text):
    '''
    Uses regular expression to match the passed 'text' to the desired pattern. If the pattern is not matched, raise value error.
    If match groups 2 and 3 are not in the same list of values in the UNITS, raise value error.
    Returns a dictionary where the key is one of temperature, weight, volume, length, speed, currency and the value is a list of the match groups from the pattern
    '''
    text = text.lower()
    if matches := re.search(r"(\d*,?\d*?\.?\d*)\s+(\w+)\s+(?:to)\s+(\w+)", text):
        for unit in UNITS:
            if matches.group(2) in UNITS[unit] and matches.group(3) in UNITS[unit]:
                return {unit: [matches.group(1), matches.group(2), matches.group(3)]}
    else:
        raise ValueError
    raise ValueError


def conversion(text):
    '''
    Expects a dictionary as its one parameter. Extracts the key and values from the dictionary, assigning them to different variables.
    The key is checked and a conversion function from the convert module is called.
    Returns a string.
    '''

    for key in text:
        key = key
    quantity = float(text[key][0].replace(",", ""))
    before = text[key][1]
    after = text[key][2]

    if key == "speed":
        new_quantity = convert.speed(quantity, before, after)
        return f"{quantity} {before} is {new_quantity} {after}"

    if key == "temperature":
        new_quantity = convert.temperature(quantity, before, after)
        return f"{quantity} {before.capitalize()} is {new_quantity} {after.capitalize()}"

    if key == "volume":
        new_quantity = convert.volume(quantity, before, after)
        return f"{quantity} {before} is {new_quantity} {after}"

    if key == "weight":
        new_quantity = convert.weight(quantity, before, after)
        return f"{quantity} {before} is {new_quantity} {after}"

    if key == "length":
        new_quantity = convert.length(quantity, before, after)
        return f"{quantity} {before} is {new_quantity} {after}"

    if key == "currency":
        end = f"{before}/{after}/{quantity}"
        response = requests.get("https://v6.exchangerate-api.com/v6/6488df943648dba6e9424b62/pair/" + end)
        data = response.json()
        return f"{quantity:,.2f} {before.upper()} is {data['conversion_result']:,.2f} {after.upper()}"


if __name__ == "__main__":
    main()