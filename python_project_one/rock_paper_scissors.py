import random

number_list = ['rock', 'paper', 'scissors']

print("This is a rock_paper_scissors game!")

print("Play well")

user = input("Enter R as Rock, P as Paper and S as Scissors: ")
real_user = user.lower()
#print(number_list[1])  --> rock
#print(number_list[2])  --> scissors
#print(number_list[0])  --> rock

if real_user == 'r': 
    print("You chose Rock")
    real_user = number_list[0]

elif real_user == 'p':
    print("You chose Paper")
    real_user = number_list[1]
elif real_user == 'scissors':
    print("You chose scissors")
    real_user = number_list[2]

count = len(number_list)

for k in number_list:
    jay = random.choice(number_list)
if real_user == jay:
    print(real_user + ' is player and ' + jay + ' is cpu')
    count -= 1