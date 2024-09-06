from baza import Engine
import random
import datetime
from math_behind import Scores
import threading
import time
from serwer import Server
from user import User


class Game:
    def __init__(self):
        self.words=Engine().get_words()
        self.time_limit=30
        self.server=Server()
        self.server.create_table()




    #Sortowanie slow zeby miec podzial na level trudnosci
    #Zasady sortowanie
    #1.<5 or set<5
    #2.>5  and < 8 or set>=5
    #3.>8 or set>=10

    def sorting_requairment(self,word_length_start,word_length_end,set_length_start,set_length_end):
        words=[i for i in self.words if (len(i)<=word_length_end and len(i)>word_length_start) or (len(set(i))>set_length_start and len(set(i))<=set_length_end)]
        return words
    def sorting_by_level(self,level):
        if level == 1:
            words=self.sorting_requairment(1,5,1,5)
        elif level == 2:
            words=self.sorting_requairment(5,8,5,8)
        elif level == 3:
            words=self.sorting_requairment(9,15,9,15)
        return words



    def get_random_word(self,level):
        return random.choice(self.sorting_by_level(level))

    def word_floor_builder(self,word):
        return ["_" for i in range(0,len(word))]

    def check_letter(self,letter,word):
        letter=letter.lower()
        found=False
        if letter.lower()==word.lower():

            found=True
        for index,value in enumerate(word):
            if value.lower()==letter.lower():
                self.bricks[index]=value
                self.correct_guesses+=1
                found=True
        return found


    def check_word(self,word,list):
        if "".join(list)==word:
            return True
        else:
            return False



    def add_corect_guesses(self,used_letters,final_word):
        counter=0
        for i in used_letters:
            if i in final_word:
                counter+=1

        return counter


    def start_game(self,level,user):

        scores=Scores()
        word=self.get_random_word(level)
        tries=0
        self.bricks=self.word_floor_builder(word)

        start_time=datetime.datetime.now()
        used_words=[]
        self.correct_guesses=0


        while tries<len(word)+3:

            if len(used_words)>0:
                print(f"Użyte litery: {', '.join(used_words)}")


            print(self.bricks)
            guessing=input("Chcesz zgadywac slowo cale (y/n)")
            if guessing.lower()=='y':
                guessed_word=input("Wpisz to slowo")
                if self.check_letter(guessed_word,word):
                    print("Wygrałes")
                    end_time=datetime.datetime.now()
                    duration=end_time-start_time
                    scores.add_game(duration,self.add_correct_guesses(used_words,word),len(used_words),True)

                    self.server.add_user(user.get_nickname(),duration,scores.calculate_precision(self.add_corect_guesses(used_words,word)),True)
                    print(scores.get_tries()[-1])
                    break
            letter=input("Wpisz litere: ")
            used_words.append(letter)
            if not self.check_letter(letter,word):
                print("Litera nie wystepuje w tym slowie")
                print(f"Zostalo ci {(len(word)+3)-tries} prób")
                tries+=1

            if self.check_word(word,self.bricks):
                print("Wygrałes")
                end_time=datetime.datetime.now()
                duration=end_time-start_time
                scores.add_game(duration,self.add_correct_guesses(used_words,word),len(used_words),True)

                self.server.add_user(user.get_nickname(),duration,scores.calculate_precision(self.add_corect_guesses(used_words,word)),True)
                print(scores.get_tries()[-1])
                break
            elif tries>=len(word)+3:
                print("Nie udało się. Gra zakończona.")
                print("Slowo które bylo "+word)
                end_time = datetime.datetime.now()
                duration = (end_time - start_time).total_seconds()
                scores.add_game(duration, self.add_correct_guesses(used_words,word), len(used_words), False)

                self.server.add_user(user.get_nickname(),duration,scores.calculate_precision(self.add_corect_guesses(used_words,word)),True)
                print(scores.get_tries()[-1])







