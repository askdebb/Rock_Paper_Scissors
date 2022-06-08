import random


def capital(name):
    final_name = name.capitalize()
    return final_name

def user_identity(player):
    player_name_here = capital(player)
    return player_name_here


def user_name(firstName):
    users_first_name_Upper = capital(firstName)
    users_first_name = print("\nWelcome {}!".format(users_first_name_Upper))
    return users_first_name


def possibleOutcomes():
    possible_outcome_selection = ['r', 'p', 's']
    return possible_outcome_selection


#cpu select function
# game starts for only 3 rounds

def cpu_random_select_function():
        cpu_turn_select = random.choice(possibleOutcomes())
        cpu = cpu_turn_select.lower()
        return cpu

def user_choice(user_input):
    while user_input != "r" and user_input != "p" and user_input != "s":
        user_input = input("Invalid input......\nKindly Enter R as Rock, P as Paper and S as Scissors: ")
    userLower = user_input.lower()
    return userLower   



def outcomes(user, cpu):
     # possible outcomes checked
    if user == 'r' and cpu == 'p':
        ans = "cpu p"
        
    elif user == 'r' and cpu == 'r':
        ans = "r draw"
    elif user == 'r' and cpu == 's':
        ans = "user r"
        
    elif user == 'p' and cpu == 'p':
        ans = "p draw"
        
    elif user == 'p' and cpu == 'r':
        ans = "user p"
        
    elif user == 'p' and cpu == 's':
        ans = "cpu s"
        
    elif user == 's' and cpu == 'p':
        ans = "user s"
        
    elif user == 's' and cpu == 'r':
        ans = "cpu r"
        
    elif user == 's' and cpu == 's':
        ans = "s draw"
    return ans
