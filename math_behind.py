class Scores:
    def __init__(self):
        self.tries=[]





    def calculate_precision(self,correct_guesses,used_letters):
        if used_letters==0:
            return 1
        return (correct_guesses/used_letters)*100
    def add_game(self,time,correct_guesses,total_letters,result):
        precision=self.calculate_precision(correct_guesses,total_letters)
        self.tries.append([time,precision,result])

    def get_tries(self):
        return self.tries