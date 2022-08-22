#Super Hero Name Generator
print("Welcome to Super Hero Name Generator")
print("")
print("Lets begin.")

#Starting Generator
play = "yes"
while play == "yes":
    print("")
    #Gathering Input
    userName = input("What is your name?: ").capitalize()
    userColour = input("What is your favourite colour?: ").lower()
    userNoun = input("Choose a noun: ").capitalize()

    #Checking Colour
    if userColour == "red":
        adjective = "Old"
    elif userColour == "orange":
        adjective = "Young"
    elif userColour == "yellow":
        adjective = "Big"
    elif userColour == "green":
        adjective = "Small"
    elif userColour == "blue":
        adjective = "Good"
    elif userColour == "purple":
        adjective = "Bad"
    elif userColour == "pink":
        adjective = "Pretty"
    elif userColour == "white":
        adjective = "Ugly"
    elif userColour == "black":
        adjective = "Cool"
    else:
        adjective = "Epic"

    print("")
    print("")

    #printing name
    print("Your super hero name is " + userName[1:].capitalize() +
          " The Incredibly " + adjective + " " + userNoun + " Person!!!")
    print("Now go fight some crime!")
    print("")
    #asking to play again
    play = input("Would you like to play again? (yes or no): ").lower()
    while play != "yes" and play != "no":
        play = input("Would you like to play again? (yes or no): ").lower()

#thanking player
if play == "no":
    print("")
    print("Thanks for playing :)")
