print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input("You're at a cross road. Where do you want to go?\n   Type \"left\" or \"right\" ")
if crossroad == "right" or crossroad == "Right":
    print("You fell into a hole. Game Over.")
elif crossroad == "left" or crossroad == "Left":
    lake = input("You came across a lake. There's an island in the middle of the lake.\n    Type \"swim\" to swim or \"wait\" to wait for a boat ")
    if lake == "swim" or lake == "Swim":
        print("A crocodile eats you. Game Over.")
    elif lake == "wait" or lake == "Wait":
        door = input("You reach the island unharmed. There is a house with three doors.\n  One red, one yellow and one blue. Which color do you choose? ")
        if door == "yellow" or door =="Yellow":
            print("You found the treasure. You WIN!")
        else:
            print("The room has a tiger in it. Game Over.")