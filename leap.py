import sys

def module( number, base ):
    zeroMod = number % base
    gMod = None
    
    if zeroMod == 0:
        gMod = True
    else:
        gMod = False
    return gMod


def checkString( string ):
    if string == "help":
        print( "To use the leap year calculator type an year and check if it is leap or not" )
        print( "Type \"about\" to know more about leap days calculation" )
        print( "Type \"exit\" to exit the calculator" )
        checkLeap()
    elif string == "about":
        print( "We all know that leap years are every 4 years right? Well, kind of." )
        print( "Not everybody knows that actually secolar years (1000, 1100, 1200, 1300 and so on) are not leap, UNLESS they are divisble by 400 (like 800, 1200, 1600, 2000); in this case they are leap anyway" )
        checkLeap()
    elif string == "exit":
        print( "Bye!" )
        sys.exit()
    

def checkLeap():
    print( "\nWelcome to the leap year calculator!" )
    yearStr = input( "Choose an year and check if it is leap or not: " )
    checkString( yearStr )
    yearNum = int( yearStr )
    leap = None
    
    
    if module( yearNum, 4 ):
        if module( yearNum, 100 ):
            if module( yearNum, 400 ):
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap =  False
    
    if leap:
        print( yearStr + " is a leap year!" )
    else:
        print( yearStr + " is not a leap year!" )
    

checkLeap()