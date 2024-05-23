#-------------------------------------------------------------------------------
# Name:        project3
# Purpose:
#
# Author:      kandp
#
# Created:     22-05-2024
# Copyright:   (c) kandp 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print("Welcome to treasure island.Your mission is to find the treasure..")
c1=input("You're at a cross road where do you want to go? type 'left' or 'right'.")
if(c1=='left'):
    c1_1=input("you come to a lake. There is an island in the middle of the lake. type 'wait' to wait for a boat. type 'swim' to swim across")
    if(c1_1=='wait'):
        c1_1_1=input("You arrive at the island unharmed. There is a house with 3 doors RED, BLUE and YELLOW. Which color do you choose?")
        if(c1_1_1=='red' or c1_1_1=='blue'):
            print("you lose");
        else:
            print("you win");
    else:
        print("you drowned. hahahahahaha hahaha hahaha")
else:
    c2_1=input("you come to a road and a car is coming to you what will you do? 'run' or 'stay'")
    if(c2_1=='run'):
        c2_1_1=input("You arrive at a villa unharmed. There is a house with 3 doors RED, BLUE and YELLOW. Which color do you choose?")
        if(c2_1_1=='red' or c2_1_1=='blue'):
            print("you lose");
        else:
            print("you win");
    else:
        print("you are at the heaven now. hahahahaha hahaha hahaha")
