
from stylecss import *
from figure import *

class Scene:
    def __init__(self, description: str, index: int):
        self.__paths = []  # hier werden die Choices abgespeichert
        self.__description = description
        self.__index = index

    def __repr__(self):
        text = self.__description + "\n"
        text += color.GREEN + "Choices:" + color.RESET + "\n"
        choice_number = 1
        for choice in self.__paths:
            text += color.GREEN + str(choice_number) + color.RESET  + ": " + str(choice) + "\n"
            choice_number += 1
        return text

    def add_choice(self, scene, text: str):
        self.__paths.append(Choice(text, scene))

    def get_paths(self):
        return self.__paths


class Choice:
    def __init__(self, text: str, scene: Scene):
        self.__text = text
        self.__scene = scene

    def __repr__(self):
        return self.__text

    def get_scene(self):
        return self.__scene


class Game:
    def __init__(self, scene: Scene):
        self.__current_scene = scene

    def print_description(self):
        print(self.__current_scene)

    def user_choice(self, counter=1):
        if counter > 3:
            print("To much Try´s, Game Over")
            exit(0)
        else:
            choice = input("Your choice: ")
            if not choice.isdigit():
                print("\033[91m" + "Invalid input: Please enter a number" + "\033[0m")
                self.print_description()
                counter += 1
                self.user_choice(counter)
            elif (int(choice) - 1) >= len(self.__current_scene.get_paths()) or (int(choice) - 1) < 0:
                print("\033[91m" + "Choice out of Range, try Again" + "\033[0m")
                self.print_description()
                counter += 1
                self.user_choice(counter)
            else:
                self.__current_scene = self.__current_scene.get_paths()[(int(choice) - 1)].get_scene()

