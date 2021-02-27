#import json

#gameMode = input( "Would you like to start a new game or load an existing one? [new/load]" )
#if gameMode == "new":
#    main()
#elif gameMode == "load":
#    load()

#def close():
#    jsonContent = ""

#jsonFile = open( "tables.json" )
#tables = json.loads( jsonFile.read() )

print( "Welcome to this simple text-adventure game!" )

inventory = {

}

commands = { "/exit", "/commands" }

def pg1():
    # do nothing rn
    print( "You just survived a plane crash." )
    print( "Around you the plane is still on fire and no one is alive..." )
    print( "The plane crashed in a huge forest." )
    ch1 = input( "Are you going to look for something in the airplane or go into the forest? [plane/forest]" )
    if ch1 == "plane":
        pg2()
    elif ch1 == "forest":
        pg3()
    elif ch1 in commands:
        commandUsed( ch1 )


def pg2():
    print( "page 2 reached" )

def pg3():
    print("page 3 reached")

def commandUsed( command ):
    if command == "/exit":
        exit()
    elif command  == "/commands":
        print( "Commands: ..." )

def main():
    starting = input( "Type \"start\" to start the game and \"info\" to get instructions about it." )
    if starting == "start":
        print( "The game starts!")
        pg1()
    elif starting == "info":
        print( "During all the game you can use one of these commands that won't change your situation in the game:\n /exit\n /commands")
        main()

main()
