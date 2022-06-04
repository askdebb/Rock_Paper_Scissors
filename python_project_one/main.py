import random

def captial(name):
    final_name = name.capitalize()
    return final_name

possible_outcome_selection = ['r', 'p', 's']
print("\n***********************************************************")
print("This is a rock_paper_scissors game!, Play Objectively.....")
print("***********************************************************\n")

your_name = input("Enter your first name: ")
print("\nWelcome {}!".format(captial(your_name)))
User_name_capitalize = captial(your_name)


Count_Down = 3
print("\n--> Count down = {}.".format(Count_Down))
User_Score = 0
print("--> {} Score = {}.".format(User_name_capitalize,User_Score))
CPU = 0
print("--> CPU Score = {}.".format(CPU))


# game starts for only 3 rounds
while Count_Down <= 3 and Count_Down != 0:
# cpu selection
    for cpu_choice in possible_outcome_selection:
        cpu_turn_select = random.choice(possible_outcome_selection)
        cpu = cpu_turn_select.lower()

    user = input("\nEnter R as Rock, P as Paper and S as Scissors: ")
    real_user = user.lower()

    # User description of selected outcomes as rock or paper or scissors

    if real_user == 'r': 
        print("{} chose Rock".format(User_name_capitalize))
    elif real_user == 'p':
        print("{} chose Paper".format(User_name_capitalize))
    elif real_user == 's':
        print("{} chose scissors".format(User_name_capitalize))
        

        
    # cpu description of selected outcomes as rock or paper or scissors
    if cpu == 'r': 
        print("CPU chose Rock\n")       
    elif cpu == 'p':
        print("CPU chose Paper\n")        
    elif cpu == 's':
        print("CPU chose scissors\n")
        

    # possible outcomes checked
    if real_user == 'r' and cpu == 'p':
        print("Outcome: CPU wins\n")
        CPU += 1
    elif real_user == 'r' and cpu == 'r':
        print("Draw\n")
    elif real_user == 'r' and cpu == 's':
        print("Outcome: {} wins".format(User_name_capitalize))
        User_Score += 1
    elif real_user == 'p' and cpu == 'p':
        print("Outcome: Draw\n")
    elif real_user == 'p' and cpu == 'r':
        print("Outcome: {} wins".format(User_name_capitalize))
        User_Score += 1
    elif real_user == 'p' and cpu == 's':
        print("Outcome: CPU wins\n")
        CPU += 1
    elif real_user == 's' and cpu == 'p':
        print("Outcome: {} wins\n".format(User_name_capitalize))
        User_Score += 1
    elif real_user == 's' and cpu == 'r':
        print("Outcome: CPU wins\n")
        CPU += 1
    elif real_user == 's' and cpu == 's':
        print("Outcome: Draw\n")
    else:
        print("Program stopped unexpectedly...")
        print("Possible reasons....\n")
        print("{}!!!!.... you chose wrong outcome selection, ".format(your_name.upper())) 
        print("Restart the program and ...")  
        print("Kindly Enter R as Rock, P as Paper and S as Scissors\n") 
        print("NO WINNER")
        break
    Count_Down -= 1
    print("Count down is now: ", +  Count_Down)
    print("CPU Score: ", +  CPU)
    print("{} Score: ".format(User_name_capitalize), +  User_Score)

if Count_Down == 0:
    if User_Score > CPU:
        print("{} wins with a score of {}. ".format(User_name_capitalize,User_Score))
    elif User_Score < CPU:
        print("CPU wins with a score of {}. ".format(CPU))
    else:
        print("Its a tie!, Restart the program")
print("Game Over")
