
from local_packages.myFunctions import cpu_random_select_function, possibleOutcomes, user_choice
from local_packages.myFunctions import user_name, outcomes

def repeat_if_tie():
    rock_paper_scissors = possibleOutcomes()
    print("\n***********************************************************")
    print("This is a rock_paper_scissors game!, Play Objectively.....")
    print("***********************************************************\n")

    your_name = input("Enter your name: ")
    User_name_capitalize = user_name(your_name)

    #score board
    Count_Down = 3
    print("\n--> Count down = {}.".format(Count_Down))
    User_Score = 0
    print("--> {} Score = {}.".format(your_name.capitalize(),User_Score))
    CPU = 0
    print("--> CPU Score = {}.".format(CPU))


    #the game starts from here with a count down of 3
    while Count_Down > 0:
            playerSelect = input("\nEnter R as Rock, P as Paper and S as Scissors: ")
            real_user = playerSelect.lower()
            player_now = user_choice(real_user)  
            if player_now == "r":
                print("\nPlayer chose Rock")
            elif player_now == "p":
                print("\nPlayer chose Paper")
            elif player_now == "s":
                print("\nPlayer chose Scissors") 
            

                
            # cpu description of selected outcomes as rock or paper or scissors
            cpu = cpu_random_select_function()
            if cpu == 'r': 
                print("CPU chose Rock\n")       
            elif cpu == 'p':
                print("CPU chose Paper\n")        
            elif cpu == 's':
                print("CPU chose scissors\n")
                
            # the feedback for the outcome of each count down or event
            outcome_here = outcomes(player_now, cpu)
            if ((outcome_here == "s draw") or (outcome_here == "r draw") or (outcome_here == "p draw")):
                outcome_here = print("Outcome: Draw\n")
            elif ((outcome_here == "user p") or (outcome_here == "user s") or (outcome_here == "user r")):
                outcome_here = print("Outcome: {} wins.".format(your_name.capitalize()))
                User_Score += 1    
            elif ((outcome_here == "cpu p") or (outcome_here == "cpu s") or (outcome_here == "cpu r")):
                outcome_here = print("Outcome: CPU wins.")
                CPU += 1      

            # the updated scoreboard
            Count_Down -= 1
            print("\nCount down is now: ", +  Count_Down)
            print("{} Score: ".format(your_name.capitalize()), +  User_Score)
            print("CPU Score: ", +  CPU)
            
    # result of the winner and the possibility of restarting if there comes a tie
    if Count_Down == 0:
        if User_Score > CPU:
            print("\n{} wins with a score of {}. ".format(your_name.capitalize(),User_Score))
            print("Game \n")
        elif User_Score < CPU:
            print("\nCPU wins with a score of {}. ".format(CPU))
            print("Game Over\n")
        else:
            print("\nIts a tie!....\n The games needs to restart\n")
            restart = input("Restart the game?: ").lower()
            if restart == "yes" or restart == "y" or restart == "yeah" or restart == "yh":
                repeat_if_tie()
            else:
                print("Ok!, Bye\n")

# function called if there is a tire and the player accepts to play again
repeat_if_tie()
