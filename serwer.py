import sqlite3



class Server:
    def __init__(self):
        self.conn=sqlite3.connect('hangman.db')


        self.cursor=self.conn.cursor()




    def create_table(self):
        self.conn.execute("CREATE TABLE IF NOT EXISTS Scores (user TEXT,time REAL,precision REAL,score INTEGER)")


    def add_user(self,user,time,precision,score):
        self.cursor.execute("""INSERT INTO Scores(user,time,precision,score) VALUES (user,time,precision,score)""")
        self.conn.commit()


    def get_user(self,user1):
        cursor=self.conn.execute("SELECT * FROM Scores WHERE user1 = ?",(user1,))
        result=cursor.execute()
        return result