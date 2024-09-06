from baza import Engine
import random
import datetime
from math_behind import Scores
from gamestation import Game
from user import User


class Silnik:
    def __init__(self):
        print("Welcome in hangman(but idk if i made that correctly &&&& whole freestyle ;3 ^^^^^^^^^^)")


    #Kilka rund wprowadzic

    def game(self):
        still=True

        name=input("What is your name? ")
        age=int(input("What is your age? "))

        while still:
            gra=Game()

            level=int(input("Choose your level from 1 to 3: "))
            gra.start_game(level,User(name,age))
            still_going=input("Would you like to play again? (y/n)")
            if still_going.lower()!="y":
                break



silnik=Silnik()


silnik.game()
