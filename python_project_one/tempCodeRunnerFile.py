if Count_Down == 0:
        if User_Score > CPU:
            print("{} wins with a score of {}. ".format(your_name.capitalize(),User_Score))
        elif User_Score < CPU:
            print("CPU wins with a score of {}. ".format(CPU))
        else:
            print("Its a tie!, Restart the program\n The games needs to restart\n")
            restart = input("Restart the game?: ").lower()
            if restart == "yes" or restart == "y" or restart == "yeah" or restart == "yh":
                repeat_if_tie()
            else:
                print("Ok!, Bye")
    print("Game Over")
