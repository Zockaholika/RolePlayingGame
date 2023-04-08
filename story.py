from logic import *



# myScene1 = Scene("My first scene", 1)
# myScene2 = Scene("This is my second Scene", 2)
# myScene3 = Scene("This is my third Scene", 3)
# myScene1.add_choice(myScene2, "Go left")
# myScene2.add_choice(myScene1, "Go right")
# myScene3.add_choice(myScene1, "go up")
# myScene3.add_choice(myScene2, "go down")
# myScene1.add_choice(myScene3, "go down")
# myScene2.add_choice(myScene3, "go up")

print("Welcome to our RPG!")
user = Player(str(input("Please enter your Nickname: ")))

myScene1 = Scene(f"Welcome {user.name}, to my RPG, what would you like to do?", 1)
myScene2 = Scene("You went left and there is a River", 2)
myScene3 = Scene("You went right and there is a Mountain", 3)
myScene4 = Scene("You see a small Bandit camp at the Riverbank", 4)
myScene5 = Scene("There are Skeletons all over the Track", 5)
# What can happen at the start
myScene1.add_choice(myScene2, "Go left")
myScene1.add_choice(myScene3, "Go right")
# If you went left
myScene2.add_choice(myScene4, "Follow the River")
myScene2.add_choice(myScene1, "Go back to the beginning")
# If you went right
myScene3.add_choice(myScene5, "Follow the Mountain track")
myScene3.add_choice(myScene1, "Go back to the beginning")
