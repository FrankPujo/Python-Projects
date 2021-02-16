import random

def play():
    print( "\nWelcome to the \"Rock - Paper - Scissors\" game!" )
    print( "To play write 1, 2 or 3 for (respectivily) rock, paper or scissors" )
    matchesNum = input( "Choose the number of matches: " )
    
    winCount = 0
    loseCount = 0
    for x in range( int(matchesNum) ):
        print( "\nMatch no." + str(x + 1) )
        text = input( "Make your move: " )
        pcAnsw = random.randint( 1, 3 )
        choice = int( text )
        
        if choice == pcAnsw:
            print( "It's a tie!")
            print( " Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 1 and pcAnsw == 2:
            print( "Rock against paper!" )
            print( "You lose this round!" )
            loseCount += 1
            print( " Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 1 and pcAnsw == 3:
            print( "Rock against scissors!" )
            print( "You win this round!" )
            winCount += 1
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 2 and pcAnsw == 1:
            print( "Paper against rock!" )
            print( "You lose this round!" )
            loseCount += 1
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 2 and pcAnsw == 3:
            print( "Paper against scissors!" )
            print( "You win this round!" )
            winCount += 1
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 3 and pcAnsw == 1:
            print( "Scissors against rock!" )
            print( "You lose this round!" )
            loseCount += 1
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 3 and pcAnsw == 2:
            print( "Scissors against paper!" )
            print( "You win this round!" )
            winCount += 1
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
        
    if winCount >= loseCount:
        print( "\nYou won " + str(winCount) + " to " + str(loseCount) )
    elif winCount <= loseCount:
        print( "\nYou lost " + str(winCount) + " to " + str(loseCount) )
    elif winCount == loseCount:
        print( "\nYou tied " + str(winCount) + " to " + str(loseCount) )
    
    print( "\nThank you for playing!" )

play()