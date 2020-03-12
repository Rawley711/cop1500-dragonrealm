#Rawley Moyer
#Integration Project - Pycharm
#This is Dragon Realm. An adventure game where you pick your own journey.
print("Welcome to my integration project!")
name = input("What is your name? ")
print("Hello, " + name)
# Dragon Realm

#Defining distances used in this game using arithmetic

lives = 3
score = 0
level = 1
#Creating List
rucksack = ["sword", "armor", "potion", "firewood", "flint"]

#Intro
Choice1 = input("Would you like to go on a quest? (yes/no) ")

if Choice1 == "yes":
    print("Excelsior!")
    print("You trek many hills until you reach a crossroads")
    Choice2 = input("Would you like to go left or right? ")
    if Choice2 == "right":
        print("Good Choice you avoided that pesky quick-sand")
        Choice3 = input("How many Furlong's would you like to go before resting? ")
        if Choice3 >= "3":
            print("You're a sturdy one")
            print()
            print("Unfortunately you find yourself walking into a a herd of sorcerers")
            print()
            print("Thank goodness you remembered your trusty sword.")
            print("However, there are many evil wizards")
            print()
            Choice4 = input("Do you wish to sneak away or fight? ")
            if Choice4 == "fight":
                print("Take a look inside your rucksack to see what you have")
                print(rucksack)
                Choice_weapon = input("Please pick weapon of choice ")
                if Choice_weapon == "sword":
                    print("You beat the wizards!")
                    score = score + 10
                    print("Your score is", score)
            else:
                print("Avoiding confrontation when possible is honorable")

        else:
            print("Resting is wise, for it is a long journey")


    else:
        print("Oh no! Quicksand! uh-buh-bye.")
        lives -= 3
        print("you have two lives left")

else:
    print("Well that's just poor sportsmanship")






#Citations:
#https://www.youtube.com/watch?v=UXkuJlDVEdo&list=PLvrGx2UE_sKSYMRFIzeLDMDqiI_8WBJ-_

#https://www.w3schools.com/python/python_lists.asp
