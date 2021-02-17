import random

# check if the number of games selected is even or odd
def even( num ):
    half = num / 2
    fHalf = round( half, 0 )
    isEven = None
    
    if half == fHalf:
        isEven = True
    else:
        isEven = False
    
    return isEven

# better randomization for the PC choice
def pcTurn():
    # do something
    print("pcTurn")

# main play function
def play():
    # introduction to the game
    print( "\nWelcome to the \"Rock - Paper - Scissors\" game!" )
    print( "To play write 1, 2 or 3 for (respectivily) rock, paper or scissors" )
    matchesNum = input( "Choose the number of matches: " )
    #while even( matchesNum ):
    #   do something
    
    winCount = 0
    loseCount = 0
    
    # repeate matches for as many times as chosen by the player
    for x in range( int(matchesNum) ):
        print( "\nMatch no." + str(x + 1) )
        text = input( "Make your move: " )
        pcAnsw = random.randint( 1, 3 )
        choice = int( text )
        
        # check the winner of the match
        if choice == pcAnsw:
            print( "It's a tie!")
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
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
            print( "You win this round!" )
            winCount += 1
            print( "Current points: " + str(winCount) + " : " + str(loseCount) )
        elif choice == 2 and pcAnsw == 3:
            print( "Paper against scissors!" )
            print( "You lose this round!" )
            loseCount += 1
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
    
    # print out the result of the game
    if winCount > loseCount:
        print( "\nYou won " + str(winCount) + " to " + str(loseCount) )
    elif winCount < loseCount:
        print( "\nYou lost " + str(winCount) + " to " + str(loseCount) )
    elif winCount == loseCount:
        print( "\nYou tied " + str(winCount) + " to " + str(loseCount) )
    
    print( "\nThank you for playing!" )
    
    playAgain = input( "Do you want to play again? [y/n]" )
    if playAgain == "y":
        play()
    elif playAgain == "n":
        print( "Bye!" )
    

# start playing when running the code
play()