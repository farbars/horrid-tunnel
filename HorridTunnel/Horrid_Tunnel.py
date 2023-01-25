import time
import os

weapon = False

def yesno():
    choice = ["yes","no"]
    d = ""
    counter = 0
    while counter < 3:
        d_print("\nDo you want to enter the Horrid Tunnel again? (yes or no): ")
        d = input()

        if d in choice:
            if d == "yes":
                time.sleep(2)
                clear()
                main()
            elif d == "no":
                time.sleep(2)
                clear()
                d_print("\nThank you for playing the Horrid Tunnel! Please Like, Share & Subscribe...")
                time.sleep(2)
                quit()
            break
        else:
            time.sleep(2)
            clear()
            d_print("Invalid option.\n")
            counter += 1

    if counter == 3:
        f_print("\nYou entered wrong option for more than 3 times. Exiting...")
        quit()

def d_print(s):
    for char in s:
        print(char, end="", flush=True)
        time.sleep(0.05)

def e_print(s):
    for char in s:
        print(char, end="", flush=True)
        time.sleep(0.1)

def f_print(s):
    for char in s:
        print(char, end="", flush=True)
        time.sleep(0.2)

def clear():
    os.system('cls||clear')

def creature():
    actions = ["fight","run"]
    global weapon
    e_print("A strange ghoul-like creature has appeared.\n")
    d_print("You can either run or fight it.\n")
    time.sleep(1)
    d_print("What are you going to do now?!\n")
    x = ""
    while x not in actions:
        print("Options: run/fight")
        x = input()

        if x == "fight":

            if weapon:
                time.sleep(2)
                clear()
                d_print("You kill the ghoul with the knife you found earlier.\nIt cries out for help as it vanishes into thin air.\n")
                e_print("You left running as you find one of the exits. At last!\n")
                time.sleep(2)
                yesno()
            else:
                time.sleep(2)
                clear()
                d_print("The ghoul-like creature has killed you and reap your flesh.\n")
                time.sleep(2)
                yesno()

        elif x == "run":
            time.sleep(2)
            clear()
            skeletons()
        else:
            time.sleep(2)
            clear()
            d_print("Time is of the essence...\n")
            time.sleep(2)
      
def skeletons():
    directions = ["backward","forward"]
    global weapon
    d_print("You see a wall of skeletons as you walk into the room.\n")
    e_print("Someone is watching you.\n")
    time.sleep(1)
    d_print("Where will you go now?\n")
    x = ""

    while x not in directions:
        print("Options: left/backward/forward")
        x = input()

        if x == "left":
            time.sleep(2)
            clear()
            d_print("You find a knife glowing which is held by one of corpse in the wall.\n")
            e_print("You keep it and think you might need it somehow...\n")
            weapon = True
        elif x == "backward":
            time.sleep(2)
            clear()
            intro()
        elif x == "forward":
            time.sleep(2)
            clear()
            creature()
        else:
            time.sleep(2)
            clear()
            d_print("You need to find to decide quick for your life...\n")
            time.sleep(2)
      

def haunted():
    directions = ["right","left","backward"]
    d_print("You hear crying voices that comes out from that hole in the wall.\n")
    e_print("You think you have awoken some ancient spirits.\n")
    time.sleep(1)
    d_print("Where would you like to go?\n")
    x = ""

    while x not in directions:
        time.sleep(1)
        print("Options: right/left/backward")
        x = input()

        if x == "right":
            time.sleep(2)
            clear()
            d_print("A massive count of zombies rising from the tombs as you enter the room.\n")
            e_print("You are shred into pieces.\n")
            time.sleep(2)
            yesno()
        elif x == "left":
            time.sleep(2)
            clear()
            d_print("You made it! You've found an exit to the cursed tunnel")
            e_print(" and promise to never go back ever again...\n")
            time.sleep(2)
            yesno()
        elif x== "backward":
            time.sleep(2)
            clear()
            intro()
        else:
            time.sleep(2)
            clear()
            print("Time is running out...\n")
            time.sleep(2)

def camera():
    directions = ["forward","backward"]
    d_print("You see a camera has been dropped on the ground.\n")
    f_print("Someone has been here recently.\n")
    time.sleep(1)
    d_print("Where would you like to go?\n")
    x = ""
    while x not in directions:
        time.sleep(1)
        print("Options: forward/backward")
        x = input()

        if x == "forward":
            time.sleep(2)
            clear()
            d_print("You made it! You've finally found you way out and")
            e_print(" plan to quit on exploring places like this...\n")
            time.sleep(2)
            yesno()
        elif x == "backward":
            time.sleep(2)
            clear()
            shadow()
        else:
            time.sleep(2)
            clear()
            d_print("That's not the time to think slow.\n")
      
def shadow():
    directions = ["right","backward"]
    e_print("You see a shadowy figure appear in the distance.\n")
    d_print("It looks like that it is approaching you any minute.\nDecide quickly on where to go.\n")
    x = ""

    while x not in directions:
        time.sleep(1)
        print("Options: right/left/backward")
        x = input()

        if x == "right":
            time.sleep(2)
            clear()
            camera()
        elif x == "left":
            time.sleep(2)
            clear()
            print("You find that this door opens into a wall. What direction now?\n")
        elif x == "backward":
            time.sleep(2)
            clear()
            intro()
        else:
            time.sleep(2)
            clear()
            d_print("You are growing tired and weary.\n")


def intro():
    directions = ["left","right","forward"]
    d_print("Walking for 5 minutes straight on your way out perhaps.\nNow, you are at a crossroads, and you can choose to go down any of the 4 hallways.")
    e_print("\nIt is too late go back now. Where would you like to go?\n")
    x = ""

    while x not in directions:
        time.sleep(1)
        print("Options: left/right/forward/backward")
        x = input()

        if x == "left":
            time.sleep(2)
            clear()
            shadow()
        elif x == "right":
            time.sleep(2)
            clear()
            skeletons()
        elif x == "forward":
            time.sleep(2)
            clear()
            haunted()
        elif x == "backward":
            time.sleep(2)
            clear()
            d_print("You find that this door opens into a wall. Where to go next?\n")
        else:
            time.sleep(2)
            clear()
            d_print("You hungry and wanted to get out to have a nice meal.\n")

def main():
    e_print("Welcome to the Horrid Tunnel!")
    time.sleep(2)
    d_print("\nAs a thrill-seeker, you have decided to visit the infamous Horrid Tunnel.\nHowever, during your admirable adventure, you find yourself lost.\nYou can choose to walk in multiple directions to find a way out.\n")
    e_print("Let's start with your name: ")
    name = input("")
    time.sleep(1)
    clear()
    e_print("Someone whispers to your ear as if that someone is standing near you.\nWhispering... Hope you can get out here alive, ")
    f_print(f"{name}...")
    time.sleep(2)
    clear()
    intro()

main()