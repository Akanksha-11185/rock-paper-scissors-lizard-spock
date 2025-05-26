# Rock Paper Scissor Lizard Spock!
import random

#Introduction
print("Let's Play Rock Paper Scissor Lizard Spock! 😎")

print("\n Here are the Rules📜: \n")
print("Scissors✌🏻 cut Paper🖐🏻.")
print("Paper🖐🏻 covers Rock✊🏻.")
print("Rock✊🏻 crushes Lizard🦎.")
print("Lizard🦎 poisons Spock🖖🏻.")
print("Spock🖖🏻 smashes Scissors✌🏻.")
print("Scissors✌🏻 beat Lizard🦎.")
print("Lizard🦎 eats Paper🖐🏻.")
print("Paper🖐🏻 disproves Spock🖖🏻.")
print("Spock🖖🏻 vaporizes Rock✊🏻.")
print("Rock✊🏻 breaks Scissors✌🏻.")

print("\n")
print("\n")

print("Enter 1 for Rock✊🏻")
print("Enter 2 for Scissors✌🏻")
print("Enter 3 for Paper🖐🏻")
print("Enter 4 for Lizard🦎")
print("Enter 5 for Spock🖖🏻")
player = int(input("\n Select Number Between 1 to 5: ")) #Take user input
print("\n Your Move: ")
if player == 1:
    print("Rock✊🏻")
elif player == 2:
    print("Scissors✌🏻")
elif player == 3:
    print("Paper🖐🏻")
elif player == 4:
    print("Lizard🦎")
elif player == 5:
    print("Spock🖖🏻")        
else:
    print("Invalid input")  
    exit()  

computer =  random.randint(1,5)   

print("\n Computer's Move: ")

if computer == 1:
    print("Rock✊🏻")
elif computer == 2:
    print("Scissors✌🏻")
elif computer == 3:
    print("Paper🖐🏻")
elif computer == 4:
    print("Lizard🦎")
else:
    print("Spock🖖🏻")

# Comparing User and Computer Input 

if computer == player:
    print("It's a draw!")
    exit()

if player == 1 and computer == 2:
    print("Congrats! You Won!🥳")
elif player == 1  and computer == 4:
    print("Congrats! You Won!🥳")
elif player == 2 and computer == 3:
    print("Congrats! You Won!🥳")
elif player == 2 and computer == 4:
    print("Congrats! You Won!🥳")    
elif player == 3 and computer == 1:
    print("Congrats! You Won!🥳")    
elif player == 3 and computer == 5:
    print("Congrats! You Won!🥳") 
elif player == 4 and computer == 3:
    print("Congrats! You Won!🥳")
elif player == 4 and computer == 5:
    print("Congrats! You Won!🥳")   
elif player == 5 and computer == 1:
    print("Congrats! You Won!🥳") 
elif player == 5 and computer == 2:
    print("Congrats! You Won!🥳") 

else:
    print("Awww! You Loss!☹️")    