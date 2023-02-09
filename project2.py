#Title: Wish it was a dream
#Setting: Mall 
#Story/ Game Summary: Two girls go to the mall and get lost, the certain "challenge" is to find them before the time runs out. In reality tho I made this game lead you to go to the Toy store no matter what. Most of the plot and main like story happens in the toy store. No matter what, You lose ur sister and you take a speacial path. In this path, once you get to the bottom as youre about to reach for the doors leading out, someone grabs you. The ending is basically that it was all a dream. Although it wasnt necesarilly just a dream, more of the moment in which the girl or you got kidnapped (which you still are). This is basically a story in whihc I was inspired by some common kidnappings that happen in malls. In the end, in some cases the kids are not found and this is a referance to the dreams or in a way fear and trauma those kids have in the end and in this case this game represents a dream that they wish was not their cruel reality. 
#Global Variable: I used the global variable as a kind of distraction to what the game and story really is and represents. The time and minutes do have a meaning. They represent the minutes that passed before the kid got kidnapped so like the time they were last seen and after 25 minutes they were kidnapped (not sure if that makes sense). 
########
#import modules
#######
import os
import time
########
#define functions
#######

def check_time():
    os.system('clear')
    global minutes
    minutes = minutes + 3
    print("You now have", 25 - minutes, "minutes")
    if minutes >= 25:
        minu()


def minu():
    global minutes
    print("Times up! Try again.")

def start():
    print("Today you are at the mall with you're sister. You seem to have separated from your parents\nLets look for them! We have 25 minutes to find them.")
    firstfloor()

def firstfloor():
    print("You are in the first floor")
    move = input("\nWhere would you like to go? Say one of these choices:\n(type in lowercases!)\n\tClothes Store\n\tGame Store\n\tUpstairs\n\tKeep Walking\n")
    if move.lower() == "clothes store":
        clothesstore()
    elif move.lower() == "upstairs":
        upstairs()
    elif move.lower() == "keep walking":
        keepwalking()
    else:
        #TODO: what should happen if they type something else? nothing
        gamestore()

def clothesstore():
    check_time()
    print("You are in the Clothes Store, you get distracted and loose track of time. Your little sister throws a tantrum, so you walk out\n She wants to go to the Toy Store. Take her to the toy store :)")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tKeep walking\n\tUpstairs\n")
    if move.lower() == "upstairs":
        upstairs()
    elif move.lower() == "room3":
        upstairs()
    else:
        pass

def gamestore():
    check_time()

    print("You are in the Game Store, you get distracted and loose track of time. Your parents arent there so you walk out\nLets look somewhere else!")
    move = input("\nWhere would you like to go? Say one of these choices:\n\tClothes Store\n\tKeep walking\n\tUpstairs\n")
    if move.lower() == "clothes store":
        clothesstore()
    elif move.lower() == "upstairs":
        upstairs()
    else:
        keepwalking()


def upstairs():
    check_time()
    print("You are in the Second Floor")
    move = input("Where would you like to go? Say one of these choices:\n\tToy Store\n\tBathroom\n\tDownstairs\n")
    if move.lower() == "toy store":
        toystore()
    elif move.lower() == "down stairs":
        firstfloor()
    else:
        bathroom()

def bathroom():
    check_time()
    print("\nYou had to use the bathroom urgently youre sister was really eager to go to the Toy Store that was right in front. You told her to wait and that after you use the bathroom you would take her.\nOnce you finish using the bathroom and open the door, your sister runs out. You try to run after her but it was crowded.\nYou go into the Toy Store and look around for her but nothing. You look at a nearby staircase.\n")
    move = input("\nMaybe this will be a way faster to security.\nLets go to security.\nType down to keep going.\n")
    if move.lower() == "down":
        secretstair()

def toystore():
    check_time()
    print("\nYou walk into the Toy Store and all the toys catch your attention. Without thinking much you rush over to the aisle where your favorite toys are. You loose track of time and decide its time to go back.\nYou look to your side and your sister is no longer there. You look everywhere but she is no where to be found.")
    move = input("\n\nLets go back. Maybe security will be able to help now.\nYou see some stairs in the Toy Store that say they lead to downstairs.\nMaybe this way is quicker. Type down.\n")
    if move.lower() == "down":
        secretstair()

def secretstair():
    check_time()
    print("\nYou go down the stairs and once you reach the bottom you see a single door. As you're about to open it you feel someone touch your shoulder and you suddenly shiver after hearing a fimiliar voice whisper in your ear.")
    move = input("\nType next to continue\n")
    if move.lower() == "next":
        print("\n.\n.\nYou wake up covered in sweat, you look around and realize that it wasnt just a dream. You relived the moment in which you got kidnapped.\nYou here the same voice call out for you.\nHes back. In that moment you wish that it was all a dream.")

def keepwalking():
    check_time()
    print("In this hallway there's only a Food Court and the Security Room.")
    move = input("Where would you like to go? Say one of these choices:\n\tFood Court\n\tSecurity\n\tBack\n")
    if move.lower() == "food court":
        foodcourt()
    elif move.lower() == "security":
        security()
    else:
        firstfloor()

def foodcourt():
    check_time()
    print("\nYou enter the Food Court but you remember you dont have money.\nYou walk out.")
    move = input("Lets go back to where we were! Type back.\n")
    if move.lower() == "back":
        firstfloor()

def security():
    check_time()
    print("\nYou walk in and there is only a lady standing at the front desk. She says to come back later because there is something being taken care of. You wanted to wait there but your sister was bored and decide to go to the Toy Store.\n Go to the Toy Store!")
    move = input("Lets go back to where we were. Type back.\n")
    if move.lower() == "back":
        firstfloor()
########
#main
#######
#TODO: Add some global variables
minutes = 0
start()