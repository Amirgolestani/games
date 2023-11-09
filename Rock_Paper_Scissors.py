# Rock Paper Scissors
# rock = sang
# paper = kaghaz
# scissors =  gheichi
player_1 = input ( " please select (P1):")
player_2 = input ( " please select (P2):")
if player_1 == "rock" and player_2 == "paper" :
    print ( "player 2 won")
elif player_1 == "rock" and player_2 == "scissors" :
    print ( "player 1 won")
elif player_1 == "rock" and player_2 == "rock" : 
    print ("draw")
elif player_1 == "paper" and player_2 == "rock" :
    print ( "player 1 won")
elif player_1 == "paper" and player_2 == "scissors" :
    print = ("player 2 won")
elif player_1 == "paper" and player_2 == "paper" :
    print ("draw")
elif player_1 == "scissors" and player_2 == "rock" :
    print ("player 2 won")
elif player_1 == "scissors" and player_2 == "paper" :
    print ( "player 1 won")
elif player_1 == "scissors" and player_2 == "scissors" :
    print = ("draw")
else :
    print ( " please enter valid words !")