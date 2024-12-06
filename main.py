print(r'''
                        ,////,
                        /// 6|
                        //  _|
                       _/_,-'
                  _.-/'/   \   ,/;,
               ,-' /'  \_   \ / _/
               `\ /     _/\  ` /
                 |     /,  `\_/
                 |     \'
 pb  /\_        /`      /\
   /' /_``--.__/\  `,. /  \
  |_/`  `-._     `\/  `\   `.
            `-.__/'     `\   |
                          `\  \
                            `\ \
                              \_\__
                               \___)
    
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
act1 = input("Type 'Left' or 'Right' \n")
if act1 == "Left" or act1 == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    act2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across\n")

    if act2 == "Wait" or act2 == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        act3 = input("One red, one yellow and one blue. Which colour do you choose?\n")

        if act3 == "Red" or act3 == "red":
            print("Burned by fire.")
            print("Game Over:(")
        elif act3 == "Yellow" or act3 == "yellow":
            print("You Win! :)")
        elif act3 == "Blue" or act3 == "blue":
            print("Eaten by beasts.")
            print("Game Over :(")
        else:
            print("Game Over :(")

    elif act2 == "Swim" or act2 == "swim":
        print("Attacked by trout")
        print("Game Over:(")
    else:
        print("Game Over :(")

elif act1 == "Right" or act1 == "right":
    print("Fall into a hole.")
    print("Game Over:(")
else:
    print("Game Over :(")



