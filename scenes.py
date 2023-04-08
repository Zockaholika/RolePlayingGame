from logic import *

# Rot
# print("\033[91m" + "Dieser Text ist rot" + "\033[0m")
# Grün
# print("\033[92m" + "Dieser Text ist grün" + "\033[0m")
# Blau
# print("\033[94m" + "Dieser Text ist blau" + "\033[0m")
# Gelb
# print("\033[93m" + "Dieser Text ist gelb" + "\033[0m")


myScene1 = Scene("My first scene", 1)
myScene2 = Scene("This is my second Scene", 2)
myScene3 = Scene("This is my third Scene", 3)
myScene1.add_choice(myScene2, "Go left")
myScene2.add_choice(myScene1, "Go right")
myScene3.add_choice(myScene1, "go up")
myScene3.add_choice(myScene2, "go down")
myScene1.add_choice(myScene3, "go down")
myScene2.add_choice(myScene3, "go up")
